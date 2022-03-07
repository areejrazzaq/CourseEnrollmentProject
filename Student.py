import sqlite3;
from datetime import datetime

conn = sqlite3.connect("DB-Project-Python-Files/databases.sqlite");
cur = conn.cursor();


class Student:
	student_id = 0;
	date = datetime.today().strftime('%d/%m/%y')


	def login(self,email,password):
		'''Login Function for Student'''
		cur.execute('''
			SELECT s.first_name , s.last_name , s.student_id
			FROM Student s
			WHERE s.email = ? and s.password = ?
		'''	, 	(email,password) );

		row = cur.fetchone();

		if row is None:
			print("Login Failed".center(20,"*"))
			#login_status=False;
			self.student_id = -1;
			return False;
		else:
			print("\n\tWelcome",row[0],row[1]);
			#login_status=True;
			self.student_id = row[2]
			return True;




	def register(self,first_name,last_name,email,password,DOB,gender,phone_num,street,city,country):
		'''Register for Student'''
		try:
			cur.execute('''
				INSERT INTO Student 
				(first_name,last_name,email,password,DOB,gender,phone_num,street,city,country) 
				VALUES (?,?,?,?,?,?,?,?,?,?)
				''' , (first_name,last_name,email,password,DOB,gender,phone_num,street,city,country))
			conn.commit();
			print("\n",first_name,last_name, "registered successfully.")
			return True;
		except:
			print(first_name,last_name, "registered unsuccessful.")
			return False;




	def view_all_courses(self):
		'''Student portal view all available courses'''
			
		cur.execute('''
			SELECT c.course_code , c.title , c.duration
			FROM Course c
		''')
		row = cur.fetchall();
		
		print("\n\n")
		print("-"*150)
		print("AVAILABLE COURSES".center(150))
		print("\n")

		for item in row:
			course_code = item[0];
			title = item[1];
			duration = item[2];
			print("Course Code: {:^30} -- Title: {:^30} --  Duration: {:^30} ".format(course_code,title,duration));

		print("\n")
		print("-"*150)
		print("\n\n")



	def view_enrolled_courses(self):
		'''SHOWING PERSON THEIR ENROLLED COURSES'''
		id_num = self.student_id
		cur.execute('''
			SELECT c.course_code , c.title , e.date_enrolled , c.status 
			FROM Course c
			JOIN Enrolled e ON c.course_id = e.course_id
			JOIN Student s ON e.student_id = s.student_id
			WHERE s.student_id = ?
		''' , (id_num,));
		row = cur.fetchall();
		

		print("\n\n")
		print("-"*150)
		print("ENROLLED COURSES".center(150))
		print("\n")

		for item in row:
			course_code = item[0];
			title = item[1];
			date = item[2];
			status = item[3];
			print("Course Code: {:^30} --  Title: {:^30} --  Date Enrolled: {:^30} -- Status: {:^30} ".format(course_code,title,date,status));

		print("\n")
		print("-"*150)
		print("\n\n")




	def enroll_course(self,course_code):
		'''ENROLLING STUDENT IN A COURSE BY PROVIDED COURSE CODE'''

		def get_course_id(course_code):
			cur.execute('''
				SELECT course_id
				FROM Course
				WHERE course_code = ?
			''', (course_code,))

			course_id = cur.fetchone();

			if (course_id is None):
				return -1;
			else:
				return course_id[0];


		course_id = get_course_id(course_code);

		if (course_id == -1):
			print('Course not available')
			return;

		try:
			# adding in the enrolled table
			cur.execute('''
				INSERT INTO Enrolled
				(student_id,course_id,date_enrolled)
				VALUES (?,?,?)
			''' , (self.student_id,course_id,self.date));
			conn.commit();
			print("Enrolled successfully");
			return True;
		except:
			return False;
			print('Enrollment Failed');





