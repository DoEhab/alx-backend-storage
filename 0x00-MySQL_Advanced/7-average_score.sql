-- calculate and update score for a user
DROP PROCEDURE IF EXISTS `ComputeAverageScoreForUser`;

DELIMITER |

CREATE PROCEDURE ComputeAverageScoreForUser (IN in_user_id INT)
BEGIN
	UPDATE users
	SET average_score = (SELECT AVG(score) FROM corrections WHERE user_id = in_user_id)
	WHERE id = in_user_id;
END;
|

DELIMITER ;
