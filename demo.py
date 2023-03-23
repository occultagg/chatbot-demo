import openai
import os

#export OPENAI_API_KEY='sk-...'
api_key= os.environ["OPENAI_API_KEY"]

openai.api_key = api_key

messages = []

while True:
    user_input = input('user:')
    messages.append({'role': 'user', 'content': user_input})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages
        )
    print("chatgpt:{}".format(completion.choices[0].message.content))