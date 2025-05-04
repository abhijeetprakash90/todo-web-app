import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['todo_label'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("Manage your daily todos")

#st.checkbox("Buy Grocery")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    #Used to remove item from the list
    if (checkbox):
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add a new Todo...", on_change=add_todo, key="todo_label")

st.session_state