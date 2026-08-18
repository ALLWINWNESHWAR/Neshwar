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
values (2203,'allwin',9626932842,to_date('18/08/2026', 'dd/mm/yyyy'),'chennai','allwin@gmail.com')
