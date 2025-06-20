#基于控制台的Chatbot
import os
import time
from openai import OpenAI
# 设置 openai相关的参数
import tiktoken
MAX_TOKENS=8
MAX_RESPONSE_TOKENS=6
encoder=tiktoken.encoding_for_model("gpt-4o")     #初始化tiktoken编码器


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)
#运算tokens
def count_tokens(text):
    encoder.encode(text)
    tokens=encoder.encode(text)
    return len(tokens)



#Create a chat completion
def stream_completion_responce(prompt):
        response = client.chat.completions.create(
            model="gpt-4o",  # 使用的模型名称
            messages=[

                {"role": "user", "content":prompt}
            ],
            stream=True , # 启用流式传输
            max_tokens=200,
            temperature=0.7
        )

        for chunk in response:
            #获取消息片段
            chunk_massage=chunk.choices[0].delta.content if chunk.choices[0].delta.content else ""
            print(chunk_massage,end="")

    #prompt="怎么在pycharm终端切换环境"
    #stream_completion_responce(prompt)

while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        print('====================')
        stream_completion_responce(user_input)


