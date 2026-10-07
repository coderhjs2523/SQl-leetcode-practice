SELECT 
    T.Department,
    T.Employee,
    T.salary
FROM (SELECT 
    D.name AS Department, 
    E.name AS Employee, 
    E.salary,
    RANK() OVER (PARTITION BY D.name ORDER BY E.salary DESC) AS salary_rank
    FROM Employee E
    JOIN Department D ON E.departmentId = D.id
    ) T
WHERE T.salary_rank = 1;