SELECT AVG(n.num) AS median
FROM Numbers n
WHERE n.frequency >= ABS((
    SELECT SUM(frequency) FROM Numbers WHERE num <= n.num
) - (SELECT SUM(frequency) FROM Numbers WHERE num >= n.num));
