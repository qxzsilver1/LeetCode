# Write your MySQL query statement below
WITH followers_count AS (
    SELECT followee, COUNT(*) AS followers
    FROM Follow
    GROUP BY followee
), following_count AS (
    SELECT follower
    FROM Follow
    GROUP BY follower
)

SELECT f1.follower, f2.followers AS num
FROM following_count AS f1 JOIN followers_count AS f2 ON f1.follower = f2.followee
ORDER BY 1;
