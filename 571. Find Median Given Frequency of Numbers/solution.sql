# Write your MySQL query statement below
WITH cte1 AS (
    SELECT FLOOR((SUM(frequency) + 1) / 2) as m1, FLOOR((SUM(frequency) + 2) / 2) as m2
    FROM Numbers
), cte2 AS (
    SELECT num, SUM(frequency) OVER (ORDER BY num ROWS UNBOUNDED PRECEDING) AS prefix_sum
    FROM Numbers
), n1 AS (
    SELECT num
    FROM cte2
    WHERE prefix_sum >= (SELECT m1 FROM cte1) LIMIT 1
), n2 AS (
    SELECT num
    FROM cte2
    WHERE prefix_sum >= (SELECT m2 FROM cte1) LIMIT 1
)

SELECT AVG(num) AS median
FROM (SELECT * FROM n1 UNION SELECT * FROM n2) t;
