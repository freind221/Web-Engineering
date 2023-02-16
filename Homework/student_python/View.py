from Controller import StudentController, FacultyController
from Utils import *
import time


def main():
    try:
        while True:
            choice = mainMenu()
            if choice == 1:
                subMenuChoice = subMenu("faculty")
                facultyController = FacultyController()
                if subMenuChoice == 1:
                    isLoginSuccessful = facultyController.login()
                    if isLoginSuccessful:
                        while True:
                            loggedInMenuChoice = loggedInMenu(
                                "faculty", username=facultyController.faculty.username)
                            if loggedInMenuChoice == 1:
                                facultyController.view_profile()
                            elif loggedInMenuChoice == 2:
                                facultyController.edit_profile()
                            elif loggedInMenuChoice == 3:
                                facultyController.delete_profile()
                                break
                            elif loggedInMenuChoice == 4:
                                break
                    else:
                        time.sleep(1)

                elif subMenuChoice == 2:
                    isRegistrationSuccessful = facultyController.register()
                    if isRegistrationSuccessful:
                        time.sleep(1)
                        main()
                        break
                elif subMenuChoice == 3:
                    main()
                    break
            elif choice == 2:
                subMenuChoice = subMenu("student")
                studentController = StudentController()
                if subMenuChoice == 1:
                    isLoginSuccessful = studentController.login()
                    if isLoginSuccessful:
                        while True:
                            loggedInMenuChoice = loggedInMenu(
                                "student", username=studentController.student.username)
                            if loggedInMenuChoice == 1:
                                studentController.view_profile()
                            elif loggedInMenuChoice == 2:
                                studentController.edit_profile()
                            elif loggedInMenuChoice == 3:
                                studentController.delete_profile()
                                break
                            elif loggedInMenuChoice == 4:
                                break
                    else:
                        time.sleep(1)
                elif subMenuChoice == 2:
                    isRegistrationSuccessful = studentController.register()
                    if isRegistrationSuccessful:
                        time.sleep(1)
                        main()
                        break
                elif subMenuChoice == 3:
                    main()
                    break
            elif choice == 3:
                print("Thank you for using the FCIT Management System.")
                break
    except KeyboardInterrupt:
        print("Thank you for using the FCIT Management System.")