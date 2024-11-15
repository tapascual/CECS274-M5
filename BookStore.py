import Book
import ArrayList
# import ArrayQueue
import RandomQueue
import DLList
# import SLLQueue
import MaxQueue
import ChainedHashTable
import BinarySearchTree
# import BinaryHeap
# import AdjacencyList
import time


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.bookCatalog = None # DDList
        self.shoppingCart = MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()
        # will hold object Book and compare by rank with highest rank being best seller?
        # self.shoppingCart = ArrayQueue.ArrayQueue()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = DLList.DLList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                self.bookIndices.add(key, self.bookCatalog.size()-1)
                self.sortedTitleIndices.add(key, self.bookCatalog.size()-1)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")


    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")


    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = MaxQueue.MaxQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")


    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")


    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise, it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")


    def searchBookByInfix(self, infix: str, cnt: int = 15) -> None:
        '''
        searchBookByInfix: Search all the books that contains infix
        input and print the first cnt that match:
            infix: A string
            cnt: An int
        '''

        start_time = time.time()

        if self.bookCatalog is None:
            print("No books are loaded. Load a book catalog to search")
            return


        res = ArrayList.ArrayList()
        books_found = 0
        for book in self.bookCatalog:
            if infix in book.title:
                res.append(book)
                books_found += 1
                if books_found == cnt:
                    break
        for b in res:
            print(b)

        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")


    def getCartBestSeller(self) -> None:

        """
            getCartBestSeller: prints the title of the book
            with the most sales in the user's cart
        """

        start_time = time.time()

        best_seller = self.shoppingCart.max()

        elapsed_time = time.time() - start_time

        print(f"getCartBestSeller returned \n{best_seller.title} \nCompleted in {elapsed_time} seconds")
        # return best_seller.title


    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")
            
    
    def addBookByKey(self, key: object):
        start_time = time.time()
        
        # Find the book at the given key
        book = self.bookIndices.find(key)
        
        # Verifies if there is a book stored with the given key
        if book is not None:
            self.shoppingCart.add(self.bookCatalog.get(book))   # Adds the book to the shopping cart
            print(f"Added title: {self.bookCatalog.get(book).title}")   # Prints the book title after added to shopping cart
            
        else:   # If there is not book stored with the given key
            print("Book not found.")
            
        elapsed_time = time.time() - start_time
        
        # Print the line given in project directions
        print(f"addBookByKey Completed in {elapsed_time} seconds")
        
    
    def addBookByPrefix(self, prefix):
        """
        Add first matched book containing prefix in the title
        Returns 'None' if no book is matched
        """
        book = self.sortedTitleIndices.findKeyOrSmallest(prefix)
        
        if book.k[0:len(prefix)] == prefix and len(prefix) > 0:
            self.shoppingCart.add(self.bookCatalog.get(book.v))
            print(f'Added first matched title: {book.k}')
        
        else:
            print('Error: Prefix was not found.')
        
            
        