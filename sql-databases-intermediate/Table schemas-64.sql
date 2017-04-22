## 2. Adding columns ##

alter table facts
add leader text

## 6. Creating a table with relations ##

create table factbook.states
(
    id integer primary key, 
    name text, 
    area integer, 
    country integer, 
    FOREIGN KEY (country) REFERENCES facts(id)
)

## 7. Querying across foreign keys ##

select *
from landmarks l
inner join facts f on f.id = l.country

## 8. Types of joins ##

select *
from landmarks l
left outer join facts f on f.id = l.country