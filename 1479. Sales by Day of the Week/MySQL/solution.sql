# Write your MySQL query statement below
SELECT item_category as category,
SUM(IF(WEEKDAY(order_date) = 0, quantity, 0)) AS Monday,
SUM(IF(WEEKDAY(order_date) = 1, quantity, 0)) AS Tuesday,
SUM(IF(WEEKDAY(order_date) = 2, quantity, 0)) AS Wednesday,
SUM(IF(WEEKDAY(order_date) = 3, quantity, 0)) AS Thursday,
SUM(IF(WEEKDAY(order_date) = 4, quantity, 0)) AS Friday,
SUM(IF(WEEKDAY(order_date) = 5, quantity, 0)) AS Saturday,
SUM(IF(WEEKDAY(order_date) = 6, quantity, 0)) AS Sunday
FROM Items LEFT JOIN Orders ON Items.item_id = Orders.item_id
GROUP BY item_category
ORDER BY item_category
