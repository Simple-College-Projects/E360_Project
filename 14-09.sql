/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.6.15 : Database - hotel
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`hotel` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `hotel`;

/*Table structure for table `assign` */

DROP TABLE IF EXISTS `assign`;

CREATE TABLE `assign` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL,
  `estimation` varchar(50) NOT NULL,
  `duration` varchar(50) DEFAULT NULL,
  `priority` varchar(50) NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  `start_date` date NOT NULL,
  `task_date` date DEFAULT NULL,
  PRIMARY KEY (`aid`),
  KEY `assign_ibfk_1` (`event_id`),
  KEY `assign_ibfk_2` (`task_id`),
  KEY `assign_ibfk_3` (`employee_id`),
  CONSTRAINT `assign_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`),
  CONSTRAINT `assign_ibfk_2` FOREIGN KEY (`task_id`) REFERENCES `task` (`id`),
  CONSTRAINT `assign_ibfk_3` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `assign` */

insert  into `assign`(`aid`,`event_id`,`task_id`,`employee_id`,`estimation`,`duration`,`priority`,`status`,`start_date`,`task_date`) values (1,1,1,5,'8','pending','High','new','2019-07-25','2018-09-26'),(2,1,2,6,'6','pending','Low','new','2019-06-25','2019-07-26');

/*Table structure for table `branch` */

DROP TABLE IF EXISTS `branch`;

