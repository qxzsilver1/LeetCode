-- Write your PostgreSQL query statement below
SELECT d.name AS Department, e1.name AS Employee, e1.salary AS Salary
FROM Employee AS e1, Department AS d
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e1.departmentId=e2.departmentId AND e2.salary > e1.salary
) < 3
AND e1.departmentId = d.id;
