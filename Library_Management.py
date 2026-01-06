library = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter published year: ")

    book = {
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }

    library.append(book)
    print("Book added successfully!")
    print()

def remove_book():
    title = input("Enter book title to remove: ")

    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed.")
            print()
            return

    print("Book not found.")
    print()

def issue_book():
    title = input("Enter book title to issue: ")

    for book in library:
        if book["title"].lower() == title.lower():
            if book["available"]:
                book["available"] = False
                print("Book issued!")
            else:
                print("Book already issued.")
            print()
            return

    print("Book not found.")
    print()

def return_book():
    title = input("Enter book title to return: ")

    for book in library:
        if book["title"].lower() == title.lower():
            book["available"] = True
            print("Book returned.")
            print()
            return

    print("Book not found.")
    print()

def search_book():
    title = input("Enter book title to search: ")
    found = False

    for book in library:
        if title.lower() in book["title"].lower():
            status = "Available" if book["available"] else "Issued"
            print(book["title"], "-", book["author"], "-", book["year"], "-", status)
            found = True

    if not found:
        print("No matching book found.")

    print()

def display_books():
    if len(library) == 0:
        print("Library is empty.")
        print()
        return

    print("----- Library Books -----")

    for book in library:
        status = "Available" if book["available"] else "Issued"
        print(book["title"], "|", book["author"], "|", book["year"], "|", status)

    print()

def menu():
    while True:
        print("========== LIBRARY MENU ==========")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Display Books")
        print("7. Exit")

        choice = input("Enter choice: ")
        print()

        if choice == "1":
            add_book()

        elif choice == "2":
            remove_book()

        elif choice == "3":
            search_book()

        elif choice == "4":
            issue_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            display_books()

        elif choice == "7":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice.")
            print()

menu()
