---- drop ----
DROP TABLE IF EXISTS `buyma`;

---- create ----
create table IF not exists `buyma`
(
 `id`               INT(20) AUTO_INCREMENT,
 `name`             TEXT NOT NULL,
 `price`            VARCHAR(20) NOT NULL,
 `brand`            VARCHAR(20) NOT NULL,
 `shopper`          VARCHAR(20) NOT NULL,
 `created_at`       Datetime DEFAULT NULL,
 `updated_at`       Datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
