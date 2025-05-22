INSERT INTO Book
VALUES(11,'스포츠 세계','대한미디어', 10000);

DELETE FROM Book WHERE publisher = '삼성당';

DELETE FROM Book WHERE publisher = '이상미디어';/* Orders에서 id값 참조중 */

UPDATE Book
SET publisher = '대한출판사'
WHERE publisher = '대한미디어';

CREATE TABLE Bookcompany(
    name VARCHAR2(20) PRIMARY KEY,
    address VARCHAR2(20),
    begin DATE
);

ALTER TABLE Bookcompany ADD WebAddress VARCHAR2(30);

INSERT INTO Bookcompany VALUES('한빛아카데미', '서울 마포구', TO_DATE('1993 01 01','yyyy mm dd'), 'http://hanbit.co.kr');