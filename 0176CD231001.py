import random
from datetime import datetime

logged_user = None
logged_role = None


# ---------- REGISTRATION ----------
def register():
    print("\n--- Registration ---")
    username = input("Enter username: ")

    # Check if user exists
    with open("users.txt", "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == username:
                print("Username already exists!\n")
                return

    password = input("Enter password: ")
    name = input("Enter full name: ")
    branch = input("Enter branch: ")
    year = input("Enter year: ")
    email = input("Enter email: ")
    contact = input("Enter contact number: ")

    role = "admin" if username.lower() == "admin" else "user"

    with open("users.txt", "a") as f:
        f.write(f"{username}|{password}|{name}|{branch}|{year}|{email}|{contact}|{role}\n")

    print(f"\nRegistration successful for {name} ({role}).\n")


# ---------- LOGIN ----------
def login():
    global logged_user, logged_role
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "r") as f:
        for line in f:
            data = line.strip().split("|")
            if len(data) < 8:
                continue
            if data[0] == username and data[1] == password:
                logged_user = username
                logged_role = data[7]
                print(f"\nWelcome {data[2]}! ({logged_role}) logged in.\n")
                return
    print("Invalid username or password!\n")


# ---------- SHOW PROFILE ----------
def show_profile():
    if not logged_user:
        print("Please login first!\n")
        return

    with open("users.txt", "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == logged_user:
                print("\n--- Profile ---")
                print(f"Name: {data[2]}")
                print(f"Branch: {data[3]}")
                print(f"Year: {data[4]}")
                print(f"Email: {data[5]}")
                print(f"Contact: {data[6]}")
                print(f"Role: {data[7]}\n")
                return


# ---------- UPDATE PROFILE ----------
def update_profile():
    if not logged_user:
        print("Please login first!\n")
        return

    updated_lines = []
    with open("users.txt", "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == logged_user:
                print("\n--- Update Profile ---")
                data[2] = input(f"Enter new name ({data[2]}): ") or data[2]
                data[3] = input(f"Enter new branch ({data[3]}): ") or data[3]
                data[4] = input(f"Enter new year ({data[4]}): ") or data[4]
                data[5] = input(f"Enter new email ({data[5]}): ") or data[5]
                data[6] = input(f"Enter new contact ({data[6]}): ") or data[6]
                print("\nProfile updated successfully!\n")
            updated_lines.append("|".join(data))

    with open("users.txt", "w") as f:
        for line in updated_lines:
            f.write(line + "\n")


# ---------- LOGOUT ----------
def logout():
    global logged_user, logged_role
    if logged_user:
        print(f"\n{logged_user} logged out successfully.\n")
        logged_user = None
        logged_role = None
    else:
        print("No user logged in.\n")


# ---------- QUIZ DATA ----------
quiz_data = {
    "DSA": [
        ("Which uses LIFO?", ["Queue", "Stack", "Tree", "Graph"], "Stack"),
        ("Which is FIFO?", ["Queue", "Stack", "Heap", "Tree"], "Queue"),
        ("Binary search complexity?", ["O(n)", "O(log n)", "O(n^2)", "O(1)"], "O(log n)"),
        ("Not linear?", ["Array", "Queue", "Tree", "Stack"], "Tree"),
        ("Fastest average sort?", ["Bubble", "Quick", "Selection", "Merge"], "Quick")
    ],
    "DBMS": [
        ("Command to retrieve data?", ["SELECT", "INSERT", "UPDATE", "DELETE"], "SELECT"),
        ("Removes all rows?", ["DROP", "DELETE", "TRUNCATE", "CLEAR"], "TRUNCATE"),
        ("Uniquely identifies record?", ["Foreign", "Primary", "Candidate", "Alternate"], "Primary"),
        ("Removes transitive dependency?", ["1NF", "2NF", "3NF", "BCNF"], "3NF"),
        ("Which is DDL?", ["CREATE", "UPDATE", "INSERT", "DELETE"], "CREATE")
    ],
    "PYTHON": [
        ("Keyword for function?", ["fun", "def", "function", "define"], "def"),
        ("Immutable type?", ["List", "Set", "Tuple", "Dict"], "Tuple"),
        ("Output of 3*'2'?", ["6", "222", "32", "Error"], "222"),
        ("Comment symbol?", ["//", "#", "/*", "<!"], "#"),
        ("Random module name?", ["math", "random", "os", "sys"], "random")
    ]
}


# ---------- ATTEMPT QUIZ ----------
def attempt_quiz():
    if not logged_user:
        print("Please login first!\n")
        return

    print("\nCategories: DSA | DBMS | PYTHON")
    category = input("Choose category: ").upper()
    if category not in quiz_data:
        print("Invalid category!\n")
        return

    questions = random.sample(quiz_data[category], len(quiz_data[category]))
    score = 0
    total = len(questions)

    for i, (q, opts, ans) in enumerate(questions, 1):
        print(f"\nQ{i}. {q}")
        for j, opt in enumerate(opts, 1):
            print(f"   {j}. {opt}")
        choice = input("Your answer (1-4): ")
        if choice.isdigit() and 1 <= int(choice) <= 4:
            if opts[int(choice) - 1] == ans:
                score += 1

    print(f"\nQuiz completed! Your score: {score}/{total}\n")

    with open("scores.txt", "a") as f:
        f.write(f"{logged_user}|{category}|{score}/{total}|{datetime.now()}\n")


# ---------- VIEW SCORES ----------
def view_scores():
    if not logged_user:
        print("Please login first!\n")
        return

    print("\n--- Your Quiz Scores ---")
    found = False
    with open("scores.txt", "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == logged_user:
                print(f"{data[1]}: {data[2]} on {data[3]}")
                found = True
    if not found:
        print("No quiz attempted yet.\n")


# ---------- MAIN ----------
def main():
    while True:
        print("\n========= QUIZ SYSTEM =========")
        print("1. Register")
        print("2. Login")
        print("3. Show Profile")
        print("4. Update Profile")
        print("5. Attempt Quiz")
        print("6. View Scores")
        print("7. Logout")
        print("8. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            show_profile()
        elif choice == '4':
            update_profile()
        elif choice == '5':
            attempt_quiz()
        elif choice == '6':
            view_scores()
        elif choice == '7':
            logout()
        elif choice == '8':
            print("\nThank you for using the Quiz System!\n")
            break
        else:
            print("Invalid choice!\n")


# Create necessary files if not exist
open("users.txt", "a").close()
open("scores.txt", "a").close()

if __name__ == "__main__":
    main()
