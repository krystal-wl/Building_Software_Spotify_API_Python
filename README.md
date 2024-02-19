# Analysis Script

## Overview

The Analysis package is a Python library designed for performing and visualizing data analysis, specifically tailored for Spotify's top tracks data. It supports data retrieval from the Spotify API, computation of analytical metrics, visualization of analysis results, and sending notifications upon completion of analysis tasks.

## Features

- Data retrieval from the Spotify API
- Computation of analytical metrics such as track popularity
- Visualization of analysis results through plots
- Notification of analysis completion via ntfy.sh service

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Pipenv or virtual environment for Python
- A Spotify Developer account for API access
- An ntfy.sh account for notifications

## Installation

To install the package directly from GitHub, use the following command:

```bash
!pip install git+https://github.com/Krystal-WL/Building_software_assignment
```

## Configuration
Before using the Analysis package, you need to set up the necessary configuration files:

* Spotify API Credentials: Securely store your Spotify API credentials in a secrets.yml file.
* Analysis Configuration: Define your analysis parameters in configs/analysis_config.yml. This file should specify details such as plot configurations and notification settings.

## Usage
After installing the package, you can use it in your projects as follows:
  
  ```bash
  from Building_software_assignment import Analysis
  
  # Initialize the analysis object with your configuration
  analysis_obj = Analysis('configs/analysis_config.yml')

  # Load data from the configured sources
  analysis_obj.load_data()

  # Perform the analysis and print the output
  analysis_output = analysis_obj.compute_analysis()
  print(analysis_output)

  # Plot the analysis results
  analysis_figure = analysis_obj.plot_data()

  # Send a notification upon completion
  analysis_notify = analysis_obj.notify_done('Analysis completed')

  ```

This code snippet demonstrates how to initialize the analysis, load data, compute the analysis, and plot the results.

## Contributing
Contributions to the Analysis package are welcome. Please consult our CONDUCT.md for guidelines on how to contribute in a manner that promotes a respectful and welcoming community.

## License
This project is licensed under the MIT License - see the 'LICENSE' file for details.

## Contact
Krystal Lin: krystal.lin.work@gmail.com

Project Link: https://github.com/Krystal-WL/Building_software_assignment
