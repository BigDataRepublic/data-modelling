{{
    config(
        materialized="incremental",
        unique_key=['Date', 'HandsOnID'],
        incremental_strategy="append"
    )
}}

WITH base AS (
    SELECT
        *
    FROM {{ source('raw', 'HandsOn') }}
    WHERE
        Date IS NOT NULL
        AND HandsOnID IS NOT NULL
)

SELECT * FROM base

{% if is_incremental() %}

WHERE
    Date > (SELECT MAX(Date) FROM {{ this }})

{% endif %}
