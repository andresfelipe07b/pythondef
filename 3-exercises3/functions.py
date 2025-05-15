
# 1. Library Book Tracker
library: dict = {}
def add_book(title: str, author: str, pages: int)-> None:
    title = title.lower()
    if title in library.keys():
        print(f"\nThe product '{title}' already exists and was not added.")

    library[title] = (author, pages)
    print(f"\nThe product '{title}' was added to the library.")

def find_book(title:str)-> str or tuple:
    book:tuple = library.get(title)
    if book:
        return f"Title: {title}, Author: {book[0]}, Pages: {book[1]}"
    else:
        return f"Book not found."

def show_books()-> None:
    if library:
        print("\nLibrary:")
        for title, (author, pages) in library.items():
            print(f"Title: {title} | Author: {author} | Pages: {pages}")
    else:
        print(f"The library is empty.")


# 2. Student Grade Manager
grades: dict = {}


def add_student(name: str)-> None:
    name = name.lower()
    if name in grades.keys():
        print(f"\nThe student'{name}' already exists and was not added.")
        return
    grades[name] = []
    print(f"\nThe student '{name}' was added.")


def add_grade(name:str, grade:int)-> None:
    name = name.lower()
    for student, grade_list in grades.items():
        if name == student:
            grades[student].append(grade)
            print(f"the grade '{grade}' was added to student '{student}'.")
            break

def get_average(name:str)-> float or str:
    name = name.lower()
    student = grades[name]
    if student:
        average: float = sum(student) / len(student)
        return average
    else:
        return "Student not found."


# 3. Restaurant Menu Editor
menu: dict = {}
def add_dish(dish:str, price:float, is_available:bool = False)-> None:
    dish = dish.lower()
    if dish in menu.keys():
        print(f"\nThe dish '{dish}' already exists and was not added.")
        return
    menu[dish] = (price, is_available)
    print(f"\nThe dish '{dish}' was added.")



def change_availability(dish:str, is_available:bool = False)-> None:
    for name, (price, _) in menu.items():
        if name == dish:
            menu[dish] = (price, is_available)
            print(f"\nThe dish availability was changed to '{is_available}'.")

        else:
            print(f"\nThe dish doesn't exist.The availability was not changed.")

def total_available_price()-> float:
    total = 0
    for name, (price, is_available) in menu.items():
        if is_available:
            total += price
    return total



# 4. Warehouse Box Counter
warehouse: dict = {}
def add_box(box_type:str, amount: int)-> None:
    if box_type in warehouse.keys():
        print(f"\nThe box type '{box_type}' already exists and was not added.")
        return
    warehouse[box_type] = amount
    print(f"\nThe box type '{box_type}' was added.")


def update_quantity(box_type:str, new_amount:int)-> None:
    for name, amount in warehouse.items():
        if name == box_type:
            warehouse[name] = amount + new_amount
            print(f"\nThe amount was update to '{new_amount}'.")

        else:
            print(f"\nThe box type doesn't exist.The amount was not updated.")

def has_enough(box_type:str, value:int)-> bool or str:

    for name, amount in warehouse.items():
        if box_type == name:
            if amount >= value:
                return True
            else:
                return False
        return "The box type doesn't exist."
    return None


# 5. Movie Rating System
movies: dict = {}
def add_movie(name:str)-> None:
    name = name.lower()
    if name in movies.keys():
        print(f"\nThe movie'{name}' already exists and was not added.")
        return
    movies[name] = []
    print(f"\nThe movie '{name}' was added.")

def rate_movie(name:str, rate:float)-> None:
    name = name.lower()
    for movie, rates in movies.items():
        if name == movie:
            movies[movie].append(rate)
            print(f"\nThe rate of movie '{movie}' was added.")
            break
        else:
            print(f"Movie not found.")
            break



def average_rating(name:str)-> float or str:
    name = name.lower()
    movie = movies.get(name)
    if len(movie) > 0:
        return sum(movie) / len(movie)
    else:
        return "Movie not found."


# 6. Online Course Tracker
courses: dict = {}
def add_course(title: str, duration: int, enrollments: int )-> None:
    if title in courses.keys():
        print(f"\nThe product '{title}' already exists and was not added.")

    courses[title] = (duration, enrollments)
    print(f"The course '{title}' was registered.")


def update_enrollment(title_name:str, e:int)-> None:
    for title, (duration, enrollment) in courses.items():
        if title == title_name:
            courses[title_name] = (duration, enrollment + e)
            print(f"\nThe enrollments was update.")

        else:
            print(f"\nTitle '{title}' not found.")

def filter_by_hours(minimum_hours: int)-> list:
    return [name for name, (duration, enrollments) in courses.items()
            if duration > minimum_hours]


# 7. To-Do List Organizer
todos: dict = {}
def add_task(task:str, priority:str)-> None:
    if task in todos.keys():
        print(f"\nTask '{task}' already exists and was not added.")

    todos[task] = {"priority": priority, "status": "pending"}
    print(f"Task '{task}' was registered.")

def complete_task(task:str)-> None:
    if task in todos:
        todos[task]["status"] = "completed"


def filter_tasks(priority: str, status: str)-> list:
    filtered: list = []
    for task_name, task_info in todos.items():
        matches = True
        if priority and task_info["priority"] != priority:
            matches = False
        if status and task_info["status"] != status:
            matches = False

        if matches:
            filtered.append(task_name)

    return filtered

# # 8. Digital Wallet
wallet = {}
def add_expense(category: str, amount: float)-> None:
    if category in wallet:
        wallet[category] += amount
    else:
        wallet[category] = amount


def get_total_expenses() -> float:
    return sum(wallet.values())


def expense_percentages() -> dict:
    total:float = get_total_expenses()
    if total == 0:
        return {}

    percentages:dict = {}
    for category, amount in wallet.items():
        percentage = (amount / total) * 100
        percentages[category] = percentage

    return percentages

# 9. Pet Adoption Center
pets: list = []
def add_pet(name: str, species: str, age: int)-> None:
    pet = {
        "name": name,
        "species": species,
        "age": age
    }
    pets.append(pet)


def find_by_species(species: str) -> list:
    return [pet for pet in pets if pet["species"].lower() == species.lower()]


def older_than(min_age: int) -> list:
    return [pet for pet in pets if pet["age"] > min_age]


# 10. Gym Membership System
members: dict = {}
def register_member(name:str, plan:str, payment_status:str)-> None:
    members[name] = {
        "plan": plan,
        "payment_status": payment_status
    }


def change_plan(name:str, new_plan:str)-> bool:
    if name in members:
        members[name]["plan"] = new_plan
        return True
    return False


def unpaid_members() -> list:
    return [
        name
        for name, info in members.items()
        if info["payment_status"] == "late"
    ]

