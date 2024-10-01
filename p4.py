class Book:
  book_count = 0

  def __init__(self,book_id,title,year,author,price,discount):
    if not(book_id[:2].isalpha() and book_id[2:].isdigit() and len(book_id) == 4):
        raise ValueError("Invalid book ID.the ID should consist of two letters followed by two digits(e.g.,'AB12').")

    self.book_id = book_id
    self.title = title
    self.year = year
    self.author = author
    self.price = price
    self.discount = discount

    Book.book_count += 1

  def total_price(self):
      return self.price - self.discount
  @classmethod
  def print_book_count(cls):
     print(f"Total books created: {cls.book_count}")
  def __str__(self):
      return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Price: {self.total_price()}"

try:
  book1 = Book("AB12", "The Great Gatsby", 1925, "F. Scott Fitzgerald", 100, 10)

  print(book1)
  book2 = Book("CD34", "1984", 1949, "George Orwell", 120, 20)
  print(book2)
  Book.print_book_count()

except ValueError as e:
  print(e)