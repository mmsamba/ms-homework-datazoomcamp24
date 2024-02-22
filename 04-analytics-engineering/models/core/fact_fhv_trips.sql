{{
    config(
        materialized='table'
    )
}}


with trip_data as (
    select * from {{ ref('stg_fhv_tripdata') }}
),
dim_zones as (
        select * from {{ ref('dim_zones') }}
)

select  
        trip_data.dispatching_base_num,
        trip_data.pickup_datetime,
        trip_data.dropoff_datetime,
        trip_data.pulocationid,
        trip_data.dolocationid,
        trip_data.sr_flag,
        trip_data.affiliated_base_number
        ,pickup_zone.borough as pickup_borough
        ,pickup_zone.zone as pickup_zone
        ,dropoff_zone.borough as dropoff_borough
        ,dropoff_zone.zone as dropoff_zone


        from trip_data
            INNER join dim_zones as pickup_zone 
                on pickup_zone.locationid = trip_data.pulocationid
            INNER join dim_zones as dropoff_zone  
                on dropoff_zone.locationid = trip_data.dolocationid
