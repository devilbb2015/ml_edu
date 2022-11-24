import pymysql

# def create(id, pw, name, tel):
def create(vo):
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='1234',
                           db='cloth',
                           charset='utf8')
    print('1. db연결 성공', conn)

    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

    # sql = "insert into member values ('" + id + "', '" + pw + "', '" +  name + "', '" + tel + "')"
    # sql = "insert into member values ('" + vo[0] + "', '" + vo[1] + "', '" +  vo[2] + "', '" + vo[3] + "')"
    sql = "insert into member values (%s, %s, %s, %s)"
    result = cur.execute(sql, vo)
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)

    conn.commit()
    conn.close()

def update(vo):
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='1234',
                           db='cloth',
                           charset='utf8')
    print('1. db연결 성공', conn)

    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

    sql = "update member set tel = %s, pw = %s where id = %s"
    result = cur.execute(sql, vo)
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)

    conn.commit()
    conn.close()

def delete(vo):
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='1234',
                           db='cloth',
                           charset='utf8')
    print('1. db연결 성공', conn)

    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)


    sql = "delete from member where id = %s"
    result = cur.execute(sql, vo)
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)

    conn.commit()
    conn.close()

def read(id):
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='1234',
                           db='cloth',
                           charset='utf8')
    print('1. db연결 성공', conn)

    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)


    sql = "select * from member where id = %s"
    result = cur.execute(sql, id)

    row = cur.fetchone()
    print(row)
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)

    conn.commit()
    conn.close()
    return row #('apple', 'apple', 'apple', 'apple')


def all():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='1234',
                           db='cloth',
                           charset='utf8')
    print('1. db연결 성공', conn)

    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)


    sql = "select * from member"
    result = cur.execute(sql)

    rows = cur.fetchall()
    print(len(rows))
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)
    print(rows)
    conn.commit()
    conn.close()
    return rows #(('apple', 'apple', 'apple', 'apple'), (),())

# 해당 모듈이 main되어서 실행될 때만, 실행해 주는 부분..!
if __name__ == '__main__':
    create('apple','apple','apple','apple')
