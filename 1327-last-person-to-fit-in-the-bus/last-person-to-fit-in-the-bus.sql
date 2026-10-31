SELECT
T.person_name AS person_name
FROM(
    SELECT
        person_name,
        SUM(weight) OVER(ORDER BY turn) AS last_fit
        FROM Queue
) T
WHERE T.last_fit <= 1000
ORDER BY T.last_fit DESC
LIMIT 1;