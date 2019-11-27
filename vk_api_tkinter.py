import requests as rq
import sys
import vk_requests as vkr
import tkinter as tk
import time
import os
import datetime
from PIL import ImageTk, Image
from tkinter import messagebox
import vkapi_helper as vkh

fields = ['has_mobile', 'photo_big', 'city', 'bdate', 'connections', 'home_town', 'photo_400_orig']

login = '89992948531'
password = 'baron070981'
apiid = 7211649

root = vkh.CreateMainWindow(flag = True)
widget = vkh.CreateMyWidgets(root)
widget.position_widgets(root)
root.create_subwindow()

login, password, apiid = vkh.load_user_data('data_user.txt')

api = vkh.ApiHelper(apiid, login, password)

def processing(event):
    widget.get_text_from_entry()
    img_file = vkh.LoaderImg(widget.datainput['path'])
    api.set_request_parameters(fields = fields, q = widget.datainput['q'],
                                hometown = widget.datainput['city'], cnt = widget.datainput['count'])
    api.get_dict_api()
    data_dict = api.data_dict
    time.sleep(1.3)
    widget.set_count_text(api.count_humans)
    widget.active_button(False)
    for data in data_dict:
        info = img_file.load_img(data_dict[data][0], 'jpg', data )
        widget.set_text(info[0])
        root.update()
        root.update_subwindow(info[1], data_dict[data][1])
        if not widget.load_bool:
            del_info = img_file.delete_img(info[1])
            print(del_info)
        else:
            print(info[0])
        time.sleep(.850)
    widget.active_button(state = True)


widget.click_search(processing)












root.mainloop()








