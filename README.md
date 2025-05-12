# 🧠 MCP AI Assistant (Groq-powered)

This project is a conversational AI assistant built using LangChain, Groq's large language models (LLMs), and a memory-enabled agent interface via MCP (Model Connected Programming). It supports multi-turn conversations, command execution, and dynamic interaction — all through a Groq-powered backend.

---

## 🚀 Features

- Chat interface with built-in conversation memory  
- Uses `qwen-qwq-32b` or any Groq-supported LLM  
- MCPClient + MCPAgent integration  
- JSON-based configuration  
- `.env` support for secure API key management  

---

## 🛠 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/MCP_AI_Assistant.git
cd MCP_AI_Assistant
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
# On Windows PowerShell
.\venv\Scripts\Activate.ps1
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up your `.env` file**

Create a `.env` file in the root of the project and add your [Groq API key](https://console.groq.com/keys):

```
GROQ_API_KEY=your_api_key_here
```

> ⚠️ **Do NOT share your API key**. Keep the `.env` file private.

---

## 📦 Running the Chat Assistant

```bash
python app.py
```

You’ll see an interactive CLI chat session:
- Type your message and press enter
- Type `clear` to reset conversation memory
- Type `exit` or `quit` to close the session

---

## 🔁 Switching Models

To use another Groq model, update this line in `app.py`:

```python
llm = ChatGroq(model="qwen-qwq-32b")
```

Valid models include:
- `qwen-qwq-32b`
- `llama3-8b-8192`
- `llama3-70b-8192`
- `gemma-7b-it`

> Make sure your API plan supports the selected model.

---

## 🔒 Security Reminder

- Keep your `.env` file out of version control (already included in `.gitignore`)  
- Never hardcode your API keys in source files  
- Rotate your keys periodically via the [Groq Console](https://console.groq.com)

---

## 📌 Future Plans

This repo will be updated to explore:
- Advanced memory modules  
- Tool use (web search, file reading)  
- Streamlit integration  
- RAG (Retrieval-Augmented Generation)  
- Deployment-ready architecture  

---

## 🙌 Credits

- [Groq API](https://console.groq.com/)  
- [LangChain](https://www.langchain.com/)  
- [MCP Framework](https://cursor.sh)  

---

## 📄 License

MIT License – use freely with attribution.
