CREATE SCHEMA `Monitoreo` ;

  CREATE TABLE `Monitoreo`.`infoserver` (
  `Ipservidor` VARCHAR(45) NULL,
  `Procesador` VARCHAR(45) NULL,
  `ProcesosCorriendo` VARCHAR(45) NULL,
  `UsuariosConectados` VARCHAR(45) NULL,
  `SO` VARCHAR(45) NULL,
  `Version_SO` VARCHAR(45) NULL,
  PRIMARY KEY (`Ipservidor`));