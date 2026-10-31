SELECT
T.Department,
T.Employee,
T.Salary
FROM
    (
    SELECT 
        D.name AS Department,
        E.name AS Employee,
        E.salary AS Salary,
        DENSE_RANK() OVER(PARTITION BY D.name ORDER BY E.salary DESC) AS rnk 
        FROM Employee E
        JOIN Department D ON E.departmentId = D.id
    ) T
WHERE T.rnk = 1;