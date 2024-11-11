-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: emumba_qor
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Geometric_Analysis_Stats`
--

DROP TABLE IF EXISTS `Geometric_Analysis_Stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Geometric_Analysis_Stats` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Stat_Name` varchar(50) DEFAULT NULL,
  `Stat_Value` varchar(50) DEFAULT NULL,
  `UniqueKey` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_Geo` (`UniqueKey`),
  CONSTRAINT `fk_Geo` FOREIGN KEY (`UniqueKey`) REFERENCES `MetaData` (`UniqueKey`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Geometric_Analysis_Stats`
--

LOCK TABLES `Geometric_Analysis_Stats` WRITE;
/*!40000 ALTER TABLE `Geometric_Analysis_Stats` DISABLE KEYS */;
INSERT INTO `Geometric_Analysis_Stats` VALUES (1,'high_curvature_internal_checking_count','0',1),(2,'high_curvature_internal_checking_max_value','0.0',1),(3,'high_curvature_internal_checking_min_value','0.0',1),(4,'high_curvature_internal_checking_marker_x','0',1),(5,'high_curvature_internal_checking_marker_y','0',1),(6,'high_curvature_external_checking_count','0',1),(7,'high_curvature_external_checking_max_value','0.0',1),(8,'high_curvature_external_checking_min_value','0.0',1),(9,'high_curvature_external_checking_marker_x','0',1),(10,'high_curvature_external_checking_marker_y','0',1),(11,'mrc_area_count','0',1),(12,'mrc_area_max_value','0.0',1),(13,'mrc_area_min_value','0.0',1),(14,'mrc_area_marker_x','0',1),(15,'mrc_area_marker_y','0',1),(16,'imrcfix_max_correction_max_value','None',1),(17,'imrcfix_the_worst_width_error_overall_max_value','None',1),(18,'imrcfix_the_worst_spacing_error_overall_max_value','None',1),(19,'high_curvature_internal_checking_setting','7',1),(20,'high_curvature_external_checking_setting','7',1),(21,'mrc_area_setting','520',1),(22,'mrc_spacing_setting','13.0',1),(23,'mrc_width_setting','13.0',1),(24,'mrc_width_count','0',1),(25,'mrc_width_max_value','0.0',1),(26,'mrc_width_min_value','0.0',1),(27,'mrc_width_marker_x','0',1),(28,'mrc_width_marker_y','0',1),(29,'mrc_spacing_count','0',1),(30,'mrc_spacing_max_value','0.0',1),(31,'mrc_spacing_min_value','0.0',1),(32,'mrc_spacing_marker_x','0',1),(33,'mrc_spacing_marker_y','0',1),(34,'high_curvature_internal_checking_count','0',2),(35,'high_curvature_internal_checking_max_value','0.0',2),(36,'high_curvature_internal_checking_min_value','0.0',2),(37,'high_curvature_internal_checking_marker_x','0',2),(38,'high_curvature_internal_checking_marker_y','0',2),(39,'high_curvature_external_checking_count','0',2),(40,'high_curvature_external_checking_max_value','0.0',2),(41,'high_curvature_external_checking_min_value','0.0',2),(42,'high_curvature_external_checking_marker_x','0',2),(43,'high_curvature_external_checking_marker_y','0',2),(44,'mrc_area_count','0',2),(45,'mrc_area_max_value','0.0',2),(46,'mrc_area_min_value','0.0',2),(47,'mrc_area_marker_x','0',2),(48,'mrc_area_marker_y','0',2),(49,'imrcfix_max_correction_max_value','None',2),(50,'imrcfix_the_worst_width_error_overall_max_value','None',2),(51,'imrcfix_the_worst_spacing_error_overall_max_value','None',2),(52,'high_curvature_internal_checking_setting','7',2),(53,'high_curvature_external_checking_setting','7',2),(54,'mrc_area_setting','520',2),(55,'mrc_spacing_setting','13.0',2),(56,'mrc_width_setting','13.0',2),(57,'mrc_width_count','0',2),(58,'mrc_width_max_value','0.0',2),(59,'mrc_width_min_value','0.0',2),(60,'mrc_width_marker_x','0',2),(61,'mrc_width_marker_y','0',2),(62,'mrc_spacing_count','0',2),(63,'mrc_spacing_max_value','0.0',2),(64,'mrc_spacing_min_value','0.0',2),(65,'mrc_spacing_marker_x','0',2),(66,'mrc_spacing_marker_y','0',2);
/*!40000 ALTER TABLE `Geometric_Analysis_Stats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Main_Stats`
--

DROP TABLE IF EXISTS `Main_Stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Main_Stats` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Stat_Name` varchar(50) DEFAULT NULL,
  `Stat_Value` varchar(50) DEFAULT NULL,
  `UniqueKey` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_UniqueKey` (`UniqueKey`),
  CONSTRAINT `fk_UniqueKey` FOREIGN KEY (`UniqueKey`) REFERENCES `MetaData` (`UniqueKey`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Main_Stats`
--

LOCK TABLES `Main_Stats` WRITE;
/*!40000 ALTER TABLE `Main_Stats` DISABLE KEYS */;
INSERT INTO `Main_Stats` VALUES (1,'fermi_job_name','v7bgciso',1),(2,'revision_branch','feature/fermi/qtm3split',1),(3,'revision_date','2023-08-14',1),(4,'fermi_id','9871',1),(5,'gpu','4',1),(6,'expect_run_time_50_gpu','720.15',1),(7,'expect_run_time_1_gpu','34500.25',1),(8,'user','exampleuser',1),(9,'name','exampleDesign01',1),(10,'max_err_per_partion','None',1),(11,'total_errors','None',1),(12,'partition','36',1),(13,'grid','8',1),(14,'optimizer_iterations','None',1),(15,'force_flag','False',1),(16,'force_screenshot','False',1),(17,'mpi_retry_count','None',1),(18,'num_qtm3_iterations','None',1),(19,'num_qtm4_iterations','None',1),(20,'num_qtm5_iterations','None',1),(21,'mask_num_deleted_shapes','None',1),(22,'mask_num_upsized_shapes','None',1),(23,'num_pixel_corrections','None',1),(24,'num_part_corrections','None',1),(25,'delete_mask_polygon_count','None',1),(26,'delete_mask_polygon_max','None',1),(27,'delete_mask_polygon_min','None',1),(28,'upsizing_mask_polygon_count','None',1),(29,'upsizing_mask_polygon_max','None',1),(30,'upsizing_mask_polygon_min','None',1),(31,'number_of_optimized_partitions','1024',1),(32,'total_number_of_partitions','1024',1),(33,'parsing_time','False',1),(34,'design_size','0.85785',1),(35,'mask_file_size','2258.88',1),(36,'machine_name','cdp51',1),(37,'run_date_time','2024-08-01',1),(38,'fermi_job_name','a7bcdfeg',2),(39,'revision_branch','feature/fermi/qtm3split',2),(40,'revision_date','2023-08-14',2),(41,'fermi_id','9872',2),(42,'gpu','4',2),(43,'expect_run_time_50_gpu','720.15',2),(44,'expect_run_time_1_gpu','34500.25',2),(45,'user','exampleuser',2),(46,'name','exampleDesign01',2),(47,'max_err_per_partion','None',2),(48,'total_errors','None',2),(49,'partition','36',2),(50,'grid','8',2),(51,'optimizer_iterations','None',2),(52,'force_flag','False',2),(53,'force_screenshot','False',2),(54,'mpi_retry_count','None',2),(55,'num_qtm3_iterations','None',2),(56,'num_qtm4_iterations','None',2),(57,'num_qtm5_iterations','None',2),(58,'mask_num_deleted_shapes','None',2),(59,'mask_num_upsized_shapes','None',2),(60,'num_pixel_corrections','None',2),(61,'num_part_corrections','None',2),(62,'delete_mask_polygon_count','None',2),(63,'delete_mask_polygon_max','None',2),(64,'delete_mask_polygon_min','None',2),(65,'upsizing_mask_polygon_count','None',2),(66,'upsizing_mask_polygon_max','None',2),(67,'upsizing_mask_polygon_min','None',2),(68,'number_of_optimized_partitions','1024',2),(69,'total_number_of_partitions','1024',2),(70,'parsing_time','False',2),(71,'design_size','0.85785',2),(72,'mask_file_size','2258.88',2),(73,'machine_name','cdp28',2),(74,'run_date_time','2024-08-01',2);
/*!40000 ALTER TABLE `Main_Stats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MetaData`
--

DROP TABLE IF EXISTS `MetaData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MetaData` (
  `Fermi_ID` int DEFAULT NULL,
  `Fermi_Name` varchar(150) DEFAULT NULL,
  `Revision_Commit` varchar(150) DEFAULT NULL,
  `UniqueKey` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`UniqueKey`),
  UNIQUE KEY `UniqueKey` (`UniqueKey`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MetaData`
--

LOCK TABLES `MetaData` WRITE;
/*!40000 ALTER TABLE `MetaData` DISABLE KEYS */;
INSERT INTO `MetaData` VALUES (9871,'v7bgciso','heads/feature/fermi/qtm3split-0-g44d2dea0a4a315e3e685475f7dc4288ee37d4155',1),(9872,'a7bcdfeg','heads/feature/fermi2/dqtm3split-0-g44d2dea0a4a315e3e685475f7dc4288ee37d4155',2);
/*!40000 ALTER TABLE `MetaData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Runtime_Analysis_Stats`
--

DROP TABLE IF EXISTS `Runtime_Analysis_Stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Runtime_Analysis_Stats` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Stat_Name` varchar(50) DEFAULT NULL,
  `Stat_Value` varchar(50) DEFAULT NULL,
  `UniqueKey` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_Runtime` (`UniqueKey`),
  CONSTRAINT `fk_Runtime` FOREIGN KEY (`UniqueKey`) REFERENCES `MetaData` (`UniqueKey`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Runtime_Analysis_Stats`
--

LOCK TABLES `Runtime_Analysis_Stats` WRITE;
/*!40000 ALTER TABLE `Runtime_Analysis_Stats` DISABLE KEYS */;
INSERT INTO `Runtime_Analysis_Stats` VALUES (1,'target_prep_runtime','420.75',1),(2,'ctm_fg','830.40',1),(3,'qtm_fg','3960.60',1),(4,'ctm_prep','2300.25',1),(5,'qtm0_prep','880.00',1),(6,'qtm1_prep','1070.50',1),(7,'qtm2_prep','1150.60',1),(8,'qtm3_prep','630.75',1),(9,'qtm4_prep','0',1),(10,'qtm5_prep','0',1),(11,'qtm0_total','1300.00',1),(12,'qtm1_total','1650.75',1),(13,'qtm2_total','2000.90',1),(14,'qtm3_total','4550.00',1),(15,'qtm4_total','0',1),(16,'qtm5_total','0',1),(17,'ctm_exec_time','3200.00',1),(18,'qtm_exec_time','11200.00',1),(19,'postprocess_exec_time','1400.00',1),(20,'total_fermi_runtime','16200.00',1),(21,'the_checker_runtime','None',1),(22,'target_prep_runtime','420.75',2),(23,'ctm_fg','830.40',2),(24,'qtm_fg','3960.60',2),(25,'ctm_prep','2300.25',2),(26,'qtm0_prep','880.00',2),(27,'qtm1_prep','1070.50',2),(28,'qtm2_prep','1150.60',2),(29,'qtm3_prep','630.75',2),(30,'qtm4_prep','0',2),(31,'qtm5_prep','0',2),(32,'qtm0_total','1300.00',2),(33,'qtm1_total','1650.75',2),(34,'qtm2_total','2000.90',2),(35,'qtm3_total','4550.00',2),(36,'qtm4_total','0',2),(37,'qtm5_total','0',2),(38,'ctm_exec_time','3200.00',2),(39,'qtm_exec_time','11200.00',2),(40,'postprocess_exec_time','1400.00',2),(41,'total_fermi_runtime','16200.00',2),(42,'the_checker_runtime','None',2);
/*!40000 ALTER TABLE `Runtime_Analysis_Stats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negdose`
--

DROP TABLE IF EXISTS `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negdose`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negdose` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Stat_Name` varchar(50) DEFAULT NULL,
  `Stat_Value` varchar(50) DEFAULT NULL,
  `UniqueKey` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_Negdose` (`UniqueKey`),
  CONSTRAINT `fk_Negdose` FOREIGN KEY (`UniqueKey`) REFERENCES `MetaData` (`UniqueKey`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negdose`
--

LOCK TABLES `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negdose` WRITE;
/*!40000 ALTER TABLE `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negdose` DISABLE KEYS */;
INSERT INTO `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negdose` VALUES (1,'mean_fermi','-1.15',1),(2,'std_fermi','0.51',1),(3,'max_fermi','3.80',1),(4,'count_fermi','30000',1),(5,'marker_x_fermi','828000.0',1),(6,'marker_y_fermi','36000.0',1),(7,'mean_fermi','-1.15',2),(8,'std_fermi','0.51',2),(9,'max_fermi','3.80',2),(10,'count_fermi','30000',2),(11,'marker_x_fermi','828000.0',2),(12,'marker_y_fermi','36000.0',2);
/*!40000 ALTER TABLE `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negdose` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negfocus`
--

DROP TABLE IF EXISTS `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negfocus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negfocus` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Stat_Name` varchar(50) DEFAULT NULL,
  `Stat_Value` varchar(50) DEFAULT NULL,
  `UniqueKey` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_Negfocus` (`UniqueKey`),
  CONSTRAINT `fk_Negfocus` FOREIGN KEY (`UniqueKey`) REFERENCES `MetaData` (`UniqueKey`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negfocus`
--

LOCK TABLES `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negfocus` WRITE;
/*!40000 ALTER TABLE `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negfocus` DISABLE KEYS */;
INSERT INTO `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negfocus` VALUES (1,'mean_fermi','-1.15',1),(2,'std_fermi','0.51',1),(3,'max_fermi','3.80',1),(4,'count_fermi','30000',1),(5,'marker_x_fermi','828000.0',1),(6,'marker_y_fermi','36000.0',1),(7,'mean_fermi','-1.15',2),(8,'std_fermi','0.51',2),(9,'max_fermi','3.80',2),(10,'count_fermi','30000',2),(11,'marker_x_fermi','828000.0',2),(12,'marker_y_fermi','36000.0',2);
/*!40000 ALTER TABLE `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negfocus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posdose`
--

DROP TABLE IF EXISTS `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posdose`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posdose` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Stat_Name` varchar(50) DEFAULT NULL,
  `Stat_Value` varchar(50) DEFAULT NULL,
  `UniqueKey` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_Posdose` (`UniqueKey`),
  CONSTRAINT `fk_Posdose` FOREIGN KEY (`UniqueKey`) REFERENCES `MetaData` (`UniqueKey`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posdose`
--

LOCK TABLES `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posdose` WRITE;
/*!40000 ALTER TABLE `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posdose` DISABLE KEYS */;
INSERT INTO `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posdose` VALUES (1,'mean_fermi','-1.15',1),(2,'std_fermi','0.51',1),(3,'max_fermi','3.80',1),(4,'count_fermi','30000',1),(5,'marker_x_fermi','828000.0',1),(6,'marker_y_fermi','36000.0',1),(7,'mean_fermi','-1.15',2),(8,'std_fermi','0.51',2),(9,'max_fermi','3.80',2),(10,'count_fermi','30000',2),(11,'marker_x_fermi','828000.0',2),(12,'marker_y_fermi','36000.0',2);
/*!40000 ALTER TABLE `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posdose` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posfocus`
--

DROP TABLE IF EXISTS `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posfocus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posfocus` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Stat_Name` varchar(50) DEFAULT NULL,
  `Stat_Value` varchar(50) DEFAULT NULL,
  `UniqueKey` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_Posfocus` (`UniqueKey`),
  CONSTRAINT `fk_Posfocus` FOREIGN KEY (`UniqueKey`) REFERENCES `MetaData` (`UniqueKey`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posfocus`
--

LOCK TABLES `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posfocus` WRITE;
/*!40000 ALTER TABLE `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posfocus` DISABLE KEYS */;
INSERT INTO `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posfocus` VALUES (1,'mean_fermi','-1.15',1),(2,'std_fermi','0.51',1),(3,'max_fermi','3.80',1),(4,'count_fermi','30000',1),(5,'marker_x_fermi','828000.0',1),(6,'marker_y_fermi','36000.0',1),(7,'mean_fermi','-1.15',2),(8,'std_fermi','0.51',2),(9,'max_fermi','3.80',2),(10,'count_fermi','30000',2),(11,'marker_x_fermi','828000.0',2),(12,'marker_y_fermi','36000.0',2);
/*!40000 ALTER TABLE `Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posfocus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Statistical_Analysis_EPE_Target_vs_Nominal_Mask_Simulation_f0d0`
--

DROP TABLE IF EXISTS `Statistical_Analysis_EPE_Target_vs_Nominal_Mask_Simulation_f0d0`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Statistical_Analysis_EPE_Target_vs_Nominal_Mask_Simulation_f0d0` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Stat_Name` varchar(50) DEFAULT NULL,
  `Stat_Value` varchar(50) DEFAULT NULL,
  `UniqueKey` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_f0d0` (`UniqueKey`),
  CONSTRAINT `fk_f0d0` FOREIGN KEY (`UniqueKey`) REFERENCES `MetaData` (`UniqueKey`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Statistical_Analysis_EPE_Target_vs_Nominal_Mask_Simulation_f0d0`
--

LOCK TABLES `Statistical_Analysis_EPE_Target_vs_Nominal_Mask_Simulation_f0d0` WRITE;
/*!40000 ALTER TABLE `Statistical_Analysis_EPE_Target_vs_Nominal_Mask_Simulation_f0d0` DISABLE KEYS */;
INSERT INTO `Statistical_Analysis_EPE_Target_vs_Nominal_Mask_Simulation_f0d0` VALUES (1,'mean_fermi','-1.15',1),(2,'std_fermi','0.51',1),(3,'max_fermi','3.80',1),(4,'count_fermi','30000',1),(5,'marker_x_fermi','828000.0',1),(6,'marker_y_fermi','36000.0',1),(7,'mean_fermi','-1.15',2),(8,'std_fermi','0.51',2),(9,'max_fermi','3.80',2),(10,'count_fermi','30000',2),(11,'marker_x_fermi','828000.0',2),(12,'marker_y_fermi','36000.0',2);
/*!40000 ALTER TABLE `Statistical_Analysis_EPE_Target_vs_Nominal_Mask_Simulation_f0d0` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Statistical_Analysis_Width_of_PV_Band_by_Dose`
--

DROP TABLE IF EXISTS `Statistical_Analysis_Width_of_PV_Band_by_Dose`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Statistical_Analysis_Width_of_PV_Band_by_Dose` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Stat_Name` varchar(50) DEFAULT NULL,
  `Stat_Value` varchar(50) DEFAULT NULL,
  `UniqueKey` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_dose` (`UniqueKey`),
  CONSTRAINT `fk_dose` FOREIGN KEY (`UniqueKey`) REFERENCES `MetaData` (`UniqueKey`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Statistical_Analysis_Width_of_PV_Band_by_Dose`
--

LOCK TABLES `Statistical_Analysis_Width_of_PV_Band_by_Dose` WRITE;
/*!40000 ALTER TABLE `Statistical_Analysis_Width_of_PV_Band_by_Dose` DISABLE KEYS */;
INSERT INTO `Statistical_Analysis_Width_of_PV_Band_by_Dose` VALUES (1,'mean_fermi','-1.15',1),(2,'std_fermi','0.51',1),(3,'max_fermi','3.80',1),(4,'count_fermi','30000',1),(5,'marker_x_fermi','828000.0',1),(6,'marker_y_fermi','36000.0',1),(7,'mean_fermi','-1.15',2),(8,'std_fermi','0.51',2),(9,'max_fermi','3.80',2),(10,'count_fermi','30000',2),(11,'marker_x_fermi','828000.0',2),(12,'marker_y_fermi','36000.0',2);
/*!40000 ALTER TABLE `Statistical_Analysis_Width_of_PV_Band_by_Dose` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Statistical_Analysis_Width_of_PV_Band_by_Focus`
--

DROP TABLE IF EXISTS `Statistical_Analysis_Width_of_PV_Band_by_Focus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Statistical_Analysis_Width_of_PV_Band_by_Focus` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Stat_Name` varchar(50) DEFAULT NULL,
  `Stat_Value` varchar(50) DEFAULT NULL,
  `UniqueKey` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_focus` (`UniqueKey`),
  CONSTRAINT `fk_focus` FOREIGN KEY (`UniqueKey`) REFERENCES `MetaData` (`UniqueKey`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Statistical_Analysis_Width_of_PV_Band_by_Focus`
--

LOCK TABLES `Statistical_Analysis_Width_of_PV_Band_by_Focus` WRITE;
/*!40000 ALTER TABLE `Statistical_Analysis_Width_of_PV_Band_by_Focus` DISABLE KEYS */;
INSERT INTO `Statistical_Analysis_Width_of_PV_Band_by_Focus` VALUES (1,'mean_fermi','-1.15',1),(2,'std_fermi','0.51',1),(3,'max_fermi','3.80',1),(4,'count_fermi','30000',1),(5,'marker_x_fermi','828000.0',1),(6,'marker_y_fermi','36000.0',1),(7,'mean_fermi','-1.15',2),(8,'std_fermi','0.51',2),(9,'max_fermi','3.80',2),(10,'count_fermi','30000',2),(11,'marker_x_fermi','828000.0',2),(12,'marker_y_fermi','36000.0',2);
/*!40000 ALTER TABLE `Statistical_Analysis_Width_of_PV_Band_by_Focus` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-11 14:03:10
