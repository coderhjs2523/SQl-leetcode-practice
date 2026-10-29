-- SELECT MAX(salary) AS SecondHighestSalary 
-- FROM Employee 
-- WHERE salary < (SELECT MAX(salary) FROM Employee);

SELECT MAX(t.salary) AS SecondHighestSalary 
FROM(
    SELECT salary, 
    DENSE_RANK() OVER(ORDER BY salary DESC) AS rnk
    FROM Employee
    ) t
WHERE t.rnk = 2;