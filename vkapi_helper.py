import requests as rq
import sys
import vk_requests as vkr
import tkinter as tk
import time
import os
import datetime
from PIL import ImageTk, Image
from tkinter import messagebox

login = '0000000000' # номер телефона, строка
password = 'xxxxxxxxxx' # password, строка
apiid = 0 # apiid приложения, число
m = 0

class CreateMainWindow(tk.Tk):

    def __init__(self, title = 'CreateMainWindow object', w = '200',
                 h = '200', x = '10', y = '10', flag = True, screen = False):
        super(CreateMainWindow, self).__init__()
        self.width_win = self.winfo_screenwidth()
        self.height_win = self.winfo_screenheight()
        self.img_obj = None

        if flag == False and screen == False:
            sizestr = str(w)+'x'+str(h)+'+'+str(x)+'+'+str(y)
            self.geometry(sizestr)
        elif flag == False and screen == True:
            sizestr = str(self.width_win)+'x'+str(self.height_win)+'+'+str(x)+'+'+str(y)
            self.geometry(sizestr)

        self.title(title)
        self.file_list = []


    def create_subwindow(self, title = 'SubWindow', width = 200, height = 200):
        self.child = tk.Toplevel()
        self.child.title(title)
        #self.child.minsize(width=width, height=height)
        self.panel = tk.Label(self.child)
        self.panel2 = tk.Label(self.child, fg = 'red', bg = 'blue', font='Times 30')
        self.panel.pack()
        self.panel2.pack(fill = tk.X)
        return self.child


    def update_subwindow(self, file_path, text):
        self.img_obj = ImageTk.PhotoImage(Image.open(file_path))
        self.panel.configure(image = self.img_obj)
        self.panel2.configure(text = text)
        self.panel.image = self.img_obj
        self.panel2.text = text



