{{
    config(
        materialized="view",
    )
}}

WITH _base_session_facts AS (
    SELECT 
        sd.Subject,
        sd.Topic,
        AVG(sf.YearsOfExperience) AS AvgYearsOfExperience
    FROM {{ref('session_facts')}} sf
    JOIN {{ref('session_dim')}} sd
        ON sf.SessionID = sd.SessionID
    GROUP BY sd.Subject, sd.Topic
)

SELECT 
    bsf.Subject,
    bsf.Topic,
    bsf.AvgYearsOfExperience
FROM _base_session_facts bsf