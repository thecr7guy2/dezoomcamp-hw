-- count of records for the 2022 Green Taxi Data
SELECT COUNT(*) FROM `learningde.ny_taxi_data.green_taxi_2022_external`;

-- Ceating a materialized table where the data is stored in GBQ
CREATE OR REPLACE TABLE `learningde.ny_taxi_data.green_tripdata_non_partitoned` AS
SELECT * FROM `learningde.ny_taxi_data.green_taxi_2022_external`;

-- Query to count the distinct number of PULocationIDs for the entire dataset on the external table
-- Scanning ~ 0 MB of DATA
SELECT COUNT(DISTINCT PULocationID) AS unique_count FROM `learningde.ny_taxi_data.green_taxi_2022_external`;

-- Query to count the distinct number of PULocationIDs for the entire dataset on the materialized table
-- Scanning ~ 6.41 MB of DATA
SELECT COUNT(DISTINCT PULocationID) AS unique_count FROM `learningde.ny_taxi_data.green_tripdata_non_partitoned`;

-- Query to count the total number of records having a fare_amount of 0
SELECT COUNT(*) AS zero_fare_count FROM `learningde.ny_taxi_data.green_tripdata_non_partitoned` WHERE fare_amount = 0;

-- Creating a partition and cluster table
CREATE OR REPLACE TABLE `learningde.ny_taxi_data.green_tripdata_partitoned_clustered`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS
SELECT * FROM `learningde.ny_taxi_data.green_taxi_2022_external`;

-- Query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 on the materialized table
-- Scanning ~ 12.82 MB of DATA
SELECT DISTINCT PULocationID
FROM `learningde.ny_taxi_data.green_tripdata_non_partitoned`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

-- Query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 on the partitioned and clustered table
-- Scanning ~ 1.12 MB of DATA
SELECT DISTINCT PULocationID
FROM `learningde.ny_taxi_data.green_tripdata_partitoned_clustered`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

-- Scanning ~ 0 MB of DATA
SELECT COUNT(*) FROM `learningde.ny_taxi_data.green_tripdata_non_partitoned`;
-- The Reason for this is because the number of rows is already in the metadata and Bigquery uses that to display the result instead 