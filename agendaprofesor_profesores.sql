-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: agendaprofesor
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `profesores`
--

DROP TABLE IF EXISTS `profesores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profesores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `telefono` varchar(50) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `contrasena` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profesores`
--

LOCK TABLES `profesores` WRITE;
/*!40000 ALTER TABLE `profesores` DISABLE KEYS */;
INSERT INTO `profesores` VALUES (1,'Joan','01','correo_prueba@gmail.com','1'),(2,'Joan','02','correo_prueba@gmail.com','2'),(3,'Joan','03','correo_prueba@gmail.com','3'),(4,'Joan','04','correo_prueba@gmail.com','4'),(5,'Joan','04','correo_prueba@gmail.com','4'),(6,'Joan','05','correo_prueba@gmail.com','5'),(7,'Joan','05','correo_prueba@gmail.com','5'),(8,'Joan','001','correo_pruewba@gmail.com','123'),(9,'milena','1234567','milena@gmail.com','123456789'),(10,'Universidad Tecnológica','31500234','UniversidadTecnologica@gmail.com','Universidad Tecnológica'),(11,'Joan','002','Universidad1111Tecnologica@gmail.com','99438439'),(12,'COLOMBIA','000000000000004','COLOMBIA@GMAIL.COM','000000000000000000000000004'),(13,'COLOMBIA','00000000000004','COLOMBIA@GMAIL.COM','00000000000000004'),(14,'a','a','correo_prueba@gmail.com','a'),(15,'Elian','0987654321','pou@gmail.com','0987654321'),(16,'Elian','0987654321','pou@gmail.com','0987654321'),(17,'k','222','correo_prueba@gmail.com','222'),(18,'k','222','correo_prueba@gmail.com','222'),(19,'ppppp','1212','correo_prueba@gmail.com','ewewf'),(20,'Elian','2121','elianff@gmail.com','001'),(21,'Pedro','99991','pedro@gmail.com','0000000000000000000000'),(22,'pepe','000001','pepe@gmail.com','0909090909'),(23,'AAAAAAAAAAAAA','AAAAAAAAAAAA','correo_prueba@gmail.com','AAAAAAAAAAAAAAAAAAAAAAAAAA'),(24,'pepe','000001','pepe@gmail.com','0909090909'),(25,'Jaime ','099090909','jaime@gmail.com','POP'),(26,'Jaime ','099090909','jaime@gmail.com','POP'),(27,'Marco','0987654321','marco@gmail.com','98');
/*!40000 ALTER TABLE `profesores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-23 15:16:23
