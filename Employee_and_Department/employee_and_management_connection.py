import json
import os

# File Path(s)
EMPLOYEES_JSON="employees.json"
#--------------------Helper Methods---------------------

def save_to_json(data,file):
    """Save a list f dictionaries to a JSON file"""
    with open(file,'w') as f:
        return json.dump(data, f,indent=4)

def load_from_json(file):
    """Load and return list of dictionaries from JSON file."""
    if not os.path.exists(file):
        return []
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return [] 


#-----------------------Implementation Classes--------------------

class Employee:
    def __init__(self,emp_id,first_name,last_name,doj,salary,department,role):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.doj = doj
        self.salary = salary
        self.department = department
        self.role = role 
        pass

    def to_dict(self):
        return vars(self)
    
    def __str__(self):
        return f'Role [{self.emp_name_id}]-{self.emp_name}'
    
    @classmethod
    def add_employee(cls):
        emp_id = input("Enter Employee id: ")
        first_name = input("Enter First Name: ")
        last_name =input("Enter Last Name: ")
        doj = input("Enter Date of Joining: ")
        salary = input("Enter Employee Salary: ")
        department = input("Enter Employee Department: ")
        role = input("Enter Employee Role: ")

        # Load the existing Employee List
        employees = load_from_json(EMPLOYEES_JSON)
        emp = Employee(emp_id,first_name,last_name,doj,salary,department,role).to_dict()
        
        employees.append(emp)#Append the new employee into existing Json

        save_to_json(employees,EMPLOYEES_JSON)# Recreate Json
        print("Employee is added to the Collection......")
    
    def list_employees():

        """List all  Employees"""
        #emp_id,first_name,last_name,doj,salary,department,role
        
        employees=load_from_json(EMPLOYEES_JSON)
        print("Registered Employees: ")
        for e in employees:
            print(f"{e['emp_id']}:{e['first_name']} : {e['last_name']} : {e['salary']}")
    
    def delete_employee():

        emp_id = input("Enter Employee ID to be deleted : ")
        employees = load_from_json(EMPLOYEES_JSON)
        new_list = list(filter(lambda e : e['emp_id']!=emp_id,employees))
        save_to_json(new_list,EMPLOYEES_JSON)#Recreate the Employee JSON
        print("Employee Deleted...")

class Department:
    def __init__(self,dept_id,dept_name):
        self.dept_id = dept_id
        self.dept_name = dept_name 
        pass       

    def to_dict(self):
        return vars(self)
    
    @classmethod
    def add_department(cls):
        dept_id = input("Enter Department ID: ")
        dept_name = input("Enter Department Name: ")

        departments = load_from_json(DEPARTMENTS_JSON)

        department = Department(dept_id,dept_name).to_dict()
        departments.append(department)
        save_to_json(departments,DEPARTMENTS_JSON)    

    def list_departments():
        """List all saved departments"""
        departments=load_from_json(DEPARTMENTS_JSON)
        print("Available Departments: ")
        for d in departments:
            print(f"{d['dept_id']} : {d['dept_name']}")

    def __str__(self):
        return f'Department [{self.dept_id}]-{self.dept_name}'

class Role:
    def __init__(self,role_id,role_name):
        self.role_id = role_id
        self.role_name = role_name
        pass

    def to_dict(self):
        return vars(self)
    
    @classmethod
    def add_role(cls):
        role_id = input("Enter Role ID: ")
        role_name = input("Enter Role Name: ")

        roles = load_from_json(ROLES_JSON)
        role = Role(role_id, role_name).to_dict()
        roles.append(role)
        save_to_json(roles, ROLES_JSON)

    def list_roles():
        """List all saved roles"""
        roles=load_from_json(ROLES_JSON)
        print("Available Roles: ")
        for r in roles:
            print(f"{r['role_id']} : {r['role_name']}")
        
    def __str__(self):
        return f'Role [{self.role_id}]-{self.role_name}'

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