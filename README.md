## Simple Chatbot

A minimal Streamlit chat interface powered by LangChain and a hosted LLM via the Hugging Face Inference Router. It supports adjustable creativity (temperature) and keeps a running chat history.

### Features
- **Streamlit chat UI**: uses `st.chat_input` and `st.chat_message` for a clean chat experience
- **LLM via LangChain**: `ChatOpenAI` routed to Hugging Face (`https://router.huggingface.co/v1`)
- **Configurable temperature**: slider to control response creativity
- **Session history**: messages persist during the session

### Project structure
```text
Simple_chatbot/
  ├─ main.py                # Streamlit app entrypoint
  ├─ langchain_helper.py    # LLM wiring with LangChain
  ├─ .env                   # Your secrets (not committed)
  └─ .gitignore
```

### Requirements
- Python 3.9+
- A Hugging Face access token with Inference permissions (`HF_TOKEN`)

### Quick start
1) Clone and enter the project directory.
2) Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\\Scripts\\activate
```
3) Install dependencies:
```bash
pip install streamlit langchain langchain-openai python-dotenv
```
4) Create a `.env` file in the project root:
```bash
echo HF_TOKEN=your_huggingface_token_here > .env
```
5) Run the app:
```bash
streamlit run main.py
```

Then open the local URL shown in the terminal (typically `http://localhost:8501`).

### Configuration
This project uses a hosted model via the Hugging Face Router. The defaults are set in `langchain_helper.py`:
- `openai_api_base`: `https://router.huggingface.co/v1`
- `model_name`: `Qwen/Qwen3-Coder-480B-A35B-Instruct:fireworks-ai`
- `HF_TOKEN`: read from the environment via `.env`

To change the model or endpoint, update the corresponding fields in `langchain_helper.py`.

### How it works (high level)
- `main.py` builds a Streamlit chat UI, tracks messages in `st.session_state.history`, and forwards user prompts to the LLM helper.
- `langchain_helper.py` sets up a minimal LangChain pipeline (`PromptTemplate` → `ChatOpenAI`) and returns the model's response.

### Environment variables
Create a `.env` file with the following key:
```env
HF_TOKEN=your_huggingface_access_token
```

### Troubleshooting
- **401/403 errors**: ensure `HF_TOKEN` is valid and has permissions.
- **Module not found**: verify your virtual environment is activated and dependencies are installed.
- **Network timeouts**: re-run later or try a different model via `model_name`.

### Notes
- This app is for demonstration and local prototyping. For production, consider adding request timeouts, better error handling, and usage logging.


