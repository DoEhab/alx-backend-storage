-- Trigger to adjust amount upon receiving new order
DELIMITER //

CREATE TRIGGER update_item
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.quantity
    WHERE name = NEW.item_name;
END;
//

DELIMITER ;
