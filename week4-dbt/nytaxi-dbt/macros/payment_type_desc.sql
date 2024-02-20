{#
    This macro returns the description of the payment_type 
#}


{% macro get_payment_type_description(payment_type) -%}  {#This in python is like the function definition#}

    CASE
        WHEN payment_type = 1 THEN 'First'
        WHEN payment_type = 2 THEN 'Second'
        WHEN payment_type = 3 THEN 'Third'
        ELSE 'Other'
    END AS payment_type_exp

{%- endmacro %}