from typing import Any
import base64
import requests
import yaml
import logging
import numpy as np
import matplotlib.pyplot as plt
import os

class Analysis():
    
    def __init__(self, analysis_config: str) -> None:

        ''' Load config into an Analysis object

        Load system-wide configuration from `configs/system_config.yml`, user configuration from
        `configs/user_config.yml`, and the specified analysis configuration file

        Parameters
        ----------
        analysis_config : str
            Path to the analysis/job-specific configuration file

        Returns
        -------
        analysis_obj : Analysis
            Analysis object containing consolidated parameters from the configuration files

        Notes
        -----
        The configuration files should include parameters for:
            * GitHub API token
            * ntfy.sh topic
            * Plot color
            * Plot title
            * Plot x and y axis titles
            * Figure size
            * Default save path

        '''

        CONFIG_PATHS = ['configs/system_config.yml', 'configs/user_config.yml']

        # add the analysis config to the list of paths to load
        paths = CONFIG_PATHS + [analysis_config]

        # initialize empty dictionary to hold the configuration
        config = {}

        # load each config file and update the config dictionary
        for path in paths:
            with open(path, 'r') as f:
                this_config = yaml.safe_load(f)
            config.update(this_config)

        self.config = config

    def load_data(self) -> None:
        ''' Retrieve data from the GitHub API

        This function makes an HTTPS request to the GitHub API and retrieves your selected data. The data is
        stored in the Analysis object.

        Parameters
        ----------
        None

        Returns
        -------
        None

        '''
        # load spotify acccess token from yaml file
        with open('configs/secrets.yml') as f:
            secrets = yaml.safe_load(f)

        client_id = secrets['CLIENT_ID'];
        client_secret = secrets['CLIENT_SECRET'];

        # Encode Client ID and Client Secret
        credentials = f"{client_id}:{client_secret}"
        credentials_encoded = base64.b64encode(credentials.encode()).decode()

        # The headers of the request must contain the following parameters:
        # Authorization: Basic <base64 encoded client_id:client_secret>
        # Content-Type: Set to application/x-www-form-urlencoded
        headers = {
            'Authorization': f'Basic {credentials_encoded}',
            'Content-Type': 'application/x-www-form-urlencoded',
            }

        # set the grant_type parameter to client_credentials
        data = {'grant_type': 'client_credentials'}
        url = 'https://accounts.spotify.com/api/token'

        # make a POST request to get the access token
        response = requests.post(url, headers=headers, data=data)
        token = response.json()

        # request top tracks data after getting the access token
        headers = {'Authorization': 'Bearer ' + token['access_token']}
        artist_id = '06HL4z0CvFAxyc27GXpf02' # artist ID for Taylor Swift
        top_tracks_url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=CA" # endpoints for a artist and a artist's albums and tracks

        top_tracks_data = requests.get(top_tracks_url, headers=headers).json()

        # Extract popularity and track names from the response
        track_popularity = []
        track_names = []

        for track in top_tracks_data['tracks']:
            track_popularity.append(track['popularity'])
            track_names.append(track['name'])
        
        self.dataset_tracks_popularity = track_popularity
        self.dataset_track_names = track_names
        # after loading the data, assert that the result is as expected
        assert isinstance(self.dataset_tracks_popularity, list), "Expected dataset_tracks_popularity to be a list"
        assert isinstance(self.dataset_track_names, list), "Expected dataset_track_names to be a list"
        assert len(self.dataset_tracks_popularity) == len(self.dataset_track_names), "Mismatch in lengths of track popularity and names lists"

    def compute_analysis(self) -> Any:
        '''Analyze previously-loaded data.

        This function runs an analytical measure of mean
        and returns an average of loaded data

        Parameters
        ----------
        None

        Returns
        -------
        analysis_output : Any

        '''
        return np.mean(self.dataset_tracks_popularity)
    
    
    
    def plot_data(self) -> plt.Figure:
        
        '''
        Plot the top tracks data.

        This function generates a horizontal bar chart of the top tracks data and saves it to a specified path.

        Parameters
        ----------
        save_path : str, optional
            Path to save the generated plot, defaults to None

        Returns
        -------
        fig : plt.Figure
            The generated plot figure
        '''

        # Plotting the horizontal bar chart
        plt.barh(self.dataset_track_names, self.dataset_tracks_popularity, color=self.config['plot_color'])
        plt.xlabel(self.config['plot_config']['xlabel'])
        plt.ylabel(self.config['plot_config']['ylabel'])
        plt.title(self.config['plot_config']['title'])

        # initialize logging module
        logging.basicConfig(level=logging.INFO,
            handlers=[logging.StreamHandler(), logging.FileHandler('Top_tracks_popularity.log')],
        )

        # Specify the save path
        save_path = self.config['default_save_path']

        try:
            plt.savefig(save_path, bbox_inches='tight')
            logging.info(f"Plot saved as {save_path}")
        except Exception as e:
            e.add_note("Failed to save the plot")
            raise e
        
    def notify_done(self, message: str) -> None: 
        ''' Notify the user that analysis is complete.

        Send a notification to the user through the ntfy.sh webpush service.

        Parameters
        ----------
        message : str
        Text of the notification to send

        Returns
        -------
        None

        '''
        message = 'Analysis completed'
        if self.config['ntfy_sh_topic']:
            try:
                requests.post(f"https://ntfy.sh/{self.config['ntfy_sh_topic']}", data=message.encode(encoding='utf-8'))
                logging.info("Notification sent successfully")
            except Exception as e:
                logging.error(f"Error sending notification: {e}")
        else:
            logging.warning("ntfy.sh topic not found in configuration, skipping notification")
