show databases;
create database librarydb;
use librarydb;
show tables;
create table student(studid integer,studname varchar(20),bookname varchar(20), bookqty integer);
select * from student;
insert into student values(1,'Jana','Maths',20);
insert into student values(1,'Jana','Maths',20);
drop table student;

create table student(studid integer not null primary key, studname varchar(20) not null,bookname varchar(20), bookqty integer);
desc student;
insert into student values(1,'Jana','Maths',20);
insert into student values(2,'Jana','Maths',20);

create table books(