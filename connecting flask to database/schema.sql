drop table  if exists shop;
drop table  if exists tags;

create table shop (
id integer primary key,
name text not null,
place text,
type text
);

create table tags( 
shopid integer,
tag text
);