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
 
              
       
       
       
       
       



       
       
