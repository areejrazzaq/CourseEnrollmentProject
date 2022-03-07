from Student import * 
from Instructor import *

s = Student()
i = Instructor()
login_student = False
login_instructor = False


def main_menu():
	print("\n\tPress 1 for Student")
	print("\tPess 2 for Instructor")


def login_menu():
	print("\n\tPress 1 to login")
	print("\tPress 2 to register")

def student_menu():
	print("\n\tPress 1 to view available courses.")
	print("\tPress 2 to view enrolled courses.")
	print("\tPress 3 to enroll in a course")

def instructor_menu():
	print("\n\tPress 1 to view contributed courses.")
	print("\tPress 2 to view enrolled students.")
	print("\tPress 3 to add a course.")


def student_calls():
	while True:
		choice = int(input("\nEnter your choice: "))
		if (choice == 1):
			s.view_all_courses()
		elif (choice == 2):
			s.view_enrolled_courses()
		elif (choice == 3):
			course_code = input("\tCourse code: ")
			s.enroll_course(course_code)
		else:
			break
		



def instructor_calls():
	while True:
		choice = int(input("\nEnter your choice: "))
		if (choice == 1):
			i.view_courses()

		elif (choice == 2):
			i.view_enrolled_students()

		elif (choice == 3):
			print("Fill Details\n")
			course_code = input("\tCourse code: ")
			title = input("\tTitle: ")
			credit_hr = int(input("\tCredit Hours: "))
			duration = int(input("\tDuration (In Months) : "))
			category = input("\tCategory: ")
			i.add_course(course_code,title,credit_hr,duration,category)
		else:
			break
	








def MAIN():
	
	
	
	while True: 
		main_menu()
		choice = int(input("\nEnter your choice: "))

		if ( choice == 1 ):
			# instance of student
			login_menu()

			select_login = int(input("\nEnter your choice: "))

			if (select_login == 1):
				# login of student
				email = input("\tEnter email ( dyushin0@dedecms.com ): ")
				password = input("\tEnter password ( vHhrSXyDrLsi ) : ")

				if (s.login(email,password)):
					login_student = True
				else:
					login_student = False

				if (login_student):
					student_menu()
					student_calls()


			
			elif ( select_login == 2):
				while (select_login == 2):
					# register of student
					print("**Fill in the details**\n")
					first_name = input("\tFirst name: ")
					last_name = input("\tLast name: ")
					email = input("\tEmail: ")
					password = input("\tPassword: ")
					DOB = input("\tDate of Birth: ")
					gender = input("\tGender: ")
					phone_num = input("\tPhone number: ")
					street = input("\tStreet: ")
					city = input("\tCity: ")
					country  = input("\tCountry: ")

					if(s.register(first_name,last_name,email,password,DOB,gender,phone_num,street,city,country)):
						choice = 1
						select_login = 1
						break
					else:
						print("Try Again")
						select_login = 2

			else :
				print("Bad Choice" )
		


		# selection of instructor
		elif (choice == 2):
			login_menu()

			select_login = int(input("\nEnter your choice: "))

			if (select_login == 1):
				# login of instructor
				email = input("\tEnter email ( cgorges0@smh.com.au ) : ")
				password = input("\tEnter password ( WQk8ui ) : ")

				if (i.login(email,password)):
					login_instructor = True
				else:
					login_instructor = False

				if(login_instructor):
					instructor_menu()
					instructor_calls()


			 # registering instructors
			elif ( select_login == 2):
				# register of instructor
				print("**Fill in the details**\n")
				first_name = input("\tFirst name: ")
				last_name = input("\tLast name: ")
				email = input("\tEmail: ")
				password = input("\tPassword: ")
				DOB = input("\tDate of Birth: ")
				
				if(i.register(first_name,last_name,email,password,DOB) == True):
					select_login = 1
				else:
					print("Try Again")
					select_login = 2


			else :
				print("Bad Choice" )

		else:
			print("THANK YOU".center(150))
			break






MAIN()


 
