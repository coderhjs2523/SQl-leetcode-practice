SELECT T.Department, T.Employee, T.Salary 
FROM (SELECT 
        D.name AS Department, 
        E.name AS Employee, 
        E.Salary,
        DENSE_RANK() OVER(PARTITION BY D.name ORDER BY E.salary DESC) AS salary_rank
    FROM Employee E
    JOIN Department D ON E.departmentId = D.id
    ) AS T
WHERE T.salary_rank <= 3;