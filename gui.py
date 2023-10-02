import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('lis.txt'):
    with open('lis.txt', 'w')as file:
        pass

sg.theme('Black')
clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.lis_todo(), key='todos',
                         enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
remove = sg.Button("Remove")
ex_it = sg.Button("Exit", size=10)

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, remove,],
                           [ex_it]],
                   font=('Helvetica', 15))
while True:
    event, value = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b%d,%Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.lis_todo()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_lis(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todos_to_edit = value['todos'][0]
                new_todo = value['todo']

                todos = functions.lis_todo()
                index = todos.index(todos_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_lis(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first!", font=("Helvitca", 20))
        case 'Remove':
            try:
                to_do_remove = value['todos'][0]
                todos = functions.lis_todo()
                todos.remove(to_do_remove)
                functions.write_lis(todos)
                window['todos'].update(values=todos)
                window['todo'].update("")
            except IndexError:
                sg.popup("Please select an item first!", font=('Helvitca', 20))
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case 'Exit':
            exit()
        case sg.WIN_CLOSED:
            break
window.close()

