import db.dao as dao

id = input('id >> ')
pw = input('pw >> ')
name = input('name >> ')
tel = input('tel >> ')

# 값을 전달할 때 묶어서 보내는 역할의 클래스(data transfer object, DTO, value Object, VO)
# list!!!
vo = list()
vo.append(id)
vo.append(pw)
vo.append(name)
vo.append(tel)

# vo2 = [id, pw, name, tel]
# db_test.dao.create(id, pw, name, tel)
# db_test.dao.create(vo)
dao.create(vo)
print('---------')

