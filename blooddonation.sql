create database blooddonation;
use blooddonation;
CREATE TABLE donors (
  donor_id INT AUTO_INCREMENT PRIMARY KEY,
  donor_name VARCHAR(255) NOT NULL,
  age INT,  -- Adjust data type if needed (e.g., TINYINT for ages 0-127)
  gender VARCHAR(10),
  address VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  blood_group VARCHAR(10) NOT NULL,
  other_medical_details TEXT
);
DESC donors;

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Snekha@2402';
SELECT user, plugin FROM mysql.user WHERE user = 'root';
select * from donors;

DELIMITER //
CREATE PROCEDURE delete_donor_id(IN donor_id INT)
BEGIN
    DELETE FROM donors WHERE donors.donor_id = donor_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE update_donor_id(
    IN p_donor_id INT,
    IN p_donor_name VARCHAR(255),
    IN p_age INT,
    IN p_gender VARCHAR(50),
    IN p_address VARCHAR(255),
    IN p_phone_number VARCHAR(20),
    IN p_blood_group VARCHAR(10)
    
)
BEGIN
    UPDATE donors
    SET
        donor_name = p_donor_name,
        age = p_age,
        gender = p_gender,
        address = p_address,
        phone_number = p_phone_number,
        blood_group = p_blood_group
        
    WHERE donor_id = p_donor_id;
END //
DELIMITER ;

CREATE TABLE receiver (
  receiver_id INT AUTO_INCREMENT PRIMARY KEY,
  receiver_name VARCHAR(255) NOT NULL,
  age INT,  -- Adjust data type if needed (e.g., TINYINT for ages 0-127)
  gender VARCHAR(10),
  address VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  blood_group VARCHAR(10) NOT NULL,
  other_medical_details TEXT
);

DELIMITER //
CREATE PROCEDURE delete_receiver_id(IN receiver_id INT)
BEGIN
    DELETE FROM receiver WHERE receiver.receiver_id = receiver_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE update_receiver_id(
    IN p_receiver_id INT,
    IN p_receiver_name VARCHAR(255),
    IN p_age INT,
    IN p_gender VARCHAR(50),
    IN p_address VARCHAR(255),
    IN p_phone_number VARCHAR(20),
    IN p_blood_group VARCHAR(10)
    
)
BEGIN
    UPDATE receiver
    SET
        receiver_name = p_receiver_name,
        age = p_age,
        gender = p_gender,
        address = p_address,
        phone_number = p_phone_number,
        blood_group = p_blood_group
        
    WHERE receiver_id = p_receiver_id;
END //
DELIMITER ;

select * from receiver;


