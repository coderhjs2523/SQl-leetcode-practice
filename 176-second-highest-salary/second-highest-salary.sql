SELECT MAX(T.salary) AS SecondHighestSalary 
FROM (SELECT salary, DENSE_RANK() OVER(ORDER BY salary DESC) AS ranking 
FROM Employee) T
WHERE T.ranking = 2;