
# 1. Library Book Tracker
library: dict = {}
def add_book(title: str, author: str, pages: int):
    title = title.lower()
    if title in library.keys():
        print(f"\nThe product '{title}' already exists and was not added.")
        return
    library[title] = (author, pages)
    print(f"\nThe product '{title}' was added to the library.")

def find_book(title:str):
    book:tuple = library.get(title)
    if book:
        print(f"\nTitle: {title}, Author: {book[0]}, Pages: {book[1]}")

def show_books():
    if library:
        print("\nLibrary:")
        for title, (author, pages) in library.items():
            print(f"Title: {title} | Author: {author} | Pages: {pages}")
    else:
        print(f"The library is empty.")


# 2. Student Grade Manager
grades: dict = {}


def add_student(name: str):
    name = name.lower()
    if name in grades.keys():
        print(f"\nThe student'{name}' already exists and was not added.")
        return
    grades[name] = []
    print(f"\nThe student '{name}' was added.")


def add_grade(name:str, grade:int):
    name = name.lower()
    for student, grade_list in grades.items():
        if name == student:
            grades[student].append(grade)
            print(f"the grade '{grade}' was added to student '{student}'.")
            break

def get_average(name:str):
    name = name.lower()
    student = grades.get(name)
    if student:
        print(f"Average :{sum(student) / len(student)}")


# 3. Restaurant Menu Editor
menu: dict = {}
def add_dish(dish:str, price:float, is_available:bool = False):
    dish = dish.lower()
    if dish in menu.keys():
        print(f"\nThe dish '{dish}' already exists and was not added.")
        return
    menu[dish] = (price, is_available)
    print(f"\nThe dish '{dish}' was added.")



def change_availability(dish:str, is_available:bool = False):
    for name, (price, _) in menu.items():
        if name == dish:
            menu[dish] = (price, is_available)
            print(f"\nThe dish availability was changed to '{is_available}'.")

        else:
            print(f"\nThe dish doesn't exist.The availability was not changed.")

def total_available_price():
    total_available: int = 0
    for name, (price, is_available) in menu.items():
        if is_available:
            total_available +=1
    print(f"\nThe total available dishes is: {total_available}.")


# 4. Warehouse Box Counter
warehouse: dict = {}
def add_box(box_type:str, amount: int):
    if box_type in warehouse.keys():
        print(f"\nThe box type '{box_type}' already exists and was not added.")
        return
    warehouse[box_type] = amount
    print(f"\nThe box type '{box_type}' was added.")


def update_quantity(box_type:str, new_amount:int):
    for name, amount in warehouse.items():
        if name == box_type:
            warehouse[name] = new_amount
            print(f"\nThe amount was update to '{new_amount}'.")

        else:
            print(f"\nThe box type doesn't exist.The amount was not updated.")

def has_enough(box_type:str, value:int):
    for name, amount in warehouse.items():
        if box_type == name:
            if amount >= value:
                print(f"\nThe box type '{name}' is enough.")
                break
            else:
                print(f"\nThe box type '{name}' is not enough.")
                break




# 5. Movie Rating System
movies: dict = {}
def add_movie(name:str):
    name = name.lower()
    if name in movies.keys():
        print(f"\nThe movie'{name}' already exists and was not added.")
        return
    movies[name] = []
    print(f"\nThe movie '{name}' was added.")

def rate_movie(name:str, rate:float):
    name = name.lower()
    for movie, rates in movies.items():
        if name == movie:
            movies[movie].append(rate)
            print(f"\nThe rate of movie '{movie}' was added.")
            break
        else:
            print(f"\nThe movie '{movie}' doesn't exist.")
            break



def average_rating(name:str):
    name = name.lower()
    movie = movies.get(name)
    if len(movie) > 0:
        print( sum(movie) / len(movie))


# 6. Online Course Tracker
courses: dict = {}
def add_course(title: str, duration: int, inscribed: int ): pass


def update_enrollment(): pass
def filter_by_hours(): pass

# # 7. To-Do List Organizer
# def add_task(): pass
# def complete_task(): pass
# def filter_tasks(): pass
#
# # 8. Digital Wallet
# def add_expense(): pass
# def total_spent(): pass
# def expense_percentages(): pass
#
# # 9. Pet Adoption Center
# def add_pet(): pass
# def find_by_species(): pass
# def older_than(): pass
#
# # 10. Gym Membership System
# def register_member(): pass
# def change_plan(): pass
# def unpaid_members(): pass
