import streamlit as st
import functions as func

# FILEPATH = r'C:\Users\user\PycharmProjects\pythonProject\web_app\webtodos.txt'


def add_todo():
    new_todo = st.session_state['new_todo']
    todos_list = func.get_todos()
    todos_list.append(new_todo + '\n')
    func.write_todos(todos_list)
    st.session_state['new_todo'] = ""


todos = func.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input(label="", placeholder="Add new todo...", on_change=add_todo,
              key='new_todo')

# st.session_state
