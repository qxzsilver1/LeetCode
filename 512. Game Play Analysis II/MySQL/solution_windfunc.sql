# Write your MySQL query statement below
SELECT player_id, device_id
FROM (
    SELECT player_id, device_id, event_date, 
    ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS event_row FROM Activity
) t
WHERE t.event_row=1;
