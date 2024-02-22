{{
    config(
        materialized='view'
    )
}}


with fhv_trips as (

select
    {{ dbt_utils.generate_surrogate_key(['dispatching_base_num', 'pickup_datetime','PUlocationID']) }} as tripid,
    {{ dbt.safe_cast("dispatching_base_num", api.Column.translate_type("string")) }} as dispatching_base_id,


    cast(pickup_datetime as timestamp) as pickup_datetime,
    cast(dropoff_datetime as timestamp) as dropoff_datetime,

    {{ dbt.safe_cast("PUlocationID", api.Column.translate_type("integer")) }} as pickup_locationid,
    {{ dbt.safe_cast("DOlocationID", api.Column.translate_type("integer")) }} as dropoff_locationid

from {{ source('staging', 'fhv_trips_non_partitoned') }}

)


select *, extract (YEAR FROM pickup_datetime) AS pickup_year
from fhv_trips
where EXTRACT(YEAR FROM pickup_datetime) = 2019 


{% if var('is_test_run', default=true) %}

limit 100

{% endif %}


    
    



