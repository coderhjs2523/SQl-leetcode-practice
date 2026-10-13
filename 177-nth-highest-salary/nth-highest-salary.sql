CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT MAX(T.salary)
      FROM (
        SELECT salary, DENSE_RANK() OVER(ORDER BY salary DESC) AS rnk
        FROM Employee
        ) T
      WHERE T.rnk = N  
  );
END