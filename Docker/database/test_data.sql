create database test;

grant all on test.* to `pytest` @`%` identified by 'pytestpass';

use test;

create table user (
    id smallint unsigned not null auto_increment primary key,
    login_name varchar(16) not null unique key,
    first_name varchar(20),
    last_name varchar(20),
    gender enum('M', 'F') NOT NULL DEFAULT 'M',
    age tinyint unsigned,
    phone char(11),
    password varchar(512)
);

insert into `user` (
        login_name,
        first_name,
        last_name,
        gender,
        age,
        phone,
        password
    )
values (
        'LiYinkai',
        'Li',
        'Yinkai',
        'M',
        36,
        '15810697243',
        sha('pass4yinkai')
    ),
    (
        'nana',
        'Bai',
        'Na',
        'F',
        31,
        '13256734650',
        sha('pass4nana')
    );