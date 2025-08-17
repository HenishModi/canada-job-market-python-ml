-- Province-wise average salary
SELECT province, AVG(estimated_salary) AS avg_salary
FROM job_postings
GROUP BY province;

-- Monthly job posting trends
SELECT month, COUNT(*) AS postings
FROM job_postings
GROUP BY month
ORDER BY month;

-- Top 5 highest paying job titles
SELECT job_title, AVG(estimated_salary) AS avg_salary
FROM job_postings
GROUP BY job_title
ORDER BY avg_salary DESC
LIMIT 5;

-- Province with highest demand (most postings)
SELECT province, COUNT(*) AS postings
FROM job_postings
GROUP BY province
ORDER BY postings DESC
LIMIT 1;
