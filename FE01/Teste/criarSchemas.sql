-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema pedidos
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `pedidos` ;

-- -----------------------------------------------------
-- Schema pedidos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pedidos` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema Exames
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Exames` ;

-- -----------------------------------------------------
-- Schema Exames
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Exames` ;
USE `pedidos` ;

-- -----------------------------------------------------
-- Table `pedidos`.`Doente`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pedidos`.`Doente` ;

CREATE TABLE IF NOT EXISTS `pedidos`.`Doente` (
  `idDoente` INT NOT NULL,
  `numProcesso` INT NOT NULL,
  `Nome` VARCHAR(45) NOT NULL,
  `Morada` VARCHAR(45) NOT NULL,
  `Telefone` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idDoente`),
  UNIQUE INDEX `numProcesso_UNIQUE` (`numProcesso` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pedidos`.`Pedido`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pedidos`.`Pedido` ;

CREATE TABLE IF NOT EXISTS `pedidos`.`Pedido` (
  `idPedido` INT NOT NULL AUTO_INCREMENT,
  `Estado` VARCHAR(45) NOT NULL,
  `data` DATETIME(6) NOT NULL,
  `Observacoes` VARCHAR(45) NULL,
  `Doente_idDoente` INT NOT NULL,
  `idEpisodio` INT NOT NULL,
  `Relatorio` VARCHAR(250) NULL,
  PRIMARY KEY (`idPedido`),
  INDEX `fk_Pedido_Doente_idx` (`Doente_idDoente` ASC),
  CONSTRAINT `fk_Pedido_Doente`
    FOREIGN KEY (`Doente_idDoente`)
    REFERENCES `pedidos`.`Doente` (`idDoente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pedidos`.`WorkList`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pedidos`.`WorkList` ;

CREATE TABLE IF NOT EXISTS `pedidos`.`WorkList` (
  `idWorkList` INT NOT NULL AUTO_INCREMENT,
  `editTime` TIMESTAMP(6) NOT NULL,
  `Pedido_idPedido` INT NOT NULL,
  `Estado` VARCHAR(45) NOT NULL,
  `data` DATETIME(6) NOT NULL,
  `Observacoes` VARCHAR(45) NULL,
  `Doente_idDoente` INT NOT NULL,
  `idEpisodio` INT NOT NULL,
  `Relatorio` VARCHAR(250) NOT NULL,
  PRIMARY KEY (`idWorkList`),
  INDEX `fk_WorkList_Pedido1_idx` (`Pedido_idPedido` ASC),
  CONSTRAINT `fk_WorkList_Pedido1`
    FOREIGN KEY (`Pedido_idPedido`)
    REFERENCES `pedidos`.`Pedido` (`idPedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `Exames` ;

-- -----------------------------------------------------
-- Table `Exames`.`Doente`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Exames`.`Doente` ;

CREATE TABLE IF NOT EXISTS `Exames`.`Doente` (
  `idDoente` INT NOT NULL,
  `numProcesso` INT NOT NULL,
  `Nome` VARCHAR(45) NOT NULL,
  `Morada` VARCHAR(45) NOT NULL,
  `Telefone` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idDoente`),
  UNIQUE INDEX `numProcesso_UNIQUE` (`numProcesso` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Exames`.`Pedido`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Exames`.`Pedido` ;

CREATE TABLE IF NOT EXISTS `Exames`.`Pedido` (
  `idPedido` INT NOT NULL AUTO_INCREMENT,
  `Estado` VARCHAR(45) NOT NULL,
  `data` DATETIME(6) NOT NULL,
  `Observacoes` VARCHAR(45) NULL,
  `Doente_idDoente` INT NOT NULL,
  `idEpisodio` INT NOT NULL,
  `Relatorio` VARCHAR(250) NOT NULL,
  PRIMARY KEY (`idPedido`),
  INDEX `ce_idx` (`Doente_idDoente` ASC),
  CONSTRAINT `ce`
    FOREIGN KEY (`Doente_idDoente`)
    REFERENCES `Exames`.`Doente` (`idDoente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Exames`.`WorkList`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Exames`.`WorkList` ;

CREATE TABLE IF NOT EXISTS `Exames`.`WorkList` (
  `idWorkList` INT NOT NULL AUTO_INCREMENT,
  `editTime` TIMESTAMP(6) NOT NULL,
  `Pedido_idPedido` INT NOT NULL,
  `Estado` VARCHAR(45) NOT NULL,
  `data` DATETIME(6) NOT NULL,
  `Observacoes` VARCHAR(45) NULL,
  `Doente_idDoente` INT NOT NULL,
  `idEpisodio` INT NOT NULL,
  `Relatorio` VARCHAR(250) NOT NULL,
  PRIMARY KEY (`idWorkList`),
  INDEX `fk_WorkList_Pedido1_idx` (`Pedido_idPedido` ASC),
  CONSTRAINT `fk_WorkList_Pedido1`
    FOREIGN KEY (`Pedido_idPedido`)
    REFERENCES `Exames`.`Pedido` (`idPedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `pedidos`;

DELIMITER $$

USE `pedidos`$$
DROP TRIGGER IF EXISTS `pedidos`.`insertOnWorkList` $$
USE `pedidos`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `pedidos`.`insertOnWorkList` AFTER INSERT ON  `pedido` FOR EACH ROW
BEGIN
INSERT INTO `pedidos`.`worklist`
(`idWorkList`,
`editTime`,
`Pedido_idPedido`,
`Estado`,
`data`,
`Observacoes`,
`Doente_idDoente`,
`idEpisodio`,
`Relatorio`)
VALUES
(null,
CURRENT_TIMESTAMP(6),
NEW.idPedido,
NEW.Estado,
NEW.data,
NEW.Observacoes,
NEW.Doente_idDoente,
NEW.idEpisodio,
NEW.Relatorio
);



END$$


USE `pedidos`$$
DROP TRIGGER IF EXISTS `pedidos`.`insertWorkListUpdate` $$
USE `pedidos`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `pedidos`.`insertWorkListUpdate` AFTER UPDATE ON `pedido` FOR EACH ROW
BEGIN
if(new.Estado!="Complete") then
INSERT INTO `pedidos`.`worklist`
(`idWorkList`,
`editTime`,
`Pedido_idPedido`,
`Estado`,
`data`,
`Observacoes`,
`Doente_idDoente`,
`idEpisodio`,
`Relatorio`)
VALUES
(null,
CURRENT_TIMESTAMP(6),
NEW.idPedido,
NEW.Estado,
NEW.data,
NEW.Observacoes,
NEW.Doente_idDoente,
NEW.idEpisodio,
NEW.Relatorio
);
end if;

END$$


DELIMITER ;
USE `Exames`;

DELIMITER $$

USE `Exames`$$
DROP TRIGGER IF EXISTS `Exames`.`insertWorkListUpdate` $$
USE `Exames`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `exames`.`insertWorkListUpdate` AFTER UPDATE ON `pedido` FOR EACH ROW
BEGIN
if (new.Estado="Complete") then
INSERT INTO `exames`.`worklist`
(`idWorkList`,
`editTime`,
`Pedido_idPedido`,
`Estado`,
`data`,
`Observacoes`,
`Doente_idDoente`,
`idEpisodio`,
`Relatorio`)
VALUES
(null,
CURRENT_TIMESTAMP(6),
NEW.idPedido,
NEW.Estado,
NEW.data,
NEW.Observacoes,
NEW.Doente_idDoente,
NEW.idEpisodio,
NEW.Relatorio
);
end if;

END$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
