import json
import os 
import datetime

# py i:/Python_NC/labs/task.py
users_file = r"I:\Python_NC\labs\users.json"
projects_file=r"I:\Python_NC\labs\projects.json"

def load_users():
    if os.path.exists(users_file):
        if os.stat(users_file).st_size == 0: 
            return []
        with open(users_file, "r") as f:
            try:
                return json.load(f) 
            except json.JSONDecodeError:
                print('Error')
                return []  
    return []  

def save_users(users):
    with open(users_file, "w") as f:
        json.dump(users, f, indent=4)
        f.flush()

if not os.path.exists(users_file):
    save_users([])

# for projeact
def load_projects():
    if os.path.exists(projects_file):
        if os.stat(projects_file).st_size == 0: 
            return []
        with open(projects_file, "r") as f:
            try:
                return json.load(f) 
            except json.JSONDecodeError:
                print('Error')
                return []  
    return []  

def save_projects(projects):
    with open(projects_file, "w") as f:
        json.dump(projects, f, indent=4)
        f.flush()

if not os.path.exists(projects_file):
    save_projects([])


def create_project(user):
    projects=load_projects()
    Title=input('Title Project: ').strip()
    if not Title:
        print('Title reguired')
        return
    
    Details=input('Details Project: ').strip()
    if not Details:
        print('Details reguired')
        return
    Target=float(input('Target Project: '))
    if (Target<=0):
        print('target must positive number')
        return
    Start_date=input('Start Date (yyyy-mm-dd): ').strip()
    End_date=input('End Date (yyyy-mm-dd): ').strip()

    start_date = datetime.datetime.strptime(Start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(End_date, "%Y-%m-%d")
    if not start_date or not end_date:
        print('Date reguired')
        return
    
    projects.append({"title": Title, "details": Details, "target": Target, "start_date": Start_date, "end_date": End_date, "owner": user["email"]})
    save_projects(projects)
    print("Project created successfully!")


def view_user_projects(user):
    projects=load_projects()
    user_projects = [project for project in projects if project["owner"] == user["email"]]
    if not user_projects:
        print('no projects for you')
    else:
        for  project in user_projects:
            print(f"Title: {project['title']}\n"
            f"Details: {project['details']}\n"
            f"Target: {project['target']}\n"
            f"Start Date: {project['start_date']}\n"
            f"End Date: {project['end_date']}")
            print ('---------------------------')


def view_all_projects():
    projects=load_projects()
    if not projects:
        print('no exist projects')
    else:
        for  project in projects:
            print(f"Title: {project['title']}\n"
            f"Details: {project['details']}\n"
            f"Target: {project['target']}\n"
            f"Start Date: {project['start_date']}\n"
            f"End Date: {project['end_date']}") 
            print ('---------------------------') 
        
        
def search_project():
    projects = load_projects()
    print("Search by: ")
    print("1- Start Date")
    print("2- End Date")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        start_date = input("Enter start date (yyyy-mm-dd): ").strip()
        exist_project = [project for project in projects if project['start_date'] == start_date]

    elif choice == '2':
        end_date = input("Enter end date (yyyy-mm-dd): ").strip()
        exist_project = [project for project in projects if project["end_date"] == end_date]

    else:
        print("invalid choice")
        return

    if  exist_project:
        for project in  exist_project:
            print(f"Title: {project['title']}\n"
            f"Details: {project['details']}\n"
            f"Target: {project['target']}\n"
            f"Start Date: {project['start_date']}\n"
            f"End Date: {project['end_date']}")  
            print ('---------------------------')
    else:
        print("Not found ")

def project_menu(user):
    while True:
        print(f"+++++++ Welcome {user['first_name']} ++++++++")
        print("1️-Create project")
        print("2-view your projects")
        print("3-view all projects")
        print("4-search project")
        print("5- exit")

        choice = input("Please enter your choice: ")

        if choice == '1':
            create_project(user)
        elif choice == '2':
            view_user_projects(user)
        elif choice == '3':
            view_all_projects()
        elif choice == '4':
            search_project()
        elif choice == '5':
            print('Thanks for visit program')
            break
        else:
            print("Invalid choice")

# sign_up
def Register():
    users = load_users()
    print('++++++ Registration Form ++++++ ')

    Fname=input('Please enter your first name : ').strip()
    Lname=input('Please enter your last name : ').strip()
    Email=input('Please enter your email : ').strip()
    if '@' not in Email or '.' not in Email.split('@')[-1]:
        print('invaild email ')
        return
    
    for user in users:
        if user["email"]==Email:
            print('this email is exist')
            return

    Phone=input('Please enter your phone : ').strip()

    Password=input('Please enter your password : ').strip()
    if (len(Password)<10) or (not any(i.isupper() for i in Password)) or (not any(i.isdigit() for i in Password)):
        print('password should contain at least one upperCase and one digit please')
        return
    
    confirm_password=input('Please enter your password again : ').strip()
    if Password != confirm_password:
        print("Passwords do not match!")
        return
    
    users.append({"first_name": Fname, "last_name": Lname, "email":Email, "password": Password, "phone": Phone})
    save_users(users)
    print("Registration successful! Go to log in.")

# login user
def login():
    users = load_users()
    print('++++++ Login Form ++++++ ')

    Email=input('Please enter your email : ').strip()
    Password=input('Please enter your password : ').strip()
    for user in users :
        if user["email"]==Email and user["password"]==Password:
            print("Login successful")
            project_menu(user)
            return
        
    print('invaild email and password')


while True:
    print('++++++ main menu ++++++ ')
    print('1-Register')
    print('2-Login')
    print('3-Exit')

    choice=input('Please enter your choice: ')
    if (choice=='1'):
        Register()
    elif (choice=='2'):
        login()   
    elif (choice=='3'):
        print('Thanks for visit program')
        break
    else:
        print('invaild choice')





