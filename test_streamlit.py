# app.py
# 核心套件
import streamlit as st
import pandas as pd 
import streamlit as st
def main():
    """主函式中撰寫您的程式碼"""
    st.title('Hello World!!!')
    user_input = st.text_input("請在此輸入您的名字")
    st.write("您輸入的名字是：", user_input)
    st.text_input("請輸入密碼", type="password")
    user_text = st.text_area("請輸入您的留言")
    st.write("您的留言是：", user_text)
    date = st.date_input("選擇日期")
    st.write("選擇的日期是：", date)
    time = st.time_input("選擇時間")
    st.write("選擇的時間是：", time)
    number = st.number_input("輸入數字", min_value=0, max_value=100)
    st.write("您輸入的數字是：", number)
    choice = st.radio("選擇一個選項", ("選項1", "選項2", "選項3"))
    st.write("您選擇了：", choice)

    toggle = st.toggle("切換選擇")
    st.write("開關狀態是：", toggle)

    agree = st.checkbox("我同意條款")
    if agree:
        st.write("謝謝您的同意！")
    option = st.selectbox("選擇一個選項", ["選項1", "選項2", "選項3"])
    st.write("您選擇了：", option)
    options = st.multiselect("選擇多個選項", ["選項1", "選項2", "選項3"])
    st.write("您選擇了：", options)
    value = st.slider("選擇數值", min_value=0, max_value=100, value=50)
    st.write("您選擇的數值是：", value)
    option = st.select_slider("選擇一個選項", options=["選項1", "選項2", "選項3"])
    st.write("您選擇了：", option)

    color = st.color_picker("選擇顏色", "#00f900")
    st.write("您選擇的顏色是：", color)
    df = pd.read_csv("data/ic03.csv")
    st.subheader("This is a df")
    st.dataframe(df,800,300)   
    # 成功
    st.success("Successful")
# 警告
    st.warning("This is a warning")
# 資訊警報
    st.info("This is an info alert")
if __name__ == '__main__':
    main()