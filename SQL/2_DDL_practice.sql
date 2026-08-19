/* create */
create table student(student_id number(6),
  student_name varchar2(50),
  age number(5),
  email varchar2(100),
  department varchar2(30)
  );

create table employee (emp_id number(6),
  emp_name varchar2(50),
  salary number(10,2),
  job_role varchar2(40),
  joining_date date,
  phone varchar2(15)
  );

/* alter */
alter table student
add city varchar2(30);

alter table student
add (
  gender varchar2(10),
  marks number(5,2)
  );

/* modify */
alter table student
modify department varchar2(50);

/* rename */
alter table student
rename column student_name to full_name;

/* drop */
alter table student
drop column phone;

drop table employee;

/* Truncate */
truncate table student;

/* rename the table name */
rename student to students;


/* DDL Challenge */
 create table product (product_id number(6),
   product_name varchar2(50),
   price number(10,2),
   category varchar2(30),
   stock number(5)
   );

alter table product
add brand varchar2(30);

alter table product
modify category varchar2(50);


/* DDL Mixed Challenge */
create table customer (customer_id number(6),
  customer_name varchar2(50),
  email varchar2(100),
  phone varchar2(15),
  city varchar2(30)
  );

alter table customer
add age number(3);

alter table customer
modify city varchar2(50);

alter table customer
rename column phone to mobile;

alter table customer
drop column email;


/* DDL Mixed Challenge 2 */
create table orders (order_id number(6),
  customer_name varchar2(50),
  order_date date,
  amount number(10,2),
  status varchar2(20)
  );

alter table orders
add payment_mode varchar2(20);

alter table orders
modify amount number(12,2);

alter table orders
rename column status to order_status;

alter table orders
drop column payment_mode;

rename orders to customer_orders;


/* DDL Mixed Challenge 3 */
create table department (dept_id number(4),
  dept_name varchar2(40),
  location varchar2(50),
  manager varchar2(50)
  );

alter table department
add (employee_count number(5),
  budget number(12,2)
  );

alter table department
modify location varchar2(80);

alter table department
rename column manager to manager_name;

alter table department
drop column employee_count;

rename department to company_department;



















