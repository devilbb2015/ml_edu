import db.dao as dao

id = input('id >> ')

# 값을 전달할 때 묶어서 보내는 역할의 클래스(data transfer object, DTO, value Object, VO)
# list!!!
vo = list()
vo.append(id)

dao.delete(vo)
print('---------')

