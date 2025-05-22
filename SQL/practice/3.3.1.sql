SELECT name
FROM Customer
WHERE custid IN (
    SELECT custid
    FROM Orders
    WHERE bookid IN (
        SELECT bookid
        FROM Book
        WHERE publisher IN (
            SELECT publisher
            FROM Book
            WHERE bookid IN (
                SELECT bookid
                FROM Orders
                WHERE Orders.custid =(
                    SELECT Customer.custid
                    FROM Customer
                    WHERE Customer.name = '¹ÚÁö¼º'
                )
            )
        )
    )
)