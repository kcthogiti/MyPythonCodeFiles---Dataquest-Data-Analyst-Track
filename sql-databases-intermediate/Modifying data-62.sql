## 2. Working with dates in SQL ##

select *
from facts
where updated_at > '2015-10-30 16:00'
and updated_at < '2015-11-02 15:00'

## 3. Data types ##

PRAGMA table_info(facts)

## 4. Primary keys ##

select *
from facts
order by id desc
limit 1;

## 5. Inserting data into a table ##

insert into facts
VALUES(262, "dq", "DataquestLand", 60000, 40000, 20000, 500000, 100, 50, 10, 20, "2016-02-25 12:00:00", "2016-02-25 12:00:00")

## 6. Missing values ##

INSERT INTO FACTS
VALUES(263, "dq", "DataquestLand", NULL, NULL, 20000, 500000, 100, 50, 10, 20, "2016-02-25 12:00:00", "2016-02-25 12:00:00")

## 7. Updating rows ##

UPDATE FACTS
SET name = "DataquestLand"
WHERE NAME = 'United States';

## 8. Deleting rows ##

delete from facts
where name = "canada"