import streamlit as st


def main():
    st.set_page_config(page_title='Dream School Test', layout='wide')

    st.header("English Placement Test")

    container = st.container()
    question = "Which of the following is a correct example of the past perfect tense?"
    options = ["A) She was cooking dinner when the phone rang.",
               "B) They have already left for the airport.",
               "C) He will finish the project by tomorrow.",
               "D) I had never seen that movie before last night."]

    selection = container.radio(f"***{question}***", options)


if __name__ == '__main__':
    main()