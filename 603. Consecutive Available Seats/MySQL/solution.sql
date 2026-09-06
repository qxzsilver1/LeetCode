# Write your MySQL query statement below
SELECT DISTINCT A.seat_id
FROM Cinema A JOIN Cinema B ON ABS(A.seat_id - B.seat_id) = 1 AND A.free = TRUE and B.free = TRUE
ORDER BY A.seat_id;
