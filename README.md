# 🤖 AI Assistant Runner

This project runs an AI agent using the `openai-agents` library and Gemini 2.5 Flash model to provide helpful responses to user input.

## 🚀 Quick Setup

### 1. Install `uv` (if not already installed)


pip install uv
## ⚙️ Setup Instructions

### 2. Add Dependencies


uv add openai-agents python-decouple


### 3. Configure Environment Variables
Create a .env file in the root directory with the following content: env
GEMINI_API_KEY=your_gemini_api_key_here
base_url=https://your-gemini-api-base-url.com


### 4. Run the Script bash 
uv run main.py
