SELECT name, COUNT(publisher)
FROM Orders, Customer, Book
WHERE Orders.custid = Customer.custid AND Orders.bookid = Book.bookid
GROUP BY name
HAVING COUNT(DISTINCT publisher) >= 2;