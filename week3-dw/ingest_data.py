import pandas as pd
from google.cloud import storage

# URLs of the Parquet files
parquet_urls = [
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-01.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-02.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-03.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-04.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-05.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-06.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-07.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-08.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-09.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-10.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-11.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-12.parquet"
]

# Google Cloud Storage details
bucket_name = "dezoomcamp-bucket-sai"
destination_blob_name = "green_taxi_2022.parquet"
gcs_credentials_path = "./keys/learningde-e2fe40923135.json"

# Function to download and combine Parquet files
def download_and_combine_parquet_files(urls):
    dfs = []  # List to store individual dataframes
    for url in urls:
        df = pd.read_parquet(url, engine='pyarrow')
        dfs.append(df)
    # Combine all dataframes into one
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df

# Function to upload the combined Parquet file to GCS
def upload_to_gcs(dataframe, bucket_name, destination_blob_name, credentials_path):
    # Authenticate with GCS
    storage_client = storage.Client.from_service_account_json(credentials_path)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    
    # Save the dataframe to a Parquet file in a temporary location
    temp_file = "/tmp/combined_parquet_file.parquet"
    dataframe.to_parquet(temp_file, engine='pyarrow', index=False)
    
    # Upload the file to GCS
    blob.upload_from_filename(temp_file)
    print(f"File {destination_blob_name} uploaded to {bucket_name}.")

# Main process
if __name__ == "__main__":
    combined_df = download_and_combine_parquet_files(parquet_urls)
    upload_to_gcs(combined_df, bucket_name, destination_blob_name, gcs_credentials_path)
