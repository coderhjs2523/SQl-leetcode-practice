SELECT T.Department AS Department, T.Employee AS Employee, T.Salary AS Salary
FROM(
    SELECT 
    E.name AS Employee,
    D.name AS Department,
    E.salary AS Salary,
    DENSE_RANK() OVER(PARTITION BY D.name ORDER BY E.salary DESC) AS rnk
    FROM Employee E
    JOIN Department D ON E.departmentId = D.id
    ) T
WHERE T.rnk = 1;