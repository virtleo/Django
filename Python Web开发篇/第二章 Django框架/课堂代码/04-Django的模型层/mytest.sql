/*
SQLyog Community v13.1.1 (32 bit)
MySQL - 5.7.29 : Database - mytest
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`mytest` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `mytest`;

/*Table structure for table `myapp_users` */

DROP TABLE IF EXISTS `myapp_users`;

CREATE TABLE `myapp_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` int(11) NOT NULL,
  `phone` varchar(16) NOT NULL,
  `addtime` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

/*Data for the table `myapp_users` */

insert  into `myapp_users`(`id`,`name`,`age`,`phone`,`addtime`) values 
(1,'张三',20,'123456789','2020-07-04 18:59:12.621925'),
(2,'李四',22,'1234234523','2020-07-04 19:00:17.961644'),
(3,'王五',19,'3452345','2020-07-04 19:00:43.928743'),
(5,'qq',21,'1234567654','2020-07-04 19:00:47.292401'),
(7,'小刘',26,'2345654','2020-07-04 19:00:48.002413'),
(8,'赵柳2',25,'666888','2020-07-04 20:09:54.233059');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
