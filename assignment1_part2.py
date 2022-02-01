
class Book:
    def __init__(self, author = " ", title = " "):
        
        self.aut = author
        
        self.tit = title
        
        return
    
    def display(self):
        
        print (self.aut, "writen by", self.tit)
        
        return
        book1 = Book('Of Mice and Men', 'John Steinbeck')
        book2 = Book('To Kill a Mockingbird', 'Harper Lee')
        
        "TEST COMMANDS = book1.display() and book2.display()"
        
        







