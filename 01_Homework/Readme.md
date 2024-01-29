# 1 Which tag has the following text? - Automatically remove the container when it exits
    docker run  --help |  grep "Automatically remo
    ve the container when it exits"
        *--rm*                            Automatically remove the container when it exits

# 2    What is version of the package wheel ?

 
    docker run -it python:3.9 bash
    root@0f953d75168d:/# pip list
    Package    Version
    ---------- -------
    pip        23.0.1
    setuptools 58.1.0
    wheel      0.42.0

# 3 How many taxi trips were totally made on September 18th 2019?
Tip: started and finished on 2019-09-18.
Remember that lpep_pickup_datetime and lpep_dropoff_datetime columns are in the format timestamp (date and hour+min+sec) and not in date.

select count(1) FROM green_taxi_data 
where CAST(lpep_pickup_datetime as DATE) = '2019-09-18'
and CAST(lpep_dropoff_datetime as DATE) = '2019-09-18'



# Question 4. Largest trip for each day
Which was the pick up day with the largest trip distance Use the pick up time for your calculations.

SELECT max(trip_distance) , CAST(lpep_pickup_datetime as DATE) as lpeppickupdatetime
FROM public.green_taxi_data
group by CAST(lpep_pickup_datetime as DATE)
order by 1 desc



# Question 5. Three biggest pick up Boroughs
Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?


select z."Borough" , sum(t.total_amount) as somme
from green_taxi_data t
left join taxi_zone z on t."PULocationID" = z."LocationID"
where CAST(t.lpep_pickup_datetime as DATE)  in ('2019-09-18') 
and z."Borough" != 'Unknown'
group by 1
having sum(t.total_amount) > 50000
order by 2 desc


# Question 6. Largest tip

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip? We want the name of the zone, not the id.


with pick_up_zone as (select "LocationID" , "Zone" from taxi_zone where "Zone" = 'Astoria')
select z."Zone" , max(t.tip_amount) as somme
from green_taxi_data t
left join taxi_zone z on t."DOLocationID" = z."LocationID"
join pick_up_zone pz on t."PULocationID" = pz."LocationID"
where CAST(t.lpep_pickup_datetime as DATE)  between '2019-09-01' and  '2019-09-30'
--and t."PULocationID" = 7
group by 1
order by 2 desc

# Question 7. Creating Resources

Terraform used the selected providers to generate the following execution plan. Resource actions
are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.homework_dataset will be created
  + resource "google_bigquery_dataset" "homework_dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "dataset_bq_taxi_ms"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + effective_labels           = (known after apply)
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "EU"
      + max_time_travel_hours      = (known after apply)
      + project                    = "mszoomcamp2024"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = (known after apply)
    }

  # google_storage_bucket.homework-bucket will be created
  + resource "google_storage_bucket" "homework-bucket" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "EU"
      + name                        = "homework-terra-bucket-ms"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []# 1 Which tag has the following text? - Automatically remove the container when it exits
    docker run  --help |  grep "Automatically remo
    ve the container when it exits"
        *--rm*                            Automatically remove the container when it exits

# 2    What is version of the package wheel ?

  *0.42.0*

    docker run -it python:3.9 bash
    root@0f953d75168d:/# pip list
    Package    Version
    ---------- -------
    pip        23.0.1
    setuptools 58.1.0
    wheel      0.42.0

# 3 How many taxi trips were totally made on September 18th 2019?
Tip: started and finished on 2019-09-18.
Remember that lpep_pickup_datetime and lpep_dropoff_datetime columns are in the format timestamp (date and hour+min+sec) and not in date.

select count(1) FROM green_taxi_data 
where CAST(lpep_pickup_datetime as DATE) = '2019-09-18'
and CAST(lpep_dropoff_datetime as DATE) = '2019-09-18'

15612

# Question 4. Largest trip for each day
Which was the pick up day with the largest trip distance Use the pick up time for your calculations.

SELECT max(trip_distance) , CAST(lpep_pickup_datetime as DATE) as lpeppickupdatetime
FROM public.green_taxi_data
group by CAST(lpep_pickup_datetime as DATE)
order by 1 desc

2019-09-26

# Question 5. Three biggest pick up Boroughs
Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?


select z."Borough" , sum(t.total_amount) as somme
from green_taxi_data t
left join taxi_zone z on t."PULocationID" = z."LocationID"
where CAST(t.lpep_pickup_datetime as DATE)  in ('2019-09-18') 
and z."Borough" != 'Unknown'
group by 1
having sum(t.total_amount) > 50000
order by 2 desc

"Brooklyn" "Manhattan" "Queens"


"Brooklyn"
"Manhattan"
"Queens"

# Question 6. Largest tip

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip? We want the name of the zone, not the id.

*JFK Airport*

select z."Zone" , max(t.tip_amount) as somme
from green_taxi_data t
left join taxi_zone z on t."DOLocationID" = z."LocationID"
--left join pick_up_zone pz on t."PULocationID" = pz."LocationID"
where CAST(t.lpep_pickup_datetime as DATE)  between '2019-09-01' and  '2019-09-30'
and t."PULocationID" = 7
group by 1
order by 2 de
with pick_up_zone as (select "LocationID" , "Zone" from taxi_zone where "Zone" = 'Astoria')
select z."Zone" , max(t.tip_amount) as somme
from green_taxi_data t
left join taxi_zone z on t."DOLocationID" = z."LocationID"
join pick_up_zone pz on t."PULocationID" = pz."LocationID"
where CAST(t.lpep_pickup_datetime as DATE)  between '2019-09-01' and  '2019-09-30'
--and t."PULocationID" = 7
group by 1
order by 2 desc

# Question 7. Creating Resources

Terraform used the selected providers to generate the following execution plan. Resource actions
are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.homework_dataset will be created
  + resource "google_bigquery_dataset" "homework_dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "dataset_bq_taxi_ms"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + effective_labels           = (known after apply)
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "EU"
      + max_time_travel_hours      = (known after apply)
      + project                    = "mszoomcamp2024"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = (known after apply)
    }

  # google_storage_bucket.homework-bucket will be created
  + resource "google_storage_bucket" "homework-bucket" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "EU"
      + name                        = "homework-terra-bucket-ms"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.homework_dataset: Creating...
google_storage_bucket.homework-bucket: Creating...
google_bigquery_dataset.homework_dataset: Creation complete after 1s [id=projects/mszoomcamp2024/datasets/dataset_bq_taxi_ms]
google_storage_bucket.homework-bucket: Creation complete after 2s [id=homework-terra-bucket-ms]


              + with_state            = (known after apply)
            }
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.homework_dataset: Creating...
google_storage_bucket.homework-bucket: Creating...
google_bigquery_dataset.homework_dataset: Creation complete after 1s [id=projects/mszoomcamp2024/datasets/dataset_bq_taxi_ms]
google_storage_bucket.homework-bucket: Creation complete after 2s [id=homework-terra-bucket-ms]



