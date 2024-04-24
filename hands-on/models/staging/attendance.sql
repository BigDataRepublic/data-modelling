{{
    config(
        materialized="incremental",
        unique_key=['Date', 'SessionID', 'ConsultantID'],
        incremental_strategy="append"
    )
}}

WITH base AS (
    SELECT
        *
    FROM {{ source('raw', 'Attendance') }}
    WHERE
        Date IS NOT NULL
        AND SessionID IS NOT NULL
        AND ConsultantID IS NOT NULL
        AND Attendance IS NOT NULL
)

SELECT * FROM base

{% if is_incremental() %}

WHERE
    Date > (SELECT MAX(Date) FROM {{ this }})

{% endif %}
