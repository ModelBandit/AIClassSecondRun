CREATE OR REPLACE PROCEDURE BookInsertOrUpdate(
    myBookID NUMBER,
    myBookName VARCHAR2,
    myPublisher VARCHAR2,
    myPrice INT
)
AS
    mycount NUMBER;

BEGIN
    SELECT count(*) INTO mycount FROM Book /*Book���� mycount�� Ʃ�û����� �޾ƿ�*/
    WHERE bookname LIKE myBookName; /*bookname�� ���� �ִ� myBookName�� ������ Ȯ��*/
    /*���� �ִ� �̸��� ���� å�� �ִ��� Ȯ��*/
    
    IF mycount != 0 THEN/*����*/
        UPDATE Book SET price = myPrice
        WHERE bookname LIKE myBookName;
    ELSE/*����*/
        INSERT INTO Book(bookid, bookname, publisher, price)
        VALUES(myBookID, myBookName, myPublisher, myPrice);
    END IF;
END;
/

EXEC BookInsertOrUpdate(15, '������ ��ſ�', '������м���', 25000);
SELECT * FROM Book;
/
EXEC BookInsertOrUpdate(24, '������ ��ſ�', '�Ƶ�����', 20000);
SELECT * FROM Book;
            