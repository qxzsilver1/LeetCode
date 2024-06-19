-- Write your PostgreSQL query statement below
DELETE FROM Person p2 USING Person p1
WHERE p1.email=p2.email AND p1.id < p2.id;
