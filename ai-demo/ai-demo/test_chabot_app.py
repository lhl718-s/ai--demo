import streamlit as st
import numpy as np

# 设置页面标题
st.title('欢迎来我的小小世界')

# 添加一些文本
st.write('hello，liu')


# 添加一个输入框
name = st.text_input('请输入你的名字', '世界')

# 显示输入框的内容
st.write(f'你好呀, {name}!')



with st.sidebar:
    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")


with st.chat_message("user"):
    st.write("Hello ")
    st.line_chart(np.random.randn(30, 3))


message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))