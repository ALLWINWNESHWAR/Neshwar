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



