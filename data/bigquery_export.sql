-- Mock BigQuery export for student scores
CREATE TABLE student_scores (
    user_id STRING,
    topic STRING,
    score INT64
);

INSERT INTO student_scores (user_id, topic, score) VALUES
("stu001", "DSA", 8),
("stu002", "Algorithms", 5),
("stu003", "Data Structures", 7);