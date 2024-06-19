# Write your MySQL query statement below

SELECT D.name as Department, E1.name as Employee, E1.salary as Salary
FROM Employee as E1, Department as D
WHERE
(
    SELECT Count(DISTINCT E2.salary)
    FROM Employee as E2
    WHERE E1.departmentId = E2.departmentId and E2.salary > E1.salary
) < 3
and E1.departmentId = D.id;
