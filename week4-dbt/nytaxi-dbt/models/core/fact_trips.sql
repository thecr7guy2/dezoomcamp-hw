{{
    config(
        materialized='table'
    )
}}


with green_trips as (select *, 'Green' as service_type from {{ ref('stg_green_trips_non_partitioned') }} ),
yellow_trips as (select *, 'Yellow' as service_type from {{ ref('stg_yellow_trips_non_partitioned') }} ),
trips_unioned as (select * from green_trips union all select * from yellow_trips),
dim_zones as (select * from {{ ref('dim_zones') }})

select trips_unioned.tripid, 
    trips_unioned.vendorid, 
    trips_unioned.service_type,
    trips_unioned.ratecodeid, 
    trips_unioned.pickup_locationid, 
    pickup_j.borough as pickup_borough, 
    pickup_j.zone as pickup_zone,
    trips_unioned.dropoff_locationid,
    dropoff_j.borough as dropoff_borough,
    dropoff_j.zone as dropoff_zone,
    trips_unioned.pickup_datetime, 
    trips_unioned.dropoff_datetime, 
    trips_unioned.store_and_fwd_flag, 
    trips_unioned.passenger_count, 
    trips_unioned.trip_distance, 
    trips_unioned.trip_type, 
    trips_unioned.fare_amount, 
    trips_unioned.extra, 
    trips_unioned.mta_tax, 
    trips_unioned.tip_amount, 
    trips_unioned.tolls_amount, 
    trips_unioned.ehail_fee, 
    trips_unioned.improvement_surcharge, 
    trips_unioned.total_amount, 
    trips_unioned.payment_type, 
    trips_unioned.payment_type_description

from trips_unioned
inner join dim_zones as pickup_j
on trips_unioned.pickup_locationid = pickup_j.locationid
inner join dim_zones as dropoff_j
on trips_unioned.dropoff_locationid = dropoff_j.locationid

{% if var('is_test_run', default= True) %}

  limit 100

{% endif %}


