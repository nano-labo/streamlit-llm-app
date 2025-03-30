
#from dotenv import load_dotenv
#load_dotenv()

import streamlit as st

st.title("専門家の相談チャンネル: ")

st.write("##### 使い方")
st.write("相談したい専門家を選択し、入力フォームに相談したい内容を入力し、「相談」ボタンを押すと相談結果が表示されます。")

selected_item = st.radio(
    "相談したい専門家を選択してください。",
    ["運動の専門家", "栄養の専門家"]
)

st.divider()

input_message = st.text_input(label="専門家に相談したい内容を入力してください。")

if st.button("相談"):
    st.divider()

    from langchain_openai import ChatOpenAI
    from langchain.schema import SystemMessage, HumanMessage
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=f"あなたは{selected_item}です。"),
        HumanMessage(content=f"{input_message}}"),
    ]
    result = llm(messages)
    st.write(result.content)
    st.divider()
    st.write(input_message)
    st.divider()
    st.write(messages)
    st.divider()
    st.write(result)
