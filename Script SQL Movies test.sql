CREATE TABLE `Client` (
`id_cl` INT(150) PRIMARY KEY,
`nom_c` TEXT(150),
`prenom_c` TEXT(150),
`tel` DECIMAL(20),
`adresse` VARCHAR(150),
`adhesion` BOOLEAN,
`mail` VARCHAR(150)
);


CREATE TABLE `Realisateurs` (
`id_rea` VARCHAR(150) PRIMARY KEY,
`nom_r` TEXT(150),
`prenom_r` TEXT(150)
);


CREATE TABLE `Films` (
`id_f` VARCHAR(150) PRIMARY KEY,
`titre` INT(150),
`categorie` INT(150),
`id_rmk` VARCHAR(150),
`langue` INT(150)
);


CREATE TABLE `Acteurs` (
`id_a` VARCHAR(150) PRIMARY KEY,
`stage_name` TEXT(150),
`birth_name` TEXT(150)
);


CREATE TABLE `Studios` (
`id_stu` VARCHAR(150) PRIMARY KEY,
`nom_s` TEXT(150),
`dates_stu` DECIMAL(65),
`loc_stu` TEXT(150)
)


