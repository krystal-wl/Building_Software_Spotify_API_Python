import pytest
from analysis import Analysis


def test_compute_analysis():
    # initialize an instance of Analysis in the test
    analysis_obj = Analysis('configs/analysis_config.yml') 
    
    # compute_analysis calculates the mean popularity
    analysis_obj.dataset_tracks_popularity = [80, 90, 100] 
    result = analysis_obj.compute_analysis()

    # assert that the result is as expected
    assert result == 90