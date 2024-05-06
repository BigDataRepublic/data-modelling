{{
    config(
        materialized="incremental",
        unique_key=['SessionID', 'ConsultantID'],
        incremental_strategy="append"
    )
}}

WITH base AS (
    SELECT
        s.SessionID,
        c.ConsultantID,
        c.YearsOfExperience,
        a.Attendance,
    FROM {{ ref('session') }} s
    JOIN {{ ref('attendance') }} a
        ON s.SessionID = a.SessionID
    JOIN {{ ref('consultants') }} c
        ON a.ConsultantID = c.ConsultantID
)

SELECT 
    base.SessionID,
    base.ConsultantID,
    base.Attendance,
    base.YearsOfExperience,
    ARRAY_LENGTH(sd.ExternalEmails) AS ExternalCount,
    cd.ClientName,
    cd.ProjectName,
FROM base
JOIN {{ref('session_dim')}} sd
    ON base.SessionID = sd.SessionID
JOIN {{ref('consultants_dim')}} cd
    ON base.ConsultantID = cd.ConsultantID
