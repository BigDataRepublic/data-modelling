{{
    config(
        materialized="incremental",
        unique_key=['Date', 'SessionID'],
        incremental_strategy="append"
    )
}}

WITH base AS (
    SELECT
        *
    FROM {{ source('raw', 'Session') }}
    WHERE
        Date IS NOT NULL
        AND SessionID IS NOT NULL
        AND Subject IS NOT NULL
        AND Topic IS NOT NULL
        AND FullTitle IS NOT NULL
        AND HandsOnID IS NOT NULL
)

SELECT * FROM base

{% if is_incremental() %}

WHERE
    Date > (SELECT MAX(Date) FROM {{ this }})

{% endif %}
