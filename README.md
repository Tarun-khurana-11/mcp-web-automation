# MCP Web Automation Agents

Intelligent web automation using **Model Context Protocol (MCP)** with **LangChain Agents** and **DeepAgents** for browser control via Playwright.

## 🌟 Features

- ✅ **Two Agent Types**: Standard Agent & DeepAgent (advanced reasoning)
- 🌐 **Web Automation**: Full browser control with Playwright MCP server
- 🧠 **AI-Powered**: Natural language to browser actions
- 🔄 **Smart Planning**: SNAPSHOT → PLAN → ACT → VERIFY loop
- 🛡️ **Safety**: Confirmation before irreversible actions
- 📧 **Multi-Site Support**: Gmail, TripAdvisor, Amazon, and any website

---

## 📋 Prerequisites

- Python 3.8+
- OpenAI API Key
- MCP Server running on port 8931 (or configure your own)

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd mcp
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the `mcp` directory:

```bash
cat > .env << 'EOF'
OPENAI_API_KEY=your-openai-api-key-here
EOF
```


### 5️⃣ Setup and Start Playwright MCP Server

Make sure your Playwright MCP server is running on port 8931:

```bash
# 1. Clone the Playwright MCP repository
git clone https://github.com/microsoft/playwright-mcp.git
cd playwright-mcp

# 2. Install dependencies
npx playwright install --with-deps

# 3.Start the MCP server on port 8931
npx @playwright/mcp@latest --port 8931
```

#### Verify MCP Server is Running

```bash
# Check if server is accessible
curl http://localhost:8931/mcp

# You should see a response indicating the MCP server is running
```

**Keep this terminal running** - the MCP server needs to stay active while your agents are running!

---

## 🎯 Running the Agents

### Option 1: Standard Agent (`client.py`)

**Best for**: General web automation tasks

```bash
python client.py
```

**Where to modify the query**: 
- **File**: `client.py`
- **Line**: 139
- **Location**:
```python
{"role": "user", "content": "YOUR QUERY HERE"}
```

**Example queries**:
```python
# Gmail automation
"go to gmail and login with credentials user@example.com and password yourpass, then draft an email to recipient@example.com with subject 'Test' and body 'Hello'"

# Web search
"go to tripadvisor.in and search for hotels in delhi"

# General browsing
"navigate to amazon.in and search for wireless mouse"
```

---

### Option 2: DeepAgent (`client_deep_agent.py`)

**Best for**: Complex tasks requiring deep reasoning

```bash
python client_deep_agent.py
```

**Where to modify the query**:
- **File**: `client_deep_agent.py`
- **Line**: 110
- **Location**:
```python
user_query = "YOUR QUERY HERE"
```

**Example queries**:
```python
# Travel planning
"go to tripadvisor.in and search for travel package for manali"

# Product research
"search for best laptops under 50000 on amazon and compare top 3"

# Multi-step tasks
"go to booking.com, search for hotels in Paris for next month, and get prices for top 5 hotels"
```

---

## 📝 Customization Guide

### Change the Query

#### For `client.py`:
1. Open `client.py`
2. Find line 139:
```python
{"role": "user", "content": "YOUR NEW QUERY HERE"}
```
3. Replace with your task
4. Save and run: `python client.py`

#### For `client_deep_agent.py`:
1. Open `client_deep_agent.py`
2. Find line 110:
```python
user_query = "YOUR NEW QUERY HERE"
```
3. Replace with your task
4. Save and run: `python client_deep_agent.py`

---

### Change MCP Server URL

Both files use: `http://localhost:8931/mcp`

To change it, modify line 60 in both files:
```python
client = MultiServerMCPClient({
    "playwright": {"transport": "http", "url": "http://YOUR_SERVER:PORT/mcp"}
})
```

---

## 🧠 Agent Comparison

| Feature | Standard Agent | DeepAgent |
|---------|---------------|-----------|
| **File** | `client.py` | `client_deep_agent.py` |
| **Speed** | ⚡ Fast | 🐢 Slower (more thinking) |
| **Reasoning** | Basic | 🧠 Deep multi-step |
| **Planning** | Simple | 📋 Advanced |
| **Best For** | Quick tasks | Complex research |

---

## 📖 System Prompt Features

Both agents use an advanced system prompt with:

### 1. **Operating Loop**
```
SNAPSHOT → PLAN → ACT → VERIFY → (repeat)
```

### 2. **Safety Rules**
- Ref-only interactions (no selector guessing)
- Confirmation before irreversible actions
- CAPTCHA detection and pause

### 3. **Smart Behavior**
- Form field purpose mapping
- Multi-step form handling
- Error recovery with alternatives
- Security-aware (no password leakage)

### 4. **Special Playbooks**
- Email composition workflow (customize in system_prompt if needed)
- Search and extraction
- Login procedures

---

## 📚 Project Structure

```
Ideafoundation/
├── mcp/                       # Main agent directory
│   ├── client.py             # Standard agent
│   ├── client_deep_agent.py  # DeepAgent (advanced)
│   ├── get_tools.py          # Tool listing utility
│   ├── requirements.txt      # Python dependencies
│   ├── .env                  # Environment variables (create this)
│   ├── README.md             # This file
│   └── venv/                 # Virtual environment
│
└── playwright-mcp/            # MCP Server (clone separately)
    ├── dist/                  # Compiled files
    ├── src/                   # Source code
    ├── package.json           # NPM dependencies
    └── index.js               # MCP server entry point
```

**Note**: Clone `playwright-mcp` repository separately in the parent directory

---