import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

sg.theme("DarkBlue")


clock = sg.Text(" ", key = "clock")
# label within the window
label = sg.Text("Type in a to-do")
# input box created
input_box = sg.InputText(tooltip="Enter todo",key="todo")
# button created
add_button = sg.Button(size = 2, image_source="add.png",mouseover_colors= "LightBlue", tooltip="Add Todo",key = "Add")

list_box = sg.Listbox(values=functions.get_todos(), key= "todos",
                        enable_events = True, size = [45,10])

edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source = "complete.png",size=10)
exit_button = sg.Button("Exit")

window = sg.Window('My To-do App',layout=[[clock],[label],[input_box, add_button],[list_box,edit_button,complete_button], [exit_button]], font =('Helvetica',20))

while True:
    #displays window 
    event,values = window.read(timeout=200)
    window["clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values["todo"] + "\n"
        todos.append(new_todo)
        window['todos'].update(values=todos)
        functions.write_todos(todos)

    if event == "Edit":
        try:
            todo_to_edit = values["todos"][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values = todos)
        
        except IndexError:
            sg.popup("Please select an item first!", font = ("Helvetica", 20))

    if event == "Complete":
        try:
            todos = functions.get_todos()
            todo_to_complete = values["todos"][0]
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values = todos)
            window["todo"].update(" ")
        
        except IndexError:
            sg.popup("Please select an item first!", font = ("Helvetica", 20))
    
    if event == "Exit":
        break

    if event == "todos":
       window['todo'].update(value=values['todos'][0]) 
    if sg.WIN_CLOSED:
        break

#exits the program
window.close()