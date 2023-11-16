from django.conf import settings
import os
from openai import OpenAI

client = OpenAI()
client = OpenAI(
  api_key=settings.OPENAI_API_KEY,
)



def get_completion(prompt):
    completion = client.chat.completions.create(
     model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful giving information and answering questions about Matt Cresswell, keep your answers concise."},
    {"role": "user", "content": prompt}
    ] 
    )
    output = completion.choices[0].message
    return output