class CreateMyWidgets:

    def __init__(self, root):
        self.root = root
        self.datainput = dict()
        self.subwindow_objects = []
        self.IntVar = tk.IntVar()
        self.load_bool = False
        self.state_test = True

        self.entry_log = tk.Entry(root, fg='red', bg = 'green')     # ввод логина
        self.entry_pas = tk.Entry(root, fg='red', bg = 'green')     # ввод пароля
        self.entry_q = tk.Entry(root, fg='#2087F6')       # запрос
        self.entry_city = tk.Entry(root)    # город(родной)
        self.entry_findall = tk.Entry(root, fg = 'red')   # дата рождения
        self.entry_count = tk.Entry(root, fg='#2087F6')   # число поиска
        self.entry_path = tk.Entry(root, fg = 'blue')

        self.entry_log.insert(0, '89992948531')
        self.entry_pas.insert(0, 'baron070981')
        self.entry_q.insert(0, 'Дмитрий')
        self.entry_count.insert(0, '10')
        self.entry_path.insert(0, 'folder_loader_img')

        self.label_log = tk.Label(root, text = 'логин:', anchor = tk.E)
        self.label_pas = tk.Label(root, text = 'пароль:', anchor = tk.E)
        self.label_q = tk.Label(root, text = 'запрос:', anchor = tk.E)
        self.label_city = tk.Label(root, text = 'город:', anchor = tk.E)
        self.label_findall = tk.Label(root, text = 'Найдено:', anchor = tk.E, fg = 'red')
        self.label_count = tk.Label(root, text = 'Число поиска:', anchor = tk.E)
        self.spin_age_from = tk.Spinbox(root, width = 5, from_ = 14, to = 99) # возраст от
        self.spin_age_to = tk.Spinbox(root, width = 5, from_ = 14, to = 99)   # возраст до
        self.label_age_from = tk.Label(root, text = 'Возраст от:', anchor = tk.E)
        self.label_age_to = tk.Label(root, text = 'до:', anchor = tk.E)
        self.label_path = tk.Label(root, text = 'путь сохранения:')
        self.btn_search = tk.Button(root, text='Начать поиск', bg='#2AD4EB', fg='#EDF0C4') # старт поиска
        self.check_load_state = tk.Checkbutton(root, text = 'с сохранением', variable = self.IntVar,
                                               onvalue = 1, offvalue = 0, command = self.set_state_load)

        self.spin_age_to.delete(0, tk.END)
        self.spin_age_to.insert(tk.END,'99')
        self.position_widgets( self.root )


    def position_widgets(self, root):
        self.label_log.grid(column = 0, row = 0, sticky = tk.N + tk.S + tk.W + tk.E, pady = 1)
        self.entry_log.grid(column = 1, row = 0, sticky = tk.N + tk.S + tk.W + tk.E, padx = 2, pady = 3)

        self.label_pas.grid(column = 2, row = 0, sticky = tk.N + tk.S + tk.W + tk.E, pady = 1)
        self.entry_pas.grid(column = 3, row = 0, sticky = tk.N + tk.S + tk.W + tk.E, padx = 2, pady = 3)

        self.label_q.grid(column = 0, row = 1, sticky = tk.N + tk.S + tk.W + tk.E, pady = 1)
        self.entry_q.grid(column = 1, row = 1, columnspan = 3, sticky = tk.N + tk.S + tk.W + tk.E, padx = 2, pady = 1)

        self.label_city.grid(column = 0, row = 2, sticky = tk.N + tk.S + tk.W + tk.E, pady = 1)
        self.entry_city.grid(column = 1, row = 2, columnspan = 3, sticky = tk.N + tk.S + tk.W + tk.E, padx = 2, pady = 3)

        self.label_age_from.grid(column = 0, row = 3, sticky = tk.N + tk.S + tk.W + tk.E, pady = 1)
        self.spin_age_from.grid(column = 1, row = 3, sticky = tk.N + tk.S + tk.W + tk.E, padx = 2, pady = 3)

        self.label_age_to.grid(column = 2, row = 3, sticky = tk.N + tk.S + tk.W + tk.E, pady = 1)
        self.spin_age_to.grid(column = 3, row = 3, sticky = tk.N + tk.S + tk.W + tk.E, padx = 2, pady = 3)

        self.label_findall.grid(column = 0, row = 4, sticky = tk.N + tk.S + tk.W + tk.E, pady = 1)
        self.entry_findall.grid(column = 1, row = 4, sticky = tk.N + tk.S + tk.W + tk.E, padx = 2, pady = 3)

        self.label_count.grid(column = 2, row = 4, sticky = tk.N + tk.S + tk.W + tk.E, pady = 1)
        self.entry_count.grid(column = 3, row = 4, sticky = tk.N + tk.S + tk.W + tk.E, padx = 2, pady = 3)

        self.label_path.grid(column = 0, row = 5, sticky = tk.N + tk.S + tk.W + tk.E, pady = 1)
        self.entry_path.grid(column= 1, row = 5, columnspan = 3, sticky = tk.N + tk.S + tk.W + tk.E, padx = 2, pady = 3)

        self.btn_search.grid(column = 1, columnspan = 2, row = 6, sticky = tk.N + tk.S + tk.W + tk.E, pady = 3)

        self.check_load_state.grid(column = 3, row = 6)

        self.frm = tk.Frame(root)
        self.frm.grid(column = 0, row = 7, columnspan = 4, sticky = tk.N + tk.S + tk.W + tk.E, padx = 2, pady = 3)

        self.text_space = tk.Text(self.frm, bg = 'black', fg = '#86FF00', insertbackground='#FFFFFF') # текстовое поле для вывода инфо
        self.text_space.pack(side = tk.LEFT)
        scroll = tk.Scrollbar( self.frm, command = self.text_space.yview ) # скрол для текстового поля
        scroll.pack(side = tk.RIGHT, fill = tk.Y)
        self.entry_pas.config(show = '*')


    def click_search(self, foo):
        self.btn_search.bind('<Button-1>', foo)


    def set_text(self, text):
        text = text+'\n'
        self.text_space.insert(1.0, text)


    def set_count_text(self, cnt:int):
        self.entry_findall.insert(0, str(cnt))


    def set_state_load(self):
        if self.IntVar.get() == 1:
            self.load_bool = True
            print(self.load_bool)
        elif self.IntVar.get() == 0:
            self.load_bool = False
            print(self.load_bool)


    def get_text_from_entry(self):
        self.datainput['q'] = self.entry_q.get()
        self.datainput['city'] = self.entry_city.get()
        try:
            self.datainput['count'] = int(self.entry_count.get())
        except:
            self.datainput['count'] = 5

        try:
            self.datainput['age_from'] = int(self.spin_age_from.get())
        except:
            self.datainput['age_from'] = 14

        try:
            self.datainput['age_to'] = int(self.spin_age_to.get())
        except:
            self.datainput['age_to'] = 99

        try:
            self.datainput['path'] = self.entry_path.get()
        except:
            self.datainput['path'] = 'folder_loader_img'




