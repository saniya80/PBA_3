class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = float(price)

    def get_category(self):
        if self.price >= 1000:
            return "Premium"
        if self.price >= 500:
            return "Standard"
        return "Basic"

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price:.2f}")
        print(f"Category: {self.get_category()}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, price):
        self.books.append(Book(title, author, price))
        print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for i, book in enumerate(self.books, start=1):
            print(f"Book {i}:")
            book.display_info()


def main():
    library = Library()

    while True:
        print("--- Library Management System ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Display Categories")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            try:
                price = float(input("Enter Price: "))
                if price < 0:
                    print("Price cannot be negative.")
                else:
                    library.add_book(title, author, price)
            except ValueError:
                print("Invalid price.")

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            print("exit")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()


# OUTPUT:
''' Enter your choice (1-4): 1
Enter Book Title: anatomy
Enter Author Name: wiliam
Enter Price: 2400
Enter Category (Premium/Standard/Basic): Primium
Book added successfully.

 ---Library Management System ---
1. Add Book
2. Display Book Details
3. Display Book Categories
4. Exit

Enter your choice (1-4): 2
--- Library Book Details ---
Book 1:
Title: anatomy
Author: wiliam
Price: 2400.00
Category: Premium

 ---Library Management System ---
1. Add Book
2. Display Book Details
3. Display Book Categories
4. Exit
Enter your choice (1-4): 3
Exiting Library Management System. Goodbye! '''    