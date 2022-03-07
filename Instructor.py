import sqlite3;

conn = sqlite3.connect("DB-Project-Python-Files/databases.sqlite");
cur = conn.cursor();

class Instructor:
	instructor_id = -1 ;


	def login(self,email,password):
		'''Login Function for Instructor'''
		cur.execute('''
			SELECT i.first_name , i.last_name , i.instructor_id
			FROM Instructor i
			WHERE i.email = ? and i.password = ?
		'''	, 	(email,password) );

		# grabbing results in a row
		row = cur.fetchone();

		#iterating over row
		if row is None:
			# if user does not exist in database
			print("Login Failed")
			self.instructor_id = -1
			return False;
		else:
			print("Welcome",row[0],row[1],"!");
			print("You have successfully login.");
			self.instructor_id = row[2];
			return True;



	def register(self,first_name,last_name,email,password,DOB):
		'''Register for Instructor'''
		try:
			cur.execute('''
				INSERT INTO Instructor 
				(first_name,last_name,email,password,DOB) 
				VALUES (?,?,?,?,?)
				''' , (first_name,last_name,email,password,DOB))
			conn.commit();
			print(first_name,last_name, "registered successfully.")
			return True;
		except:
			print("Register Failed.")
			return False;




	def view_courses(self):
		'''View an instructor contributed courses'''

		cur.execute('''
			SELECT c.course_code , c.title , c.credit_hr , c.duration
			FROM Course c
			JOIN Instructor i ON c.instructor_id = i.instructor_id
			WHERE i.instructor_id = ?
		''' , (self.instructor_id,))

		row = cur.fetchall();
		

		
		print("\n\n")
		print("-"*150)
		print("CONTRIBUTED COURSES".center(150))
		print("\n")
		for item in row:
			course_code = item[0];
			title = item[1];
			credit_hr = item[2];
			duration = item[3];
			print("Course Code: {:^20} --  Title: {:^20} --  Credit Hours: {:^20} -- Duration: {:^20}   ".format(course_code,title,credit_hr,duration));
		
		print("\n")
		print("-"*150)
		print("\n\n")






	def view_enrolled_students(self):
		'''VIEW ENROLLED STUDENTS IN CONTRIBUTED COURSES'''

		cur.execute('''
			SELECT  c.title , s.first_name , s.last_name , s.email, s.gender , c.status , s.student_id
			FROM Instructor f
			JOIN Course c ON f.instructor_id = c.instructor_id
			JOIN Enrolled e ON e.course_id = c.course_id
			JOIN Student s ON e.student_id = s.student_id
			WHERE f.instructor_id = ?
			ORDER BY c.title
		''', (self.instructor_id,))

		row = cur.fetchall();


		print("\n\n")
		print("-"*150)
		print("ENROLLED STUDENTS".center(150))
		print("\n")

		for item in row:
			title = item[0]
			name = item[1] + item[2]
			email = item[3]
			gender = item[4]
			print("Title: {:^20} -- Name: {:^20} -- Email: {:^20} -- Gender: {:^20} ".format(title,name,email,gender));

		print("\n")
		print("-"*150)
		print("\n\n")

	


	def add_course(self,course_code,title,credit_hr,duration,category):
		'''INSTRUCTOR CAN ADD A COURSE INTO THE DATABASE'''

		def get_category_id(category):
			'''LOOKING FOR CATEGORY ID TO SEE IF CATEGORY EXISTS'''
			cur.execute('''
					SELECT c.category_id
					From Category c
					Where c.category = ?
				''' , (category,))
			try:
				category_id = cur.fetchone()[0];
				return category_id;
			except:
				return  -1


		category_id = get_category_id(category);
		# if category already does not exist
		if (category_id == -1 ):
			cur.execute('''
				INSERT INTO Category 
				(category)
				VALUES (?)
			''', (category,))
			conn.commit();
		category_id = get_category_id(category);
                                                                                                  		 


	
		try:
			cur.execute('''
				INSERT INTO Course 
				(course_code,title,credit_hr,duration,status,category_id,instructor_id)
				VALUES (?,?,?,?,'In-Progress',?,?)
			''' , (course_code,title,credit_hr,duration,category_id,self.instructor_id))
			conn.commit();
			print("\n\t\tCourse:",course_code,"added successfully.")
			return True;
		except:
			print("\n\t\tCourse:",course_code,"addition failed.")
			return False;

	



