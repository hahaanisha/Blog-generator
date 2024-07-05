import streamlit as st
import replicate

# Function to get response from the model using Replicate API
def getResponse(input_text, no_of_words, blog_style):
  
    replicate_client = replicate.Client(api_token="r8_MLSQkDZgamCRh8TpqgmaNjWfKmQqo3Q3nkoxq")

    # Prompt Template
    prompt = f"""
    Write a blog for {blog_style} job profile for the topic given as {input_text} within {no_of_words} words.
    """
    
    # Generate response from Replicate API
    output = ""
    for event in replicate_client.stream(
        "meta/llama-2-70b-chat",
        input={"prompt": prompt},
    ):
        output += str(event)
    
    print(output)
    return output

# Streamlit setting up:
st.set_page_config(page_title="Generate Blogs", page_icon='🐸', layout='centered', initial_sidebar_state='collapsed')

st.header("Generate Blogs 🐸")

# Fields for input: blog topic, number of words, blog style
input_text = st.text_input("Enter topic for the blog")

col1, col2 = st.columns([5, 5])

with col1:
    no_of_words = st.text_input('No. of Words')

with col2:
    blog_style = st.selectbox("I am writing the blog for",
                              ('Researchers', 'Data Scientist', 'Common people'), index=0)

submit = st.button("Generate")

# response
if submit:
    if input_text and no_of_words and blog_style:
        response = getResponse(input_text, no_of_words, blog_style)
        st.write(response)
    else:
        st.warning("Please fill out all fields.")

