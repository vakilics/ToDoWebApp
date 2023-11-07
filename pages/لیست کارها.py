import streamlit as st

import functions

todos = functions.get_todos()

st.set_page_config(layout="wide") #to resize in browser
st.markdown("""
<style>
input, text, .rtl {
  unicode-bidi:bidi-override;
  direction: RTL;
}
</style>
    """, unsafe_allow_html=True)

def add_todo():
    todo = st.session_state["my_new_todo"] + "\n"
    #print(todo)
    todos.append(todo)
    functions.write_todos(todos)

st.markdown("<h1 style='text-align: center; color: green;'>"
            "به برنامه یاد داشت کارها خوش آمدید!"
            "</h1>", unsafe_allow_html=True)
st.subheader(":کار های من")
for index, todo in enumerate(todos):
    #st.checkbox(todo, key=todo) #will show each checkbox status
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:   #means: if checkbox is checked/ticked
        #print(checkbox)
        todos.pop(index)
        functions.write_todos(todos) #again write the updated todos without the removed todo.
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add To-DO!", placeholder="کار جدید ...", on_change=add_todo, key='my_new_todo')

#print("End of App!")
st.session_state