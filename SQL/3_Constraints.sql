-- contraints
-- 1. primary key
-- 2. not null
-- 3. unique
-- 4. check
-- 5. foreigh key

--creating table 1
create table city(
  city_id number primary key,
  city_name varchar2(20) 
  );
insert all
into city values(10,'chennai'),
into city values(20,'bangalore'),
into city values(30,'kochin')
commit;

--creating table 2
create table customer(
  cus_id number unique,
  cus_name varchar2(20) not null,
  mobile number unique,
  age number,
  city_id number referances city(city_id),
  );
insert all
into customer values(2201,'allwin',1234567890, 23,30),
into customer values(2202,'gopal',0987654321, 23,30),
into customer values(2203,'balaji',1234509876, 23,30),
into customer values(2204,'madesh',0987612345, 23,30),
into customer values(2205,'ragul',6789012345, 23,30),
into customer values(2206,'karthick',5432167890, 23,30),
into customer values(2207,'zee',5432109876, 23,30),
into customer values(2208,'meg',6789054321, 23,30),
into customer values(2209,'begam',2345678910, 23,30),
into customer values(2210,'barani',2345678901, 23,30),
commit;

--select statement 

  
