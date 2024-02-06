-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `mszoomcamp2024.ny_taxi.external_green_tripdata_2022`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://03-data-warehouse-bucket/green/green_tripdata_2022-*.parquet']
);


-- Create a non partitioned table from external table
CREATE OR REPLACE TABLE `mszoomcamp2024.ny_taxi.green_tripdata_2022` AS
SELECT * FROM `mszoomcamp2024.ny_taxi.external_green_tripdata_2022`;

--Question 1: Question 1: What is count of records for the 2022 Green Taxi Data??
select count(1) FROM `mszoomcamp2024.ny_taxi.external_green_tripdata_2022`;

select count(1) FROM `mszoomcamp2024.ny_taxi.green_tripdata_2022`;

--Question 2:
select  distinct PULocationID FROM `mszoomcamp2024.ny_taxi.external_green_tripdata_2022`;

select  distinct PULocationID  FROM `mszoomcamp2024.ny_taxi.green_tripdata_2022`;


-- Question 3:
select count(1) FROM `ny_taxi.external_green_tripdata_2022` where fare_amount = 0;
select count(1) FROM `ny_taxi.green_tripdata_2022` where fare_amount = 0;

-- Question 4 :
select PULocationID , fare_amount FROM `ny_taxi.green_tripdata_2022` limit 1000;
-- Question 5:
-- Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)
-- Creating a partition  table
CREATE OR REPLACE TABLE `mszoomcamp2024.ny_taxi.green_tripdata_2022_partitoned`
PARTITION BY DATE(lpep_pickup_datetime) AS
SELECT * FROM `mszoomcamp2024.ny_taxi.green_tripdata_2022`;

select  distinct PULocationID FROM `ny_taxi.green_tripdata_2022`
where date(lpep_pickup_datetime) between '2022-06-01' and  '2022-06-30' ;

select  distinct PULocationID FROM `mszoomcamp2024.ny_taxi.green_tripdata_2022_partitoned`
where date(lpep_pickup_datetime) between '2022-06-01' and  '2022-06-30' ;

--select * FROM `ny_taxi.green_tripdata_2022` ; -- 114,11 mb
