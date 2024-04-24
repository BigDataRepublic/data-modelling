{{
    config(
        materialized="incremental",
        unique_key=['Date', 'SessionID', 'Email'],
        incremental_strategy="append"
    )
}}

WITH base AS (
    SELECT
        *
    FROM {{ source('raw', 'Externals') }}
    WHERE
        Date IS NOT NULL
        AND SessionID IS NOT NULL
        AND Name IS NOT NULL
        AND Surname IS NOT NULL
        AND Company IS NOT NULL
        AND Email IS NOT NULL
)

SELECT * FROM base

{% if is_incremental() %}

WHERE
    Date > (SELECT MAX(Date) FROM {{ this }})

{% endif %}
