import pyarrow as pa
import os 

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test



os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/home/src/docker-envs/learningde-e2fe40923135.json'
bucket_name = 'dezoomcamp-bucket-sai'
project_id = 'learningde'
table_name = 'green_taxi'
root_path = f'{bucket_name}/{table_name}'

@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here
    gcs = pa.fs.GcsFileSystem()
    arrow_df = pa.parquet.ParquetDataset(root_path, filesystem=gcs)
    arrow_df = arrow_df.read_pandas().to_pandas()
    return arrow_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
