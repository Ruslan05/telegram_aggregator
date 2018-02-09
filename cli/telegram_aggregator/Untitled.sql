-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: aggregator
-- ------------------------------------------------------
-- Server version	5.5.5-10.2.11-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `channel`
--

DROP TABLE IF EXISTS `channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `channel` (
  `id_channel` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `shared_url` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_channel`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channel`
--

LOCK TABLES `channel` WRITE;
/*!40000 ALTER TABLE `channel` DISABLE KEYS */;
INSERT INTO `channel` VALUES (2,'@architecture_stories','https://t.me/architecture_stories');
/*!40000 ALTER TABLE `channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post_exucuted`
--

DROP TABLE IF EXISTS `post_exucuted`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post_exucuted` (
  `id_post_exucuted` int(11) NOT NULL,
  `id_public` int(11) DEFAULT NULL,
  `id_channel` int(11) DEFAULT NULL,
  `post_date` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_post_exucuted`),
  KEY `id_publiic_idx` (`id_public`),
  KEY `id_channel_idx` (`id_channel`),
  CONSTRAINT `id_channel` FOREIGN KEY (`id_channel`) REFERENCES `channel` (`id_channel`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `id_publiic` FOREIGN KEY (`id_public`) REFERENCES `public` (`id_public`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_exucuted`
--

LOCK TABLES `post_exucuted` WRITE;
/*!40000 ALTER TABLE `post_exucuted` DISABLE KEYS */;
/*!40000 ALTER TABLE `post_exucuted` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `public`
--

DROP TABLE IF EXISTS `public`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `public` (
  `id_public` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `owner_id` varchar(255) DEFAULT NULL,
  `id_public_data` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_public`),
  KEY `t_idx` (`id_public_data`),
  CONSTRAINT `id_public_data` FOREIGN KEY (`id_public_data`) REFERENCES `public_data` (`id_public_data`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `public`
--

LOCK TABLES `public` WRITE;
/*!40000 ALTER TABLE `public` DISABLE KEYS */;
INSERT INTO `public` VALUES (2,'Архитектор','Онлайн чат архитекторов. Живое общение и помощь в обучении!\n','https://vk.com/iamarchitect','-98559377',1);
/*!40000 ALTER TABLE `public` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `public_channel`
--

DROP TABLE IF EXISTS `public_channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `public_channel` (
  `id_public_channel` int(11) NOT NULL AUTO_INCREMENT,
  `id_public` int(11) DEFAULT NULL,
  `id_channel` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_public_channel`),
  KEY `id_public_idx` (`id_public`),
  KEY `id_channel_idx` (`id_channel`),
  CONSTRAINT `id_channel_` FOREIGN KEY (`id_channel`) REFERENCES `channel` (`id_channel`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `id_public` FOREIGN KEY (`id_public`) REFERENCES `public` (`id_public`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `public_channel`
--

LOCK TABLES `public_channel` WRITE;
/*!40000 ALTER TABLE `public_channel` DISABLE KEYS */;
/*!40000 ALTER TABLE `public_channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `public_data`
--

DROP TABLE IF EXISTS `public_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `public_data` (
  `id_public_data` int(11) NOT NULL AUTO_INCREMENT,
  `post_text` varchar(255) DEFAULT NULL,
  `picture` varchar(255) DEFAULT NULL,
  `video` varchar(255) DEFAULT NULL,
  `post_file` varchar(255) DEFAULT NULL,
  `music` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_public_data`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `public_data`
--

LOCK TABLES `public_data` WRITE;
/*!40000 ALTER TABLE `public_data` DISABLE KEYS */;
INSERT INTO `public_data` VALUES (1,'[\'response\'][\'wall\'][1][\'text\']','[\'response\'][\'wall\'][1][\'attachment\'][\'photo\'][\'src_big\']',NULL,NULL,NULL);
/*!40000 ALTER TABLE `public_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-09 22:53:52
