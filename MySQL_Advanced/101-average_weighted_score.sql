-- Stored procedure to compute and update average weighted scores for all users

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE uid INT;

    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN user_cursor;

    user_loop: LOOP
        FETCH user_cursor INTO uid;
        IF done THEN
            LEAVE user_loop;
        END IF;

        -- Declare local variables for score calculation
        DECLARE total_weighted_score FLOAT DEFAULT 0;
        DECLARE total_weight INT DEFAULT 0;
        DECLARE avg_weighted_score FLOAT DEFAULT 0;

        -- Calculate total weighted score and total weight for this user
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
            c.user_id = uid;

        -- Compute average and update
        IF total_weight > 0 THEN
            SET avg_weighted_score = total_weighted_score / total_weight;
        ELSE
            SET avg_weighted_score = 0;
        END IF;

        UPDATE users
        SET average_score = avg_weighted_score
        WHERE id = uid;

    END LOOP;

    CLOSE user_cursor;
END //

DELIMITER ;
