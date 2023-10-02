import streamlit as st
import functions

todos = functions.lis_todo()
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_lis(todos)

st.title("My To-Do App")
st.subheader("This is my todo app")
st.write("This app is use to increase your productivity")

todos = functions.lis_todo()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_lis(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Enter todo",
              on_change=add_todo, key='new_todo')