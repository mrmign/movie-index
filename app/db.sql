SET SESSION storage_engine = "InnoDB";
ALTER DATABASE CHARACTER SET "utf8";

DROP TABLE IF EXISTS movie;
CREATE TABLE movie (
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	title varchar(200) NOT NULL ,
	url varchar(200) NOT NULL ,
	thread_id int, 
    page int NOT NULL DEFAULT 0,
    KEY(title)
);

DROP TABLE IF EXISTS test;
CREATE TABLE test (
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	cont varchar(100)
	);