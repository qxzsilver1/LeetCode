# Write your MySQL query statement below
SELECT EXTRACT(YEAR_MONTH FROM fr.request_date) AS month, ROUND(IFNULL(COUNT(DISTINCT ra.requester_id, ra.accepter_id) / COUNT(DISTINCT fr.sender_id, fr.send_to_id), 0), 2) AS accept_rate
FROM FriendRequest fr JOIN RequestAccepted ra ON EXTRACT(YEAR_MONTH FROM fr.request_date) = EXTRACT(YEAR_MONTH FROM ra.accept_date)
GROUP BY EXTRACT(YEAR_MONTH FROM fr.request_date);
