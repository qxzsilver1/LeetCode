# Write your MySQL query statement below
WITH project_and_employee AS (
    SELECT t0.project_id, t1.employee_id, experience_years
    FROM Project t0 JOIN Employee t1 ON t0.employee_id = t1.employee_id
)

SELECT a.project_id, employee_id
FROM project_and_employee a JOIN (
    SELECT project_id, MAX(experience_years) AS max_experience
    FROM project_and_employee
    GROUP BY 1
) b ON a.project_id = b.project_id AND a.experience_years = b.max_experience;
