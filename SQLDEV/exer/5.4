CREATE OR REPLACE PROCEDURE Interest /* 생성하거나 재구성하는 프로시저(함수) */
AS
    myInterest NUMERIC; /*ANSI 표준 스타일 NUMBER*/
    Price NUMERIC;
    CURSOR InterestCursor IS SELECT saleprice FROM Orders;/* CURSOR를 받아서 Orders의 첫번째 튜플의 saleprice를 가르킴 */
BEGIN
    myInterest := 0.0;
    OPEN InterestCursor;/*포인터에 지정대상 읽음*/
    LOOP
        FETCH InterestCursor INTO Price; /*지정된 행을 Price에 넣음*/
        EXIT WHEN InterestCursor%NOTFOUND; /*if cursor가 가져올게 없다면 break*/
        IF Price >= 30000 THEN /*IF ~ THEN이 한 세트*/
            myInterest := myInterest + Price * 0.1;
        ELSE
            myInterest := myInterest + Price * 0.05;
        END IF;
    END LOOP;
    CLOSE InterestCursor;/*커서 반환*/
    DBMS_OUTPUT.PUT_LINE('전체 이익 금액 = ' || myInterest);
END;
/
SET SERVEROUTPUT ON;
EXEC Interest;