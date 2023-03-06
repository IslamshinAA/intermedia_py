import db, gui
from datetime import datetime


def button_click():
    a = gui.Choice()
    if (a == 1):
        id = gui.id_input()
        name = gui.Name_input()
        description = gui.Description_input()
        print("Данные запишутся в json формате:")
        current_datetime = str(datetime.now())
        db.Saving_json(id, name, description, current_datetime)
    elif (a == 2):
        db.get_base_json_names()
    elif (a == 3):
        print("Введите id заметки, которую хотите прочитать")
        id_found = int(input())
        db.get_base_json_description(id_found)
    elif (a == 4):
        print("Введите id заметки, которую хотите редактировать")
        id_found = int(input())
        db.editing_json(id_found)
    elif (a == 5):
        print("Введите id заметки, которую хотите удалить")
        id_found = int(input())
        db.deleting_json(id_found)


