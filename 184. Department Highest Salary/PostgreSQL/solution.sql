-- Write your PostgreSQL query statement below
SELECT d.name AS Department, e.name as Employee, e.salary as Salary
FROM Employee e, Department d
WHERE (e.departmentId, salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
)
AND e.departmentId=d.id;