class ApiHelper:
    def __init__(self, apiid, login, password):
        self.__password = password
        self.login = login
        self.__apiid = apiid
        self.api = vkr.create_api( app_id = apiid, login = login,
                                               password = password )
        self.cnt = 1
        self.fields = []
        self.lang = 'ru'
        self.hometown = ''
        self.quert = ''
        self.count_humans = 0
        self.age_from = 14
        self.age_to = 99
        self.birth_day = 1
        self.birth_month = 1
        self.birth_year = 1900
        self.bdate = []
        self.dict_api = dict()
        self.data_list = list()
        self.data_dict = dict()


    def set_request_parameters(self, fields:list = [''], q:str = '', cnt:int = 1, hometown:str = '',
                               age_from:int = 14, age_to:int = 99, bdate:str = '' ):
        if bdate:
            self.birth_day, self.birth_month, self.birth_year = self.get_date_from_string(bdate)

        if age_from:
            if age_from >= 14 and age_from <= age_to:
                self.age_from = age_from
            else:
                self.age_from = 14

        if age_to:
            if age_to <= 99 and age_to >= age_from:
                self.age_to = age_to
            else:
                self.age_from = 99

        self.hometown = hometown
        self.quert = q
        self.fields = list(fields)
        if 'photo_big' not in self.fields:
            self.fields.append('photo_big')
        self.cnt = cnt


    def get_dict_api(self):
        self.dict_api = self.api.users.search(q = self.quert, fields = self.fields, count = self.cnt,
                                              lang = self.lang, hometown = self.hometown, age_from = self.age_from,
                                              age_to = self.age_to)
        self.count_humans = self.dict_api['count']
        for data in self.dict_api['items']:
            firstname = data['first_name']
            lastname = data['last_name']
            key = firstname+' '+lastname
            hometwn = '...'
            city = {'id':'0', 'title':'not city'}
            bdate = 'xx.xx.xxxx'
            if 'hometown' in data:
                hometwn = data['hometown']
            if 'city' in data:
                city = data['city']
            if 'bdate' in data:
                bdate = data['bdate']
            pos = data['photo_big'].find('?')
            img_link = data['photo_big'][:pos]
            lst = list()
            info_text = firstname+'\n'+lastname+'\n'+hometwn+'\n'+city['title']+'\n'+bdate
            lst.append(img_link)
            lst.append(info_text)
            self.data_dict[key] = lst


class LoaderImg:

    def __init__(self, direct:str='folder_loader_img'):
        self.direct_path = direct
        os.makedirs( direct, exist_ok = True )


    def get_filename(self, file_extension:str, *args):
        s = ''
        for data in args:
            s += str(data).strip()
        d = datetime.datetime.now()
        date_str = str(d.day) + str(d.month) + str(d.year)+str(d.hour)+str(d.minute)+str(d.second)+str(d.microsecond%1000)
        return date_str+'_'+s+'.'+file_extension


    def load_img(self, url, file_extension, *args):
        filename = self.get_filename(file_extension, *args)
        img_data = rq.get(url)
        info = ''
        filename = self.direct_path+'\\'+filename
        with open(filename, 'wb') as f:
            try:
                f.write(img_data.content)
                info = 'Download: '+filename+' succes'
            except:
                info = 'Loading error!...'
        return info, filename


    def delete_img(self, file_path):
        pass






