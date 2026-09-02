# Write your MySQL query statement below
SELECT DISTINCT name
FROM Candidate c
LEFT JOIN Vote v ON v.candidateId=c.id
GROUP BY 1
ORDER BY COUNT(v.candidateId) DESC
LIMIT 1;
