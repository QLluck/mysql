-- Active: 1741182957477@@127.0.0.1@3306@test
show databases;
use test;
select database();
desc testtb;insert into testtb (id) values (1);

select * from testtb;

