CREATE OR REPLACE PROCEDURE BookInsertOrUpdate(
    myBookID NUMBER,
    myBookName VARCHAR2,
    myPublisher VARCHAR2,
    myPrice INT
)
AS
    mycount NUMBER;

BEGIN
    SELECT count(*) INTO mycount FROM Book /*Book에서 mycount로 튜플사이즈 받아옴*/
    WHERE bookname LIKE myBookName; /*bookname이 새로 넣는 myBookName과 같은지 확인*/
    /*새로 넣는 이름과 같은 책이 있는지 확인*/
    
    IF mycount != 0 THEN/*있음*/
        UPDATE Book SET price = myPrice
        WHERE bookname LIKE myBookName;
    ELSE/*음슴*/
        INSERT INTO Book(bookid, bookname, publisher, price)
        VALUES(myBookID, myBookName, myPublisher, myPrice);
    END IF;
END;
/

EXEC BookInsertOrUpdate(15, '스포츠 즐거움', '마당과학서적', 25000);
SELECT * FROM Book;
/
EXEC BookInsertOrUpdate(24, '스포츠 즐거움', '아동서적', 20000);
SELECT * FROM Book;
            