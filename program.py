#TANISH
import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(
  api_key="API_KEY",
)

def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False
# Step 1: Click on the chrome icon at coordinates (1639, 1412)
pyautogui.click(1148, 1075)
time.sleep(1)  # Wait for 1 second to ensure the click is registered

while True:

# Pause for a moment to allow you to switch to the correct window
time.sleep(2)

# Click at the specified position
# pyautogui.click(1161, 1054)
time.sleep(2)

# pyautogui.click(442, 475,button='left')
time.sleep(1)
pyautogui.moveTo(674,276)

# Drag from (674, 276) to (1759, 900) to select text
pyautogui.dragTo(1759, 900, duration=1,button='left')  # Adjust the duration as needed

# Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')
pyautogui.click()

# Allow a moment for the clipboard to update
time.sleep(0.5)

# Get the copied text from the clipboard
chat_history = pyperclip.paste()

# Print the copied text
print(chat_history) 
print(is_last_message_from_sender(chat_history))
# if is_last_message_from_sender(chat_history):
completion = client.chat.completions.create(
model="gpt-3.5-turbo",
messages=[
    {"role": "system", "content": "You are a person named tanish who speaks hindi as well as english. you are from India.you gives always funny replay to all. You analyze chat history and respond in real manner and also in funny manner when someone send funny msg send them funny msg and when someone is telling fact tell him you are correct. output should be short and understandable and should be the next chat response and dont send name and time of sender only text reply of last response."},
    {"role": "system", "content":"dont pretend to be coder in every response and be a normal boy who is replying in funny and respectful manner"},
    {"role": "user", "content": chat_history}
  ]
)

response = completion.choices[0].message.content

pyperclip.copy(response)

pyautogui.click(1228, 956)

# Paste the copied text
pyautogui.hotkey('ctrl', 'v')

# Press Enter
pyautogui.press('enter')
