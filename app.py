import streamlit as st

# タイトル


# パスワード入力（●●で隠す）
password = st.text_input("パスワードを入力してください", type="password")

# ボタンを押したときに判定する
if st.button("送信"):
    if password == "0619germany":
        st.success("正解")
    else:
        st.error("不正解です")
