
CREATE OR REPLACE TABLE `learningde.taxi_trips_hw.fhv_trips_non_partitoned` AS
SELECT * FROM `learningde.taxi_trips_hw.fhv_trips_2019`;

-- coudnt cluster by PUlocationID beacuse it was a float and coudnt partition because the date time column was a string
-- The data will be transformed by/in dbt instead during ingestion.

CREATE TABLE `learningde.taxi_trips_hw.green_trips_non_partitioned` AS
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2019`;

INSERT INTO `learningde.taxi_trips_hw.green_trips_non_partitioned`
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2020`;

-- Created green trips data 

CREATE TABLE `learningde.taxi_trips_hw.yellow_trips_non_partitioned` AS
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2019`;

INSERT INTO `learningde.taxi_trips_hw.yellow_trips_non_partitioned`
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2020`;

-- Created yellow trips data 