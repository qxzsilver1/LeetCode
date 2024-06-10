# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT *, LAG(num) OVER (ORDER BY id) AS previous,
    LEAD(num) OVER (ORDER BY id) AS subsequent,
    LAG(id) OVER (ORDER BY id) AS prevId,
    LEAD(id) OVER (ORDER BY id) AS nextId
    FROM Logs
) AS tmp
WHERE id=nextId-1 AND id=prevId+1 AND num=previous AND num=subsequent;
