INSERT INTO Book
VALUES(11,'������ ����','���ѹ̵��', 10000);

DELETE FROM Book WHERE publisher = '�Ｚ��';

DELETE FROM Book WHERE publisher = '�̻�̵��';/* Orders���� id�� ������ */

UPDATE Book
SET publisher = '�������ǻ�'
WHERE publisher = '���ѹ̵��';

CREATE TABLE Bookcompany(
    name VARCHAR2(20) PRIMARY KEY,
    address VARCHAR2(20),
    begin DATE
);

ALTER TABLE Bookcompany ADD WebAddress VARCHAR2(30);

INSERT INTO Bookcompany VALUES('�Ѻ���ī����', '���� ������', TO_DATE('1993 01 01','yyyy mm dd'), 'http://hanbit.co.kr');