-- Creates the db hbtn_0d_2 amd the user user_0d_2 
-- user_0d_2 should have only SELECT privilege in the db hbtn_0d_2
-- The user_0d_2 password should be to user_0d_2_pwd
-- If the db hbtn_0d_2 already exists, the script should not fail
-- If the user user_0d_2 already exists, the script should not fail. 

CREATE DATABASE
    IF NOT EXISTS 'hbtn_0d_2';
CREATE USER
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
 ON 'hbtn_0d_2'.*
 TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
