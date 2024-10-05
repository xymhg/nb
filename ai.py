
#后端

# 导库
# pip install OpenAI
from openai import OpenAI
from dotenv import load_dotenv
from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask,request,jsonify
from flask_cors import CORS


# 读取.env这个文件添加环境变量里面
load_dotenv()


# coding=utf-8
client = OpenAI(
    base_url='https://api.moonshot.cn/v1')
app=Flask(__name__)
CORS(app)

@app.route('/query' ,methods=['POST'])
def query():
    data = request.json
    ask = data.get('ask','')


    # 把这个提问传给ai
    completion = client.chat.completions.create(
        # 指定ai模型
        model="moonshot-v1-32k",
        messages=[
            # 定制我们的ai
            {'role': 'system', "content": ask},
            # 提交提问
            {"role": "user", "content": ask}
        ]
    )

    # 把ai的回答提取再给他打印出来
    answer = completion.choices[0].message.content
    return jsonify({'answer':answer})
    # print("你剩余的提问次数还有：", e - 1 - int(i), "次")
    #print("你剩余的提问次数:无限次")





if __name__== '__main__':
   app.run(debug=True)
