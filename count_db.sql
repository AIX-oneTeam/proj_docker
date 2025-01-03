-- init.sql
CREATE TABLE IF NOT EXISTS counter (
    id INT PRIMARY KEY,
    value INT DEFAULT 0
);

INSERT INTO counter (id, value) VALUES (1, 0) ON DUPLICATE KEY UPDATE value = value;