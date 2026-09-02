# Write your MySQL query statement below
SELECT id, company, salary
FROM (
    SELECT id, company, salary,
    ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary) salary_rank,
    COUNT(*) OVER (PARTITION BY company) total_cnt
    FROM Employee
) as t
WHERE salary_rank >= total_cnt / 2 and salary_rank <= total_cnt / 2 + 1;
