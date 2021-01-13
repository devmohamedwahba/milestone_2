from utils import database

USER_CHOICE = """
Enter :
- 'a' to add new book
- 'l' to list all books
- 'r' to mark book as read
- 'd' to delete book
- 'q' to quit

Your choice: """


def menu():
    user_input = input(USER_CHOICE)
    print(user_input)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command")
        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input('Enter new book name: ')
    author = input('Enter the new book author')
    database.add_book(name=name, author=author)


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read} ")


def prompt_read_book():
    name = input('Enter the name of the book that you finish: ')
    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the name of book to delete: ')
    database.delete_book(name)


menu()