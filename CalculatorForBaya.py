import streamlit as st
st.set_page_config(page_title='Calculater',
                   page_icon='💀',
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items={
                     'Get Help':'https://www.extremelycoolapp.com/help','Report a bug': "https://www.extremelycoolapp.com/bug",'About': "# This is a header. This is an *extremely* cool app!"
}
)

st.write('''
   # Calculater
''')

num1=st.number_input("Enter Value:",value= 10)
num2=st.number_input("Enter Value:",value= 5)
sel= st.selectbox(
    "What to do today?",
    ("add",'minus','divide','multiplication')
)


def calculation():
  if st.button("answer"):
    if sel == "add":
        st.markdown(num1+num2)
    elif sel == "minus":
       st.markdown(num1-num2)
    elif sel == "divide":
       st.markdown(num1/num2)
    elif sel == "multiplication":
       st.markdown(num1*num2)

calculation()