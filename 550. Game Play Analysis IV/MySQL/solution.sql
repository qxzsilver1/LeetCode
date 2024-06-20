# Write your MySQL query statement below
SELECT ROUND(SUM(date_diff) / COUNT(DISTINCT player_id), 2) AS fraction
FROM (
    SELECT player_id, DATEDIFF(event_date, MIN(event_date) OVER (PARTITION BY player_id))=1 AS date_diff
    FROM Activity
) AS t;
