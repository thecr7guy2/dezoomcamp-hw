import pandas as pd
from google.cloud import storage
import requests
import duckdb
import os 

links = [
"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-01.csv.gz",
"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-02.csv.gz",
"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-03.csv.gz",
"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-04.csv.gz",
"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-05.csv.gz",
"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-06.csv.gz",
"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-07.csv.gz",
"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-08.csv.gz",
"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-09.csv.gz",
"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-10.csv.gz",
"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-11.csv.gz",
"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-12.csv.gz",
]

# Download and combine the datasets

def download_csv(url,download_dir='downloads'):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Extract the filename from the URL
    local_filename = url.split('/')[-1]
    # Construct the valid path by combining the download directory with the filename
    valid_path = os.path.join(download_dir, local_filename)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(valid_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return valid_path 





conn = duckdb.connect(database=':memory:', read_only=False)



table_exists = False  # Flag to track if the table has been created

for csv_url in links:
    local_csv_path = download_csv(csv_url, download_dir='downloads')
    
    if not table_exists:
        # For the first CSV file, create the table
        conn.execute(f"CREATE TABLE your_table_name AS SELECT * FROM read_csv_auto('{local_csv_path}')")
        table_exists = True  # Set the flag to True after creating the table
    else:
        # For subsequent CSV files, append data to the table
        conn.execute(f"INSERT INTO your_table_name SELECT * FROM read_csv_auto('{local_csv_path}')")

conn.execute("""
COPY (SELECT * FROM your_table_name)
TO 'fhv_trips_2019.parquet'
(FORMAT PARQUET, CODEC 'ZSTD', ROW_GROUP_SIZE 8000);
""")



# Google Cloud Storage upload setup
# Make sure to replace 'your-bucket-name' with your actual GCS bucket name
bucket_name = "dezoomcamp-bucket-sai"
destination_blob_name = "fhv_trips_2019.parquet"
credentials_path = "./keys/learningde-e2fe40923135.json"
parquet_file_path = 'fhv_trips_2019.parquet'
 # This is the desired path in your GCS bucket

storage_client = storage.Client.from_service_account_json(credentials_path)
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)

blob.upload_from_filename(parquet_file_path)
print(f"File {destination_blob_name} uploaded to {bucket_name}.")




