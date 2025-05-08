SELECT Book.bookname, COUNT(Orders.custid)
FROM Book, Orders
WHERE Book.bookid = Orders.bookid
GROUP BY bookname
HAVING COUNT(Orders.custid) >= 0.3 * (
    SELECT COUNT(*)
    FROM Customer
);