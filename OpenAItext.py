import os
import openai
from config import apikey

openai.api_key = apikey

# Your user input as a string
user_input = "write an email to my boss for resignation"

# Define a single message using the user input
messages = [
    {"role": "user", "content": user_input}
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,  # Use the messages list here
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)
'''
{
  "id": "chatcmpl-7fr5NjGmYWczCdH01h9YmdqXR1sJf",
  "object": "chat.completion",
  "created": 1690209865,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Subject: Resignation - (Your Name)\n\nDear (Boss's Name),\n\nI hope this email finds you well. I wanted to personally reach out to inform you of my decision to resign from my current position at (Company Name), effective (Last Working Day, typically two weeks from the date of this email).\n\nI want to express my deepest gratitude for the opportunities and experiences I have had during my employment with (Company Name). Over the course of my tenure here, I have gained invaluable skills and knowledge, for which I am truly grateful. It has been an honor to be part of such a talented and dedicated team.\n\nAfter careful consideration and reflection, I have decided to pursue a new challenge in my career that aligns better with my long-term goals and personal aspirations. While my decision was not an easy one to make, I believe it is the right time for me to explore new opportunities and grow professionally.\n\nI am committed to making this transition as smooth as possible. Therefore, I will do my best to complete all pending tasks and ensure a proper handover to my colleagues. If there is anything specific that you would like me to focus on during this transition period, please let me know, and I will be more than happy to assist.\n\nI am truly grateful for the"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 256,
    "total_tokens": 271
  }
}
'''
