# Program to Maintain a Library Catalogue Using Text Files

# Function to add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    with open("library.txt", "a") as file:
        file.write(title + "," + author + "\n")

    print("Book added successfully")


# Function to search for a book
def search_book():
    search = input("Enter title or author to search: ")

    with open("library.txt", "r") as file:
        found = False

        for line in file:
            title, author = line.strip().split(",")

            if search.lower() in title.lower() or search.lower() in author.lower():
                print("Title:", title, "| Author:", author)
                found = True

        if not found:
            print("Book not found")


# Function to generate reports
def report():
    with open("library.txt", "r") as file:
        books = file.readlines()

    print("Total number of books:", len(books))

    author_name = input("Enter author name for report: ")
    count = 0

    for line in books:
        title, author = line.strip().split(",")

        if author.lower() == author_name.lower():
            print("Title:", title)
            count += 1

    print("Books by this author:", count)


# Main program
while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        report()
    elif choice == "4":
        break
    else:
        print("Invalid choice")