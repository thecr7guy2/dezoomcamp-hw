import pyarrow as pa
import os 


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/home/src/docker-envs/learningde-e2fe40923135.json'
bucket_name = 'dezoomcamp-bucket-sai'
project_id = 'learningde'
table_name = 'green_taxi'
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here
    gcs = pa.fs.GcsFileSystem()
    patable = pa.Table.from_pandas(data)

    pa.parquet.write_to_dataset(patable,root_path,
    partition_cols=['lpep_pickup_date'],filesystem=gcs)

