-- Write your PostgreSQL query statement below
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT id, num, LAG(num) OVER (ORDER BY id) AS prev,
    LEAD(num) OVER (ORDER BY id) AS subseq,
    LAG(id) OVER (ORDER BY id) AS prevId,
    LEAD(id) OVER (ORDER BY id) AS nextId
    FROM Logs
) AS tmp
WHERE id=nextId-1 AND id=prevId+1 AND num=prev AND num=subseq;
