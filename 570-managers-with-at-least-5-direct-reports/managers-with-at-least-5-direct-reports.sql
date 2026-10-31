SELECT
name
FROM Employee
WHERE id in
(
    SELECT 
        managerId
        FROM Employee 
        GROUP BY managerId
        HAVING COUNT(id) >= 5
);