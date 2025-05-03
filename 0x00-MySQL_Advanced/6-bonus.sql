-- stored procedure to add bonus
DELIMITER |

CREATE PROCEDURE AddBonus(
    IN in_user_id INT,
    IN in_project_name VARCHAR(255),
    IN in_score INT
)
BEGIN
    DECLARE project_id INT;
	-- insert/update the new project 
    INSERT INTO projects (name)
    VALUES (in_project_name)
    ON DUPLICATE KEY UPDATE id = LAST_INSERT_ID(id);
	-- get the lastinserted proj ID
    SET project_id = LAST_INSERT_ID();
	-- update the user score
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (in_user_id, project_id, in_score);
END;
|
DELIMITER ;
