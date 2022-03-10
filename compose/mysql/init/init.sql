CREATE USER 'jw'@'%' IDENTIFIED BY 'mysql';
GRANT ALL ON eastridge.* TO 'jw'@'%';
FLUSH PRIVILEGES;