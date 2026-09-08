/* DDL - Data Definition Language */
/* 1. create */
/* 2. insert*/
/* 3. update */
/* 4. alter */
/* 5. drop */
create table customer(customer_id number(6),
  cust_name number(10),
  mobile_no number(10),
  dob date,
  city varchar2(30),
  mail varchar2(30)
  );

select * from customer;
insert into customer (customer_id,cust_name,mobile_no,dob,city,mail)
values (2203,'allwin',9626932842,to_date('28/04/2003', 'dd/mm/yyyy'),'chennai','allwin@gmail.com')

insert into customer
values (2201,'akilan',9999966666,to_date('15/01/2025', 'dd/mm/yyyy'),'salem','akilan@gmail.com')

insert into customer
values (2205,null,1234567890,to_date('23/05/2024', 'dd/mm/yyyy'),'thiruvarur','samsa@gmail.com')

select * from customer;

rollback;        /* it mean : ctrl+z */

commit;          /* it mean : it is commited */

/* update */
update customer
set cust_name='samsa', where customer_id=2205;

/* add a coloum */
alter table customer
add country varchar2(50);

update customer set country='india';

/* drop a coloum */
alter table customer
drop coulumn city;




