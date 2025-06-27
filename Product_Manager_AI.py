import streamlit as st 
from openai import OpenAI

client = OpenAI(api_key='my-api-key')

def get_completion(prompt, model="gpt-3.5-turbo"):
    completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role": "system", "content": "You are an AI career advisor. Provide advice on what are the technical and soft skills needed for Associate Product Manager"},
        {"role": "user", "content": prompt},
        ]
    )
    return completion.choices[0].message.content

option = st.selectbox(
    "Choose input type:",
    ("Job Title", "Job Description")
)

with st.form(key="chat"):
    if option == "Job Title":
        prompt = st.text_input("Job Title:")
        submitted = st.form_submit_button("Submit")
    else:
        prompt = st.text_area(
            "Job Description:",
        )
        submitted = st.form_submit_button("Submit")
        
st.write(get_completion(prompt))
response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
st.image(image_url,
         caption="Generated Image of Product Manager")