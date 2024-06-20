# Write your MySQL query statement below
SELECT t1.date1, ROUND(IFNULL(SUM(CASE WHEN t2.ind='a' THEN t2.cnt ELSE 0 END) / SUM(CASE WHEN t2.ind='r' THEN t2.cnt ELSE 0 END), 0), 2) AS accept_rate
FROM (
    SELECT DISTINCT request_date AS date1 FROM FriendRequest UNION
    SELECT DISTINCT accept_date  AS date1 FROM RequestAccepted
) t1 
LEFT JOIN (
    SELECT a.request_date AS date1, COUNT(*) AS cnt, 'r' AS ind
    FROM (
        SELECT sender_id, send_to_id, MIN(request_date) AS request_date
        FROM FriendRequest
        GROUP BY sender_id, send_to_id
    ) a
    GROUP BY a.request_date
    
    UNION ALL
    
    SELECT b.accept_date AS date1, COUNT(*) AS cnt, 'a' as ind
    FROM (
        SELECT requester_id, accepter_id, MIN(accept_date) AS accept_date
        FROM RequestAccepted
        GROUP BY requester_id, accepter_id
    ) b
    GROUP BY b.accept_date
) t2
ON t1.date1 >= t2.date1
GROUP BY t1.date1
ORDER BY t1.date1;
