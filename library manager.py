class library: 
    def __init__(self):
        self.books=[]

    def add_book(self,title,author):
        book = {"title":"title" , "author":"author"} 
        self.books.append(book)
        print(f"books added {title} of author {author}")

    def view_book(self):
        


title=input("enter the name of book:")
author=input("enter the name of author:")
lib=library()
lib.add_book(title,author)


       
       
