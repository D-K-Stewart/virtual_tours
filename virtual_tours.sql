-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema virtual_tours
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `virtual_tours` ;

-- -----------------------------------------------------
-- Schema virtual_tours
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `virtual_tours` DEFAULT CHARACTER SET utf8 ;
USE `virtual_tours` ;

-- -----------------------------------------------------
-- Table `virtual_tours`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `virtual_tours`.`users` ;

CREATE TABLE IF NOT EXISTS `virtual_tours`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `virtual_tours`.`tours`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `virtual_tours`.`tours` ;

CREATE TABLE IF NOT EXISTS `virtual_tours`.`tours` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `location` VARCHAR(255) NULL,
  `description` VARCHAR(445) NULL,
  `date` DATE NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tours_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_tours_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `virtual_tours`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `virtual_tours`.`favorites`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `virtual_tours`.`favorites` ;

CREATE TABLE IF NOT EXISTS `virtual_tours`.`favorites` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `tour_id` INT NOT NULL,
  PRIMARY KEY (`id`, `user_id`, `tour_id`),
  INDEX `fk_users_has_videos_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_favorites_tours1_idx` (`tour_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_videos_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `virtual_tours`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favorites_tours1`
    FOREIGN KEY (`tour_id`)
    REFERENCES `virtual_tours`.`tours` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
