{{
    config(
        materialized="incremental",
        unique_key=['SnapshotDate', 'ConsultantID', 'ClientName', 'ProjectName', 'Title', 'YearsOfExperience'],
        incremental_strategy="delete+insert"
    )
}}

WITH base AS (
    SELECT
        *
    FROM {{ source('raw', 'Consultants') }}
    WHERE
        SnapshotDate IS NOT NULL
        AND ConsultantID IS NOT NULL
        AND Name IS NOT NULL
        AND Surname IS NOT NULL
        AND ClientName IS NOT NULL
        AND ProjectName IS NOT NULL
        AND Title IS NOT NULL
        AND YearsOfExperience IS NOT NULL
)

SELECT * FROM base

{% if is_incremental() %}

WHERE
    SnapshotDate > (SELECT MAX(SnapshotDate) FROM {{ this }})

{% endif %}
