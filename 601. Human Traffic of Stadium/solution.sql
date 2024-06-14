# Write your MySQL query statement below
WITH PeopleOrder AS (
    SELECT *, LAG(people) OVER() AS p1, LEAD(people) OVER() AS p2, LAG(people, 2) OVER() AS p3, LEAD(people, 2) OVER() AS p4
    FROM Stadium
)

SELECT id, visit_date, people
FROM PeopleOrder
WHERE people >= 100 AND p1 >= 100 AND p2 >= 100 
OR people >= 100 AND p1 >= 100 AND p3 >= 100
OR people >= 100 AND p2 >= 100 AND p4 >= 100;
