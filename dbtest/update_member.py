import db.dao as dao

id = input('id >> ') #조건
pw = input('pw >> ') #값변경
tel = input('tel >> ') #값변경

# 값을 전달할 때 묶어서 보내는 역할의 클래스(data transfer object, DTO, value Object, VO)
# list!!!
vo = list()
vo.append(id)
vo.append(pw)
# vo.append(name)
vo.append(tel)

dao.update(vo)
print('---------')

