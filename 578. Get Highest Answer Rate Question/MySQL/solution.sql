# Write your MySQL query statement below
SELECT question_id AS survey_log
FROM SurveyLog
GROUP BY 1
ORDER BY (COUNT(answer_id) / COUNT(CASE WHEN action='show' THEN question_id ELSE NULL END)) DESC, 1 ASC
LIMIT 1;
