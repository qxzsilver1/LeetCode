-- Write your PostgreSQL query statement below
SELECT ROUND(COUNT(*)::numeric / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity
WHERE (player_id, event_date) IN (
    SELECT player_id, MIN(event_date) + INTERVAL '1 day' AS event_date
    FROM Activity
    GROUP BY player_id
);
