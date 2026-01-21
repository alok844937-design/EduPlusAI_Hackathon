SELECT 
userid, 
AVG(score) as average_score
FROM `eduplus.students_scores`'
GROUP BY user_id;