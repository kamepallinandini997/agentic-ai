from services.employee import Employee
from services.department import Department
from services.role import Role

def menu():
    while True:
        print("\n============= EMPLOYEE SYSTEM ==============")
        print('1. Add Department')
        print('2. List Department')
        print('3. Add Role')
        print('4. List roles')
        print('5. Add Employee')
        print('6. List Employee')
        print('7. Delete Employe')
        print('0. Exit')

        choice = input("Choose an option: ")
        
        if choice == '1': Department.add_department()
        elif choice == "2": Department.list_departments()
        
        elif choice == "3": Role.add_role() 
        elif choice == "4": Role.list_roles()
        
        elif choice == "5":Employee.add_employee()
        elif choice == "6":Employee.list_employees()
        elif choice == "7":Employee.delete_employee()
        
        elif choice == "0": print('Exiting... Bye');break
        else: print("Invalid choice")

if __name__=='__main__':
    menu()