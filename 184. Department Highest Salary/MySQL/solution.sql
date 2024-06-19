# Write your MySQL query statement below
SELECT D.name as Department, E.name as Employee, E.salary as Salary
FROM Employee as E, Department as D
WHERE (E.departmentId, salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
)
AND E.departmentId=D.id;
