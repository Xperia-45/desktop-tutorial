


class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, title, author):
        book = {"title": title, "author": author, "checked_out": False}
        self.books.append(book)
        print(f'Added "{title}" by {author}.')

    def view_books(self):
        if not self.books:
            print("The library has no books yet.")
            return
        print("--- All Books ---")
        for i, book in enumerate(self.books, start=1):
            status = "Checked out" if book["checked_out"] else "Available"
            print(f'{i}. "{book["title"]}" by {book["author"]} — {status}')

    def _find_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                return book
        return None

    def checkout_book(self, title):
        book = self._find_book(title)
        if book is None:
            print(f'No book found with the title "{title}".')
            return
        if book["checked_out"]:
            print(f'"{book["title"]}" is already checked out.')
            return
        book["checked_out"] = True
        print(f'You checked out "{book["title"]}". Enjoy!')

    def return_book(self, title):
        book = self._find_book(title)
        if book is None:
            print(f'No book found with the title "{title}".')
            return
        if not book["checked_out"]:
            print(f'"{book["title"]}" was not checked out.')
            return
        book["checked_out"] = False
        print(f'You returned "{book["title"]}". Thanks!')

    def search_book(self, keyword):
        keyword = keyword.lower()
        matches = [b for b in self.books if keyword in b["title"].lower()]
        if not matches:
            print(f'No books matched "{keyword}".')
            return
        print(f'--- Search results for "{keyword}" ---')
        for book in matches:
            status = "Checked out" if book["checked_out"] else "Available"
            print(f'"{book["title"]}" by {book["author"]} — {status}')


def main():
    library = Library()

    menu = """
1. Add a book
2. View all books
3. Check out a book
4. Return a book
5. Search for a book
6. Exit
"""

    print("=== Welcome to Library Book Tracker ===")

    while True:
        print(menu)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            title = input("Book title: ").strip()
            author = input("Author: ").strip()
            library.add_book(title, author)
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            title = input("Title to check out: ").strip()
            library.checkout_book(title)
        elif choice == "4":
            title = input("Title to return: ").strip()
            library.return_book(title)
        elif choice == "5":
            keyword = input("Search keyword: ").strip()
            library.search_book(keyword)
        elif choice == "6":
            print("Goodbye! Happy reading.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()