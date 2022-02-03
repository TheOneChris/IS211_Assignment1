
class Book:
    def __init__(self, author = " ", title = " "):
        
        self.aut = author
        
        self.tit = title
        
        return
    
    def display(self):
        
        print (self.aut, "writen by", self.tit)
        
        return
    
    
if __name__ == "__main__":
    book1 = Book('Of Mice and Men', 'John Steinbeck')
    book2 = Book('To Kill a Mockingbird', 'Harper Lee')
    
    book1.display()
    book2.display()