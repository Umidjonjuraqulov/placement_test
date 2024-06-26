import streamlit as st
import pandas as pd

from data import *

def main():
    st.set_page_config(page_title='Dream School Test', layout='wide')

    st.header("English Placement Test")

    data = read_test()
    number_questions = len(data)

    for i in range(number_questions+10):
        st.sidebar.button(f"Question {i+1}", use_container_width=True, type="primary")

    container = st.container(border=True)
    question = "Which of the following is a correct example of the past perfect tense?"
    options = ["A) She was cooking dinner when the phone rang.",
               "B) They have already left for the airport.",
               "C) He will finish the project by tomorrow.",
               "D) I had never seen that movie before last night."]


    selection = container.radio(f"***{question}***", options)


if __name__ == '__main__':
    main()