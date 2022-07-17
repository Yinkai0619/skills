-- MySQL dump 10.19  Distrib 10.3.29-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: 172.27.0.1    Database: test
-- ------------------------------------------------------
-- Server version	10.6.5-MariaDB-1:10.6.5+maria~focal

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `test`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `test` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `test`;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `dept_no` varchar(4) NOT NULL,
  `dept_name` varchar(40) NOT NULL,
  PRIMARY KEY (`dept_no`),
  UNIQUE KEY `dept_name` (`dept_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES ('d009','Customer Service'),('d005','Development'),('d002','Finance'),('d003','Human Resources'),('d001','Marketing'),('d004','Production'),('d006','Quality Management'),('d008','Research'),('d007','Sales');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dept_emp`
--

DROP TABLE IF EXISTS `dept_emp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dept_emp` (
  `emp_no` int(11) NOT NULL,
  `dept_no` varchar(4) NOT NULL,
  `from_date` date NOT NULL,
  `to_date` date NOT NULL,
  PRIMARY KEY (`emp_no`,`dept_no`),
  KEY `dept_no` (`dept_no`),
  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) REFERENCES `employees` (`emp_no`),
  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) REFERENCES `department` (`dept_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dept_emp`
--

LOCK TABLES `dept_emp` WRITE;
/*!40000 ALTER TABLE `dept_emp` DISABLE KEYS */;
INSERT INTO `dept_emp` VALUES (1,'d005','1986-06-26','9999-01-01'),(2,'d007','1996-08-03','9999-01-01'),(3,'d004','1995-12-03','9999-01-01'),(4,'d004','1986-12-01','9999-01-01'),(5,'d003','1989-09-12','9999-01-01'),(6,'d005','1990-08-05','9999-01-01'),(7,'d008','1989-02-10','9999-01-01'),(8,'d005','1998-03-11','2000-07-31'),(9,'d006','1985-02-18','9999-01-01'),(10,'d004','1996-11-24','2000-06-26'),(10,'d006','2000-06-26','9999-01-01'),(11,'d009','1990-01-22','1996-11-09'),(12,'d005','1992-12-18','9999-01-01'),(13,'d003','1985-10-20','9999-01-01'),(14,'d005','1993-12-29','9999-01-01'),(15,'d008','1992-09-19','1993-08-22'),(16,'d007','1998-02-11','9999-01-01'),(17,'d001','1993-08-03','9999-01-01'),(18,'d004','1992-07-29','9999-01-01'),(18,'d005','1987-04-03','1992-07-29'),(19,'d008','1999-04-30','9999-01-01'),(20,'d004','1997-12-30','9999-01-01');
/*!40000 ALTER TABLE `dept_emp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employees` (
  `emp_no` int(11) NOT NULL AUTO_INCREMENT,
  `birth_date` date DEFAULT NULL,
  `first_name` varchar(14) NOT NULL,
  `last_name` varchar(16) NOT NULL,
  `gender` enum('M','F') DEFAULT NULL,
  `hire_date` date DEFAULT NULL,
  PRIMARY KEY (`emp_no`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'1985-06-19','Li','Yinkai','M','2015-03-16'),(2,'1989-12-14','Bai','Na','F','2014-08-15'),(3,'1993-03-16','Jin','Xue','M','2017-05-16'),(4,'1979-10-16','Huang','Yao','F','2014-05-16'),(5,'1985-04-02','User','5','F','2014-04-11'),(6,'1986-09-14','User','6','F','2008-07-04'),(7,'1986-05-14','User','7','F','2004-06-25'),(8,'1990-09-13','User','8','M','2000-02-13'),(9,'1990-02-26','User','9','M','2020-10-17'),(10,'1981-07-06','User','10','M','2013-04-12'),(11,'1983-05-08','User','11','M','2014-11-13'),(12,'1993-10-01','User','12','F','2011-02-24'),(13,'1993-01-22','User','13','F','2019-04-01'),(14,'1981-05-10','User','14','M','2000-07-11'),(15,'1986-06-13','User','15','F','2020-12-20'),(16,'1985-03-13','User','16','F','2003-04-01'),(17,'1986-12-10','User','17','F','2002-06-04'),(18,'1982-08-22','User','18','F','2008-10-28'),(19,'1986-11-15','User','19','M','2004-03-24'),(20,'1986-02-01','User','20','M','2020-05-08');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(48) NOT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'Yinkai',36),(2,'Nana',31),(3,'tom',40),(8,'tom',40),(9,'tom',40);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` smallint(6) NOT NULL AUTO_INCREMENT,
  `login_name` varchar(16) NOT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `gender` enum('M','F') NOT NULL,
  `age` int(11) DEFAULT NULL,
  `phone` char(11) DEFAULT NULL,
  `password` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login_name` (`login_name`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'U1','User','1','M',38,'13856532128','K4SU7F8L'),(2,'U2','User','2','F',42,'13838012341','FxfWZMR6'),(3,'U3','User','3','F',25,'13438553314','XMidpcIl'),(4,'U4','User','4','M',33,'13461951183','NEYmv59c'),(5,'U5','User','5','M',40,'13782241750','c44AYAFw'),(6,'U6','User','6','M',38,'13760783651','wSEUPtNL'),(7,'U7','User','7','M',33,'13742279193','DPrKvnWZ'),(8,'U8','User','8','F',28,'13949005481','W0fwfn7F'),(9,'U9','User','9','M',43,'13932925328','yW0AGRi6'),(19,'yinkai','Li','Yinkai','M',36,'13734696953','N5WK78Ve'),(20,'nana','Bai','Na','F',32,'13590155497','vSoqDhpk');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-07 23:10:38
