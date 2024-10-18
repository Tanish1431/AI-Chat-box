from openai import OpenAI

# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="API_KEY",
)

command='''
[11:20 PM, 10/14/2024] Tanish: Tereko nhi bol rha
[11:21 PM, 10/14/2024] Tanish: Yeh itna tax lagta hai naa inko bola
[11:21 PM, 10/14/2024] Tanish: 😂😂😂
[11:21 PM, 10/14/2024] Tanmay : To bhr se h isliye mene 10 dollar nikale the
[11:21 PM, 10/14/2024] Tanmay : Lekin m bapis 10 dollar dalunga to itne bapis aajayenge
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named tanish who speaks hindi as well as english. He is from India. You analyze chat history and respond like tanish"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)