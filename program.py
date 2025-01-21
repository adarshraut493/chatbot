import pyautogui
import time
import pyperclip  # For clipboard handling
from groq import Groq

client = Groq( 
    api_key="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"
)

def is_last_message_from_sender(chat_log,sender_name="Guddiya"):
    
    messages = chat_log.strip().split("/2025]")[-1]
    if sender_name in messages:
      return True
    return False


# Step 1: Click on the icon at (168, 758)
pyautogui.click(408, 757)

while True:
    # Wait for any UI to load, if necessary
    time.sleep(2)

    # Step 2: Drag to select text from (439, 111) to (1349, 662)
    pyautogui.moveTo(514,204)
    pyautogui.dragTo(522,699, duration=1,button='left')  # Drag the mouse to the end point

    # Step 3: Copy the selected text (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(482 , 156)

    # Wait for clipboard to populate
    time.sleep(0.5)

    chat_history = pyperclip.paste()

    # Step 4: Retrieve text from the clipboard
    # Print the captured text
    print("Selected text:", chat_history)
    
    
    if is_last_message_from_sender(chat_history):

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages = [
                {"role": "system", "content": "You are adarshraut439 who speaks English. You analyze chat history and respond like adarsraut439. output should be next chat response as (text message only)"},
                {"role": "user", "content":chat_history},
            ]
        )

        response = completion.choices[0].message.content

        pyperclip.copy(response)
        pyautogui.click(596,698)
        time.sleep(1)

        pyautogui.hotkey('ctrl','v')
        time.sleep(1)

        pyautogui.press('enter')