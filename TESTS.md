# Non-Automated Test Cases for Analysis Package

## Setup
* Ensure the Analysis package is installed and configured. 
* Required: Python 3.10+, Analysis package, access to terminal/command prompt.

## Test Cases
### Configuration Loading
* Objective: Confirm correct loading of YAML configuration.
* Steps:
  * Create a valid ‘analysis_config.yml’ file with predefined settings.
  * Initialize an ‘Analysis’ object with the path to this configuration file.
  * Verify that the configuration settings are correctly loaded into the ‘Analysis’ object.
* Expected: Configuration matches analysis_config.yml contents.
### Data Loading
* Objective: Test load_data method functionality.
* Steps:
  * call the load_data method on an Analysis object.
  * Manually verify that the dataset_tracks_popularity and dataset_track_names attributes of the Analysis object are populated with the expected data.
* Expected: Attributes contain correct data.
### Analysis Computation
* Objective: Ensure compute_analysis computes correctly.
* Steps:
  * After loading data using the load_data method, call the compute_analysis method.
  * Manually compute the expected analysis result using the same data set.
  * Compare the result from the compute_analysis method to the manually computed result.* 
* Expected: compute_analysis result matches manual computation.
### Error Handling
* Objective: Check error handling for invalid inputs.
* Steps: Use invalid config path, invalid API token, call compute_analysis without data.
* Expected: Meaningful errors for each scenario.
### Plotting
* Objective: Verify plot_data generates and saves plots correctly.
* Steps: Run plot_data after analysis, check saved plot file.
* Expected: Plot accurately represents analyzed data, saved correctly.
