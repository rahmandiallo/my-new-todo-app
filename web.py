import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This my todo app!")
st.write("This app is to increase your productivity!")


for todo in todos:
    st.checkbox(todo)


st.text_input(label = "Enter A Todo:",placeholder = "Add New Todo")

print("Hello")