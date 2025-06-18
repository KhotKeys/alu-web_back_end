-- Stored procedure to compute and update average weighted score for a user

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
    DECLARE avg_weighted_score FLOAT DEFAULT 0;

    SELECT
        SUM(c.score * p.weight),
        SUM(p.weight)
    INTO
        total_weighted_score,
        total_weight
    FROM
        corrections c
        JOIN projects p ON c.project_id = p.id
    WHERE
        c.user_id = user_id;

    IF total_weight > 0 THEN
        SET avg_weighted_score = total_weighted_score / total_weight;
    ELSE
        SET avg_weighted_score = 0;
    END IF;

    UPDATE users
    SET average_score = avg_weighted_score
    WHERE id = user_id;
END //

DELIMITER ;
