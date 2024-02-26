{{
    config(
        materialized='table'
    )
}}


with fhv_trips as (select * from {{ ref('stg_fhv_trips_2019') }}),
dim_zones as (select * from {{ ref('dim_zones') }})

select fhv_trips.tripid,
       'fhv' as service_type,
       fhv_trips.dispatching_base_id,
       fhv_trips.pickup_locationid,
       pickup_j.zone as pickup_zone,
       pickup_j.borough as pickup_borough,
       fhv_trips.dropoff_locationid,
       dropoff_j.zone as dropoff_zone,
       dropoff_j.borough as dropoff_borough,
       fhv_trips.pickup_year,
       fhv_trips.pickup_datetime,
       fhv_trips.dropoff_datetime
from fhv_trips
inner join dim_zones as pickup_j
on fhv_trips.pickup_locationid = pickup_j.locationid
inner join dim_zones as dropoff_j
on fhv_trips.dropoff_locationid = dropoff_j.locationid


{% if var('is_test_run', default= True) %}

  limit 100

{% endif %}




