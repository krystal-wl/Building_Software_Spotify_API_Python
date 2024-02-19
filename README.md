# Analysis Script

## Overview

This Python script, `analysis.py`, is designed to perform data analysis on Spotify's top tracks. It retrieves data via the Spotify API, conducts analysis to compute average track popularity, and generates a plot visualizing the data. Additionally, it notifies the user upon completion of analysis via the ntfy.sh service.

## Features

- Data retrieval from Spotify API
- Analysis of track popularity
- Data visualization with matplotlib
- Notification on analysis completion

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Pipenv or virtual environment for Python
- A Spotify Developer account for API access
- An ntfy.sh account for notifications

## Installation

To install the package directly from GitHub, use the following command:

```bash
!pip install git+https://github.com/user/yourteamrepo
```


## Configuration
Before using the Analysis package, you need to set up the necessary configuration files:

* System and User Configuration: Create system_config.yml and user_config.yml in a configs directory with appropriate settings.

* Spotify API Credentials: Ensure you have a secrets.yml file with your Spotify client ID and secret:
  ```bash
  CLIENT_ID: 'your-spotify-client-id'
  CLIENT_SECRET: 'your-spotify-client-secret'
  ```
* Analysis Configuration: The config.yml should include parameters relevant to your analysis, such as API tokens, plot configurations, and notification settings.

## Usage
After installing the package, you can use it in your projects as follows:
  
  ```bash
  from yourteamrepo import Analysis
  
  analysis_obj = Analysis('config.yml')
  analysis_obj.load_data()
  
  analysis_output = analysis_obj.compute_analysis()
  print(analysis_output)
  
  analysis_figure = analysis_obj.plot_data()
  ```


This code snippet demonstrates how to initialize the analysis, load data, compute the analysis, and plot the results.

## Contributing
We welcome contributions to improve the Analysis package. Please refer to our CONDUCT.md for guidelines on contributions and community behavior.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
Krystal Lin: krystal.lin.work@gmail.com

Project Link: https://github.com/Krystal-WL/Building_software_assignment

