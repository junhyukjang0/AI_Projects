import json
import pandas as pd
import streamlit as st

# Streamlit 앱 레이아웃 설정
st.set_page_config(page_title="Today's English Expression", layout="wide")

# 앱 제목 및 설명
st.title("Today's English Words",)


@st.cache_data
def load_data():
    df = pd.read_excel("words.xlsx")
    df["usage"] = df.apply(lambda row: json.loads(row["usage"]), axis=1)
    return df


df = load_data()

for i, sample in df.iterrows():
    with st.container(border=True):
        st.subheader(f"{sample['emoji']} {sample['word']}")

        # situation 의 영단어의 뜻 
        st.markdown(sample["meaning"])

        with st.container(border=True):
            """사용법"""

            for i, row in enumerate(sample["usage"]["conversation"]):
                avatar = '🧑' if i % 2 == 0 else '👩🏼'
                with st.chat_message(avatar):
                    st.markdown(row['content'])
