import streamlit as st

# タイトル


# パスワード入力（●●で隠す）
password = st.text_input("パスワードは、始まりの日（8桁）", type="password")

# ボタンを押したときに判定する
if st.button("送信"):
    if password == "18670914":
        st.success("正解!正解したと彼に伝えてみよう！低確率で飴がもらえるぞ！高確率で暇なの？って目で見られる")
    else:
        st.error("不正解")
