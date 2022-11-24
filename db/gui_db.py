from tkinter import *

def file_write():
    file = open('diary.txt', 'w')
    item = '날짜: '+date_text.get()+'\n'+'제목: '+title_text.get()+'\n'+'내용: '+content_text.get()
    file.write(item)
    file.close()
def file_read():
    file2 = open('diary.txt', 'r')
    for i in range(3):
        row = file2.readline()
        print(row)
    file2.close()

w = Tk()
w.geometry('500x600')
w.config(bg='lightgray')

icon=PhotoImage(file='../db_test/car.png')
dogLabel=Label(w,image=icon)
dogLabel.pack()

date_label = Label(w,text='날짜 입력',font=('맑은 고딕',20),bg='lightgray',fg='blue')
date_label.pack()

date_text=Entry(w,font=('맑은 고딕',20),bg='yellow',fg='red')
date_text.pack()

title_label = Label(w,text='제목 입력',font=('맑은 고딕',20),bg='lightgray',fg='blue')
title_label.pack()

title_text=Entry(w,font=('맑은 고딕',20),bg='yellow',fg='red')
title_text.pack()

content_label = Label(w,text='내용 입력',font=('맑은 고딕',20),bg='lightgray',fg='blue')
content_label.pack()

content_text=Entry(w,font=('맑은 고딕',20),bg='yellow',fg='red')
content_text.pack()

button = Button(w,width=30,height=3,bg='green',font=('맑은 고딕',10),text='db로 저장',command=file_write)
button.pack()

button2 = Button(w,width=30,height=3,bg='green',font=('맑은 고딕',10),text='db로 읽기',command=file_read)
button2.pack()

w.mainloop()