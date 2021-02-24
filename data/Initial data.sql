drop database hncj_course_assistant;
CREATE DATABASE IF NOT EXISTS hncj_course_assistant DEFAULT CHARSET utf8;
use hncj_course_assistant;

-- 添加管理员
insert into administrator values('root','670B14728AD9902AECBA32E22FA4F6BD',1);
delete from administrator where administrator_id = 'root';
select * from administrator;

-- 添加教师
insert into teacher values('888888888','root','张妍琰','670B14728AD9902AECBA32E22FA4F6BD',0,'avatar','13512345678','123@qq.com','',1);
insert into teacher values('777777777','root','张三','670B14728AD9902AECBA32E22FA4F6BD',0,'avatar','13512345678','123@qq.com','',1);
insert into teacher values('123456789','root','张四','670B14728AD9902AECBA32E22FA4F6BD',0,'avatar','13512345678','123@qq.com','',1);
insert into teacher values('123456780','root','张五','670B14728AD9902AECBA32E22FA4F6BD',0,'avatar','13512345678','123@qq.com','',1);
insert into teacher values('123456781','root','张六','670B14728AD9902AECBA32E22FA4F6BD',0,'avatar','13512345678','123@qq.com','',1);
delete from teacher where teacher_id = '888888888';
select * from teacher;

-- 添加学生
insert into student values('081417137','root','吴硕','670B14728AD9902AECBA32E22FA4F6BD',1,'avatar','15139744921','1234@qq.com','',1);

select * from student;