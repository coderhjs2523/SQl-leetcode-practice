SELECT class 
FROM (SELECT COUNT(student) AS TOTAL_STUDENT, class
      FROM Courses
      GROUP BY class
     ) sub
WHERE TOTAL_STUDENT >= 5;