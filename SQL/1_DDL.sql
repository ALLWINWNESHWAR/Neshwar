/* DDL - Data Definition Language */
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