CREATE TABLE `branch` (
  `branch_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `post` varchar(500) DEFAULT NULL,
  `landmark` varchar(50) DEFAULT NULL,
  `building` varchar(50) DEFAULT NULL,
  `pincode` bigint(10) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`branch_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `branch` */

insert  into `branch`(`branch_id`,`name`,`district`,`place`,`city`,`post`,`landmark`,`building`,`pincode`,`email`,`phone`,`created_date`,`last_updated`) values (1,'kunnamangalam Branch','Pathanamthitta','Ettumanoor North','Ettumanoor ','Ettumanoor','Near SBI Bank','Sree Muruga Building',673572,'ettumanoor@gmail.com',2,'2019-07-25 12:34:37','2019-07-26 15:07:52'),(2,'Ettumanoor Branch','Kozhikode','asd','asd','sdaa','','asd',345345,'ajay@maxlore.in',45345,'2019-07-25 12:52:50','2019-07-25 16:35:20'),(4,'westhill','Kozhikode','calicut','kkd','westhill','kjkjnkj ','abcd',673005,'addbgf@gmail.com',64465435465,'2019-07-27 11:00:27','2019-07-27 14:28:22');

/*Table structure for table `browse` */

DROP TABLE IF EXISTS `browse`;

CREATE TABLE `browse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `url` varchar(500) NOT NULL,
  `date` varchar(50) NOT NULL,
  `time` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `browse` */

insert  into `browse`(`id`,`emp_id`,`url`,`date`,`time`) values (1,5,'https://www.w3schools.com/js/','25-7-19','9.00');

/*Table structure for table `call` */

DROP TABLE IF EXISTS `call`;

CREATE TABLE `call` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) DEFAULT NULL,
  `status` varchar(40) DEFAULT NULL,
  `number` bigint(40) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `con_name` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `call` */

insert  into `call`(`id`,`emp_id`,`status`,`number`,`duration`,`con_name`) values (1,5,'incoming',9875767689,2,'anu');

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department` varchar(50) NOT NULL,
  `hotel_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hotel_id` (`hotel_id`),
  CONSTRAINT `department_ibfk_1` FOREIGN KEY (`hotel_id`) REFERENCES `hotel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`id`,`department`,`hotel_id`) values (2,'bill',1),(3,'food preparation',2),(4,'food serving',2),(5,'service',4);

/*Table structure for table `document` */

DROP TABLE IF EXISTS `document`;

CREATE TABLE `document` (
  `document_id` int(11) NOT NULL AUTO_INCREMENT,
  `document_name` varchar(50) DEFAULT NULL,
  `creator_id` int(20) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`document_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `document` */

insert  into `document`(`document_id`,`document_name`,`creator_id`,`created_date`,`last_updated`) values (1,'Adhar-card',1,'2019-07-18 00:00:00','2019-07-26 15:12:55'),(2,'Passport',1,'2019-07-26 15:13:09','2019-07-26 15:13:11'),(3,'PAN-card',1,'2019-07-26 15:13:31','2019-07-26 15:13:32'),(4,'Birth-certificate',1,'2019-07-26 15:13:56','2019-07-26 15:13:58'),(5,'Voter-ID card',1,'2019-07-26 15:14:10','2019-07-26 15:14:12'),(6,'Ration-card',1,'2019-07-26 15:14:24','2019-07-26 15:14:25'),(7,'SSLC-certificates',1,'2019-07-26 15:14:40','2019-07-26 15:14:43'),(8,'Marriage Certificate',1,'2019-07-26 15:15:05','2019-07-26 15:15:07'),(9,'Driving License',1,'2019-07-26 15:15:54','2019-07-26 15:15:57'),(10,'HSE Certificate',1,'2019-07-27 15:23:24','2019-07-27 15:23:24'),(11,'hsd',1,'2019-07-27 14:34:03','2019-07-27 14:34:03'),(12,'hgh',1,'2019-07-27 15:01:51','2019-07-27 15:01:51'),(13,'hgh',1,'2019-07-27 15:02:00','2019-07-27 15:02:00'),(14,'',1,'2019-07-27 15:42:24','2019-07-27 15:42:24'),(15,'sdfghjkl,',1,'2019-07-27 15:42:42','2019-07-27 15:42:42'),(16,'wow',1,'2019-07-27 15:42:44','2019-07-27 15:42:44'),(17,'rs',1,'2019-07-27 15:43:37','2019-07-27 15:43:37'),(18,'',1,'2019-07-27 15:44:22','2019-07-27 15:44:22'),(19,'Caste Certificate',1,'2019-07-27 15:48:20','2019-07-27 15:48:20'),(20,'Nativity Certificate',1,'2019-07-27 15:49:34','2019-07-27 15:49:34');

/*Table structure for table `employee` */

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `emp_id` int(11) NOT NULL,
  `f_name` varchar(40) NOT NULL,
  `l_name` varchar(40) DEFAULT NULL,
  `hotel_id` int(11) DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  `jop_position` varchar(40) NOT NULL,
  `work_email` varchar(40) DEFAULT NULL,
  `work_mob` bigint(11) unsigned DEFAULT NULL,
  `work_imei` bigint(11) DEFAULT NULL,
  `gender` varchar(40) DEFAULT NULL,
  `marital_status` varchar(40) DEFAULT NULL,
  `dob` varchar(20) DEFAULT NULL,
  `address` varchar(40) DEFAULT NULL,
  `pmail` varchar(40) DEFAULT NULL,
  `pmobile` bigint(40) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`emp_id`),
  KEY `hotel_id` (`hotel_id`),
  KEY `dept_id` (`dept_id`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`hotel_id`) REFERENCES `hotel` (`id`),
  CONSTRAINT `employee_ibfk_2` FOREIGN KEY (`dept_id`) REFERENCES `department` (`id`),
  CONSTRAINT `employee_ibfk_3` FOREIGN KEY (`emp_id`) REFERENCES `login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `employee` */

insert  into `employee`(`emp_id`,`f_name`,`l_name`,`hotel_id`,`dept_id`,`jop_position`,`work_email`,`work_mob`,`work_imei`,`gender`,`marital_status`,`dob`,`address`,`pmail`,`pmobile`,`image`) values (2,'aswathi','r',2,3,'Manager','sree@gmail.com',8891903124,987654321,'Female','Married','2019-07-01','kozhikode','achu@gmail',9876543211,'20190724-100027avatar3.png'),(3,'Chaithanya','diva',2,4,'Employee','ammu@gmail.com',1234098765,987654321,'Female','Unmarried','2019-07-03','kozhikode','c@gmail.com',9876543211,'20190724-100237avatar2.png'),(4,'ajay','sa',1,2,'Manager','ajay@gmail.com',1234098765,123456789123456,'Male','Married','2019-07-10','kozhikode','a@gmail.com',9876543211,'20190724-100506avatar04.png'),(5,'bivya','s',2,3,'Employee','anu@gmail.com',9747786190,9876543210,'Female','Unmarried','2019-07-16','kozhik','achussree@gmail',8891904124,'20190724-105158user2.jpg'),(6,'vish','e',2,3,'Employee','admin@maxlore.in',8891903124,987654321,'Male','Unmarried','2019-07-11','ko','c@gmail.com',9876543211,'20190724-105818avatar5.png'),(7,'bony','R',1,2,'Employee','admin@maxlore.in',8891903124,123456321456789,'Male','Married','2019-07-09','kozhi','b@gmail.com',7890654321,'20190724-120554avatar.png'),(8,'jilsina','rosh',1,2,'Employee','sree@gmail.com',9747786190,123456456789561,'Female','Unmarried','2019-07-02','kozhikode','j@gmail.com',7890654321,'20190724-121248avatar3.png'),(9,'sharon','naz',1,2,'Employee','sha@gmail.com',6788999991,567456456456456,'Male','Unmarried','2019-05-30','kozhikode','s@gmail.com',1234567890,'20190724-124013usericon.jpg'),(10,'sharon','naz',1,2,'Employee','sha@gmail',678899999,567,'Male','Unmarried','2019-05-30','kozhikode','s@gmail.com',888888888,'20190724-124326usericon.jpg'),(11,'libin','k',4,5,'Manager','li@gmail.com',9747786190,1234334,'Male','Unmarried','2019-07-11','3ededsl','l@gmail',8788,'20190724-125507avatar04.png'),(12,'libin','k',4,5,'Employee','li@gmail.com',9747786190,1234334,'Male','Unmarried','2019-07-11','3ededsl','l@gmail',8788,'20190724-125648avatar04.png'),(13,'Arun Babu','ABK',1,2,'Manager','bla@bla.bla',9869325178,321456987741852,'Female','Married','1996-01-01','Manasseri, Mukkam','abk@gmail.com',9698979593,'20190914-114542Screenshot (2).png');

/*Table structure for table `event` */

DROP TABLE IF EXISTS `event`;

CREATE TABLE `event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_name` varchar(50) NOT NULL,
  `description` varchar(200) NOT NULL,
  `event_date` varchar(100) NOT NULL,
  `event_location` varchar(100) NOT NULL,
  `client_name` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL,
  `quantity` int(11) NOT NULL,
  `manager_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `event_ibfk_1` (`manager_id`),
  CONSTRAINT `event_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `employee` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `event` */

insert  into `event`(`id`,`event_name`,`description`,`event_date`,`event_location`,`client_name`,`address`,`quantity`,`manager_id`) values (1,'marriage','yyyyyy iiii mmmm llll','2019-07-26','kozhikode','chaithnya','kozhikode',10,2);

/*Table structure for table `event_employee` */

DROP TABLE IF EXISTS `event_employee`;

CREATE TABLE `event_employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `event_employee_ibfk_1` (`event_id`),
  KEY `event_employee_ibfk_2` (`employee_id`),
  CONSTRAINT `event_employee_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`),
  CONSTRAINT `event_employee_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `event_employee` */

insert  into `event_employee`(`id`,`event_id`,`employee_id`) values (3,1,5);

/*Table structure for table `hotel` */

DROP TABLE IF EXISTS `hotel`;

CREATE TABLE `hotel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `star` varchar(50) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  `ameneties` varchar(200) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longtitude` varchar(100) DEFAULT NULL,
  `contact` bigint(100) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `hotel` */

insert  into `hotel`(`id`,`name`,`star`,`description`,`address`,`image`,`ameneties`,`latitude`,`longtitude`,`contact`,`email`,`website`) values (1,'Rahmath hotel','5','kidilan','kozhikode','20190720-104341Screenshot (4).png','1,2,3,','11.77777','9.11111',9897969594,'rahmath@gmail.com','rahmath@gmail.com'),(2,'TopForm','3','ggg','hhh','20190720-104341Screenshot (4).png','2,5,','12.777777','7.888888',8891903124,'top@maxlore.in','www.topform.com'),(4,'TopForm','3','ggg','hhh','20190720-104341Screenshot (4).png','2,3,','12.777777','7.888888',8891903124,'admin@maxlore.in','www.topform.com'),(5,'Devika','2','Nice','Kizhur','20190914-095744Screenshot (3).png','5,','12.25.365','125.25.123',9638527410,'asdfghj@gmail.com','asdfghj'),(6,'NewHotel','2','Nice','Kizhur','20190914-100643Screenshot (2).png','6,','1.1.1.1','2.2.2.2',1234567890,'jdfghkdj@jhgkdjfhg.gvjd','gdfkjjkg');

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) DEFAULT NULL,
  `longititude` varchar(45) DEFAULT NULL,
  `latitude` varchar(45) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `locality` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `emp_id` (`emp_id`),
  CONSTRAINT `location_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employee` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `location` */

insert  into `location`(`id`,`emp_id`,`longititude`,`latitude`,`place`,`locality`) values (1,5,'25.456','72.256','chevayur','kozhikode');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values (1,'admin','admin','admin'),(2,'aswathi','qq','Manager'),(3,'chai','cc','Employee'),(4,'ajay','aa','Manager'),(5,'bivya','bb','Employee'),(6,'vi','vv','Employee'),(7,'vi','vv','Employee'),(8,'vi','vv','Employee'),(9,'sha','sa','Employee'),(10,'sharon','sharon','Employee'),(11,'libi','lll','Manager'),(12,'libi','lk','Employee'),(13,'Arun Blabu','123456','Manager');

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `empid` int(11) NOT NULL,
  `status` varchar(40) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `empid` (`empid`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`empid`) REFERENCES `employee` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `message` */

insert  into `message`(`id`,`empid`,`status`,`number`,`name`,`message`) values (1,5,'incoming',334566,'aswathi','haii');

/*Table structure for table `task` */

DROP TABLE IF EXISTS `task`;

CREATE TABLE `task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `task` varchar(50) NOT NULL,
  `description` varchar(500) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `task_ibfk_1` (`event_id`),
  CONSTRAINT `task_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `task` */

insert  into `task`(`id`,`event_id`,`task`,`description`) values (1,1,'decoration stage','hgfdchjkmnbv'),(2,1,'seating','luyutfgnm ');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
