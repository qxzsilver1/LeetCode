# Write your MySQL query statement below
WITH cte1 AS (
    SELECT e1.company, e1.salary, e1.id, COUNT(*) AS salary_rank
    FROM Employee e1 JOIN Employee e2 ON e1.company=e2.company AND
    (e1.salary > e2.salary OR (e1.salary=e2.salary AND e1.id >= e2.id))
    GROUP BY e1.company, e1.salary, e1.id
    ORDER BY e1.company, e1.salary, e1.id
), cte2 AS (
    SELECT company, COUNT(id) AS total_count
    FROM Employee
    GROUP BY company
)

SELECT cte1.id, cte1.company, cte1.salary
FROM cte1 JOIN cte2 ON cte1.company=cte2.company
WHERE cte1.salary_rank BETWEEN (cte2.total_count / 2) AND (cte2.total_count / 2) + 1;
