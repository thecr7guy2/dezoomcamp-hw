import io
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def magichahaha(base_url, months):
    data_frames = []

    for month in months:
        url = base_url.format(month)
        response = requests.get(url)
        if response.status_code == 200:
            df = pd.read_parquet(io.BytesIO(response.content))
            data_frames.append(df)
        else:
            print(f"Failed to fetch data for month {month}: HTTP {response.status_code}")

    return pd.concat(data_frames, ignore_index=True)


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2020-{}.parquet"
    months = [10,11,12]
    con_df = magichahaha(base_url,months)

    return con_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
