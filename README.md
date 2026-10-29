# AI Writing Assistant — Week 1 Mini Project

A Python + Streamlit application that uses an LLM API to generate:
- Blog posts
- Professional email drafts
- Beginner-friendly code explanations
- Social media posts

Features include selectable AI provider (Gemini/OpenAI), temperature control, tone selection, output formatting, approximate output length, and downloading results as a text file.

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (optional but recommended).
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Copy `.env.example` to `.env` and add your API key. Get a key from Google AI Studio for Gemini or the OpenAI platform for OpenAI. Never upload `.env` to GitHub.
6. Start the app:

   ```bash
   streamlit run app.py
   ```

## GitHub submission

Create a public repository named `ai-writing-assistant-week1`, upload the project files, and submit the repository URL on the internship page. Do not commit API keys.

## Notes

API usage may incur charges or have rate limits depending on provider and account. This project requires an API key; it does not work offline.
