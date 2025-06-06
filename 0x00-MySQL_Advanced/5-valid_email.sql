-- change valid email upon insert
DELIMITER //

CREATE TRIGGER reset_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = FALSE;
    END IF;
END;
//

DELIMITER ;
