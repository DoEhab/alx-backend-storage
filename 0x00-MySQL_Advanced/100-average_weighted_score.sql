-- CREATE SP to calculate avg score
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER |

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN IN_USER_ID INT)
BEGIN
    DECLARE weighted_sum FLOAT DEFAULT 0;
    DECLARE total_weight FLOAT DEFAULT 0;
    DECLARE avg_weighted_score FLOAT DEFAULT 0;
    
    SELECT SUM(c.score * p.weight),
    SUM(p.weight)
    INTO
		weighted_sum, 
        total_weight
	FROM
		corrections c,
        JOIN 
        projects p ON c.project_id = p.id
    WHERE 
        c.user_id = in_user_id;

	IF total_weight > 0 THEN
        SET avg_weighted_score = weighted_sum / total_weight;
    ELSE
        SET avg_weighted_score = 0;
    END IF;

    UPDATE users
    SET average_score = avg_weighted_score
    WHERE id = in_user_id;
    
END
|
DELIMITER ;
