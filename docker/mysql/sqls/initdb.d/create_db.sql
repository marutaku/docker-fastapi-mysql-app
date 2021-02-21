DROP DATABASE IF EXISTS app;
CREATE DATABASE app;
USE app
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS articles;

/* TIMESTAMP with implicit DEFAULT value is deprecated. */
SET GLOBAL explicit_defaults_for_timestamp = 1;

CREATE TABLE users
(
    id         int(12) primary key auto_increment,
    username   varchar(100) not null,
    password   varchar(100) not null,
    created_at datetime     not null default CURRENT_TIMESTAMP
) CHARACTER SET UTF8
  COLLATE utf8_general_ci;

CREATE TABLE articles
(
    id         int(12) primary key auto_increment,
    user_id    int(12)       not null,
    title      varchar(1000) not null,
    body       varchar(1000) not null,
    created_at datetime      not null default CURRENT_TIMESTAMP
) CHARACTER SET UTF8
  COLLATE utf8_general_ci;
