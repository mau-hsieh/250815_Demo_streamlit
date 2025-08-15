import numpy as np
import pandas as pd
import streamlit as st

st.title("DataFrame Display Example")
st.write("This app displays a DataFrame with custom styling.")
st.write("## 123")

arr1 = np.array([1, 2, 3, 4, 5, 6])
st.write(arr1)

df1 = pd.DataFrame([[11,22,33,44], [55,66,77,88]])
st.write(df1)
st.table(df1)

st.write("## 核取方塊")
r1 = st.checkbox("Check me out!")
if r1:
    st.info("Checkbox is checked!")
else:
    st.info("Checkbox is not checked!")
    
checks = st.columns(3)
txt = ''
with checks[0]:
    r11 = st.checkbox("Check me out!001")
    if r11:
        txt += "Checkbox 1 is checked! "

with checks[1]:
    r12 = st.checkbox("Check me out!002")
    if r12:
        txt += "Checkbox 2 is checked! "

with checks[2]:
    r13 = st.checkbox("Check me out!003")
    if r13:
        txt += "Checkbox 3 is checked! "

if txt:
    st.info(txt)


st.write("## 按鈕")
b1 = st.radio("Select an option:", ["Option 1", "Option 2", "Option 3"],horizontal=True)
st.info(f"You selected: {b1}")

b2 = st.radio("Select an option:", ["Option 1", "Option 2", "Option 3"],horizontal=True, key="radio2")
st.info(f"You selected: {b2}")

st.write("## 滑桿")
slider_val = st.slider("選擇一個數字", 1.0, 5.0, 1.0,0.1)
st.info(f"你選擇的數字是: {slider_val}")

st.write('## 下拉選單')
city = st.selectbox("選擇一個城市", ["台北", "台中", "高雄"])
st.info(f"你選擇的城市是: {city}")
if city == "台北":
    st.info("台北是台灣的首都。")
elif city == "台中":
    st.info("台中是台灣的第三大城市。")
elif city == "高雄":
    st.info("高雄是台灣的第二大城市。")
    
st.write("## 側邊欄(左側)")
st.sidebar.title("Sidebar Example")
test = st.sidebar.selectbox("選擇一個選項", ["選項1", "選項2", "選項3"])
st.sidebar.info(f"你在側邊欄選擇的選項是: {test}")

st.sidebar.info("這是側邊欄的資訊。")

st.write("## 按鈕")
a = st.number_input("輸入一個數字")
b = st.number_input("輸入一個數字",key="num2")
st.info(f"你輸入的數字是: {a} 和 {b}")
if st.button("計算總和"):
    total = a + b
    st.success(f"兩個數字的總和是: {total}")

