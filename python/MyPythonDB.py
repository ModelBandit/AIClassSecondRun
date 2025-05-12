import oracledb as cx_Oracle

class BookList:
    def __init__(self):
        lib_Dir = "C:\\PythonLib\\instantclient_19_25"
        cx_Oracle.init_oracle_client(lib_dir=lib_Dir)

        self.dsn = cx_Oracle.makedsn("localhost", 1521, sid="xe")
        self.user = "scott"
        self.pwd = "tiger"

        try:
            print("연결 준비")
            self.connection = cx_Oracle.connect(user=self.user, password=self.pwd, dsn=self.dsn)
            print("Connected")
        except cx_Oracle.DatabaseError as e:
            print("Fail: ", e)
            self.connction = None

    def sql_run(self):
        if self.connection is None:
            print("펑")
            return
        
        query = "SELECT * FROM Book"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                print("no\tname\tpubli\tprice")
                for row in cursor:
                    print(f"\t{row[0]}\t{row[1]}\t{row[2]}\r{row[3]}")

                print("작업 끝")
        except cx_Oracle.DataBaseError as e:
            print("오류 : ", e)
        finally:
            if self.connection:
                self.connection.close()
                print()
# bl = BookList()
# bl.sql_run()