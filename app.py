import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Writing Assistant", page_icon="✍️", layout="centered")
st.title("✍️ AI Writing Assistant")
st.write("Generate blogs, professional emails, code explanations, and social media posts.")

provider = st.sidebar.selectbox("AI Provider", ["Gemini", "OpenAI"])
temperature = st.sidebar.slider("Creativity (temperature)", 0.0, 1.5, 0.7, 0.1)
style = st.sidebar.selectbox("Output format", ["Clear paragraphs", "Bullet points", "Numbered steps"])
max_words = st.sidebar.slider("Approx. output length (words)", 50, 800, 250, 50)

task = st.selectbox("Choose a task", ["Blog Writing", "Email Drafting", "Code Explanation", "Social Media Post"])
prompt = st.text_area("Describe what you want", height=150, placeholder="Enter your topic, email details, code, or post idea...")
tone = st.selectbox("Tone", ["Professional", "Friendly", "Simple", "Creative", "Formal"])

def make_prompt(task, user_input, tone, style, max_words):
    instructions = {
        "Blog Writing": "Write a useful blog post with a title and an introduction, main points, and conclusion.",
        "Email Drafting": "Draft a complete email with a suitable subject line and professional greeting/closing.",
        "Code Explanation": "Explain the supplied code in beginner-friendly language. Describe its purpose and important lines.",
        "Social Media Post": "Create an engaging social media post with a hook and relevant hashtags."
    }
    format_instruction = {
        "Clear paragraphs": "Use clear, readable paragraphs.",
        "Bullet points": "Use bullet points wherever appropriate.",
        "Numbered steps": "Use numbered steps wherever appropriate."
    }[style]
    return f"""Task: {task}
Instruction: {instructions[task]}
Tone: {tone}
Length: approximately {max_words} words.
Formatting: {format_instruction}
User request/content:
{user_input}
If information is missing, make reasonable assumptions and do not invent factual claims."""

if st.button("Generate", type="primary", use_container_width=True):
    if not prompt.strip():
        st.warning("Please enter a topic or content first.")
    else:
        try:
            final_prompt = make_prompt(task, prompt, tone, style, max_words)
            with st.spinner("Generating..."):
                if provider == "Gemini":
                    api_key = os.getenv("GEMINI_API_KEY", "")
                    if not api_key:
                        st.error("Add GEMINI_API_KEY to your .env file.")
                        st.stop()
                    from google import genai
                    client = genai.Client(api_key=api_key)
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=final_prompt,
                        config={"temperature": temperature}
                    )
                    result = response.text or "No text returned."
                else:
                    api_key = os.getenv("OPENAI_API_KEY", "")
                    if not api_key:
                        st.error("Add OPENAI_API_KEY to your .env file.")
                        st.stop()
                    from openai import OpenAI
                    client = OpenAI(api_key=api_key)
                    response = client.responses.create(
                        model="gpt-4.1-mini",
                        input=final_prompt,
                        temperature=temperature
                    )
                    result = response.output_text
            st.subheader("Generated result")
            st.markdown(result)
            st.download_button("Download as TXT", result, file_name="ai_writing_output.txt")
        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.caption("Week 1 Mini Project | Python + LLM API | Keep API keys private.")
