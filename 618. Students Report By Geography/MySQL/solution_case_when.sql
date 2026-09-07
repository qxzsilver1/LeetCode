# Write your MySQL query statement below
SELECT MIN(America) AS America, MIN(Asia) AS Asia, MIN(Europe) AS Europe
FROM (
    SELECT
CASE
WHEN continent = 'America' THEN @am:=@am+1
WHEN continent = 'Asia' THEN @as:=@as+1
WHEN continent = 'Europe' THEN @eu:=@eu+1
END AS rowline,

CASE WHEN continent = 'America' THEN name END AS America,
CASE WHEN continent = 'Asia' THEN name END AS Asia,
CASE WHEN continent = 'Europe' THEN name END AS Europe

FROM student, (SELECT @am:=0, @as := 0, @eu:=0) temp
ORDER BY name) t
GROUP BY rowline;
