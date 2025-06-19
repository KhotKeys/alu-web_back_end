DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
    DECLARE avg_weighted_score FLOAT DEFAULT 0;

    -- Calculate total weighted score and total weight for the user's projects
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

    -- Prevent division by zero
    IF total_weight > 0 THEN
        SET avg_weighted_score = total_weighted_score / total_weight;
    ELSE
        SET avg_weighted_score = 0;
    END IF;

    -- Update the user's average_score
    UPDATE users
    SET average_score = avg_weighted_score
    WHERE id = user_id;
END //

DELIMITER ;
