import pymysql

class DAO:
    cur = None
    conn = None

    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='1234',
                               db='cloth',
                               charset='utf8')
        print('1. db연결 성공', self.conn)

        self.cur = self.conn.cursor()

    # def create(id, pw, name, tel):
    def create(self, vo):
        sql = "insert into member values (%s, %s, %s, %s)"
        result = self.cur.execute(sql, vo)
        print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)

        self.conn.commit()
        self.conn.close()

    def update(self, vo):
        sql = "update member set tel = %s, pw = %s where id = %s"
        result = self.cur.execute(sql, vo)
        print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)

        self.conn.commit()
        self.conn.close()

    def delete(self, vo):
        sql = "delete from member where id = %s"
        result = self.cur.execute(sql, vo)
        print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)

        self.conn.commit()
        self.conn.close()

    def read(self, id):
        sql = "select * from member where id = %s"
        result = self.cur.execute(sql, id)

        row = self.cur.fetchone()
        print(row)
        print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)

        self.conn.commit()
        self.conn.close()
        return row #('apple', 'apple', 'apple', 'apple')


    def all(self):
        sql = "select * from member"
        result = self.cur.execute(sql)

        rows = self.cur.fetchall()
        print(len(rows))
        print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)
        print(rows)
        self.conn.commit()
        self.conn.close()
        return rows #(('apple', 'apple', 'apple', 'apple'), (),())

# 해당 모듈이 main되어서 실행될 때만, 실행해 주는 부분..!
if __name__ == '__main__':
    dao = DAO()
    dao.create(['apple4','apple','apple','apple'])
