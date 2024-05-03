{{
    config(
        materialized="view",
    )
}}

WITH _base_session AS (
    SELECT * FROM {{ref('session')}}
), 

_base_handson AS (
    SELECT * FROM {{ref('handson')}}
),

_base_externals AS (
    SELECT * FROM {{ref('externals')}}
),

_base_externals_grouped AS (
    SELECT SessionID,  ARRAY_AGG(Email) AS ExternalEmails
    FROM _base_externals
    GROUP BY SessionID
)

SELECT
    bs.SessionID,
    bs.Subject,
    bs.Topic,
    bs.Date,
    bh.RepositoryURL,
    beg.ExternalEmails
FROM _base_session bs
JOIN _base_handson bh
    ON bs.HandsOnID = bh.HandsOnID
JOIN _base_externals_grouped beg
    ON bs.SessionID = beg.SessionID