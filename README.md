# habi-test-api
Repository for HABI test, we are going to create a microservice of  rest type that connects to a MYSQL database

## Getting Started

1) Clone project from https://github.com/felipe2323/habi-test-api
2) Open a terminal and install prerequisites
3) Create a virtualenv and install requirements.txt

## Prerequisites

1) Python 3.7+
2) Pip
3) Virtualenv
4) Python libraries on requirements.txt 

## Deployment 

1) Open a terminal into the project directory
2) Create virtual env -> python3 -m venv name_venv
3) Activate virtual env -> source name_venv / bin / activate
4) Install python dependencies -> pip3 install -r requirements.txt
5) Deploy microservice -> uvicorn index:app --reload

## Technologies (Why were they chosen?)

#### Python
Language required for the test

#### Fast API
Is a library that is being very popular for the creation of microservices type rest

#### PyMySQL
Library required for connection with a MYSQL database engine

#### SQLAlchemy
It is the most popular orm to work with SQL, it integrates perfectly with Fast API, 
although its use is purely theoretical and it remains an alternative in the source code, 
because plain SQL was used.

#### PyTest
Required for unit tests

## EndPoints 

1) localhost:8000/
	- GET: Home microservice
	
2) localhost:8000/docs
	- GET: Get Automatic docs by Swagger UI
	
3) localhost:8000/properties/
	- GET: Search properties with filters (year, city, status)
	
4) localhost:8000/properties/{id}
	- GET: Search property by identifier
	


## Concept New service ("Like")

#### Current ER Diagram

![ScreenShot](/screnshots/entity_current.png)


#### Extended ER Diagram

![ScreenShot](/screnshots/entity_extend.png)

* Basically we add a new user table, the table can be extended with many more attributes, 
for the exercise, it will only have the id and the name.

* Also we can add an intermediate table, which will allow us to store "likes" history.

* The table also has an attribute called is_like, 1 if it was a like, and 0, if it removed a like.

* We can assume with this data model, that if we want to consult: 
if any property has "like" for some user. We simply look for the last inserted record 
and we will verificate is_like field

#### SQL Extend

```
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


-- -----------------------------------------------------
-- Schema habi_test_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `habi_test_db` ;
USE `habi_test_db` ;


-- -----------------------------------------------------
-- Table `habi_test_db`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `habi_test_db`.`user` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `habi_test_db`.`likes_history`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `habi_test_db`.`likes_history` (
  `id` INT NOT NULL,
  `property_id` INT(11) NOT NULL,
  `user_id` INT NOT NULL,
  `like_date` DATETIME NULL,
  `is_like` TINYINT(1) NULL,
  PRIMARY KEY (`id`, `property_id`, `user_id`),
  INDEX `fk_property_has_user_user1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_property_has_user_property1_idx` (`property_id` ASC) VISIBLE,
  CONSTRAINT `fk_property_has_user_property1`
    FOREIGN KEY (`property_id`)
    REFERENCES `habi_test_db`.`property` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_property_has_user_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `habi_test_db`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

```

# Plus 




## Database design proposal.

![ScreenShot](/screnshots/entity_modify.png)

Basically I will remove the table status_history, and I would create a direct relationship with the status, thinking that in the microservice, 
we are only bringing the last state of that historical table, discarding everything else. Unless we need the status history for something else. 
But I think that we can increase speed up the speed of the query if we will reduce this intermediate table.



## Run Unit test

1) Open a terminal into the project directory
2) Activate virtual env -> source name_venv / bin / activate
3) Run unit tests writing on terminal -> pytest


## Video Demostration

https://youtu.be/D1JNfgYOpLw

		
## Interesting links

* [Fast API](https://fastapi.tiangolo.com/) - The rest framework used
* [Pip](https://pypi.org/project/pip/) - Package Management
* [MYSQL](https://www.mysql.com/) - Database engine


## Authors

* **Luis Felipe Valencia Alvarez**

## License

This project is licensed under the MIT License
