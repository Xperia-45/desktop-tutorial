class library:
       def __init__(self):
              self.books = []
       def add_book(self,title,author):
              books = {"title":title , "author" : author , checked_out:False}
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



              
 
              
       
       
       
       
       



       
       
