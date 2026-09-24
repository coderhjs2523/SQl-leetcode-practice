SELECT person_name
FROM (
    SELECT person_name,
           SUM(weight) OVER (ORDER BY turn) AS TotalWeight
    FROM Queue
) t
WHERE TotalWeight <= 1000
ORDER BY TotalWeight DESC
LIMIT 1;