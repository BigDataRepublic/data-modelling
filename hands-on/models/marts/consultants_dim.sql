{{
    config(
        materialized="view",
    )
}}

WITH _base_consultants AS (
    SELECT * FROM {{ref('consultants')}}
)

SELECT
    bc.ConsultantID,
    bc.Name,
    bc.Surname,
    bc.ClientName,
    bc.ProjectName,
FROM _base_consultants bc