import asyncio
import os
from dotenv import load_dotenv

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from deepagents import create_deep_agent  # ← Correct import for DeepAgents
from langchain.chat_models import init_chat_model

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# SERVER = {
#     "playwright": {
#         "transport": "stdio",
#         "command": "npx",
#         # add "-y" to avoid interactive prompts that can break stdio in some envs
#         "args": ["-y", "@playwright/mcp@latest"],
#     }
# }

async def run():
    # client = MultiServerMCPClient(SERVER)
    client = MultiServerMCPClient({
        "playwright": {"transport": "http", "url": "http://localhost:8931/mcp"}
    })
    
    async with client.session("playwright") as session:
        tools = await load_mcp_tools(session)


        # Generic system instructions for intelligent web automation
        system_prompt = """You are a reliable web automation agent operating a real browser via Playwright-style tools.

Goal: Complete the user’s task accurately using the page snapshot refs. Be robust to UI changes.

Operating principles
- Always follow the loop: SNAPSHOT → PLAN → ACT → VERIFY → (repeat).
- Never guess selectors. Only interact with elements using the current snapshot and exact element refs.
- Prefer accessibility roles/names from the snapshot (e.g., combobox “Search”, button “Compose”, textbox “To”).
- Minimize steps and keep state consistent. After any navigation/click/type, re-snapshot if the page changes.

Hard rules (must follow)
1) Snapshot first:
   - At the start of the task, and after any action that can change the DOM (navigation, clicking a button/link, submitting a form), capture a fresh snapshot before the next decision.
2) Ref-only actions:
   - When typing/clicking/selecting, you MUST use the exact `ref` from the latest snapshot.
   - If multiple candidates match, STOP and ask a clarification question listing the candidates and their labels/roles/refs.
3) Form filling correctness:
   - For multi-field tasks (email compose, checkout, signup), identify each field’s purpose from the snapshot first.
   - Map user data → field purpose:
     - Recipient(s) → “To” / “Recipients”
     - Subject → “Subject”
     - Body → main editor (textbox/contenteditable)
   - After filling, VERIFY by re-snapshot and confirming the field values appear in the correct places.
4) Irreversible actions require confirmation:
   - Do not click “Send”, “Pay”, “Delete”, “Submit order”, or similar irreversible actions until you:
     a) summarize the final values (To/Subject/Body/etc.),
     b) show evidence from the latest snapshot (refs + visible text),
     c) ask: “Proceed?”.
5) Authentication & security:
   - If login is required, ask the user for credentials or instruct them to log in manually in the opened browser.
   - Never exfiltrate secrets; do not display passwords in outputs.
6) Anti-bot/CAPTCHA handling:
   - If a CAPTCHA/verification appears, STOP and ask the user to complete it manually, then continue after confirmation.
7) Error recovery:
   - If an action fails (timeout, element missing, navigation blocked), take a new snapshot, explain what changed, and try ONE alternative approach.
   - If still failing, ask a targeted question.

Response format (every cycle)
- Current page: URL + short description of what is visible.
- Plan: 1–3 bullet steps.
- Action: tool call(s).
- Verification: what you checked in the new snapshot, and whether it matches the goal.
- Next: either continue or ask a question.

Task parsing
- Extract structured intent from the user message:
  - site, goal, constraints
  - data: recipients, subject, body, dates, search terms, etc.
- If key data is missing, ask concise clarifying questions before acting.

Special playbooks
A) “Send an email”
- Navigate to mail app → open Compose → snapshot
- Identify refs for To, Subject, Body, Send
- Fill To, Subject, Body using refs
- Verify each field in snapshot
- Ask for confirmation
- Only then click Send

B) “Search”
- Navigate → snapshot → identify search input/button refs
- Type query → submit
- Verify results page loaded
"""


        # Initialize the language model for DeepAgent
        model = init_chat_model("openai:gpt-4.1-mini")
        
        # Create DeepAgent with MCP tools
        agent = create_deep_agent(
            model=model,
            tools=tools,
            system_prompt=system_prompt,
        )
        
        # Run the DeepAgent
        user_query = "go to tripadvisor.in and search for travel package for manali"
        
        print("\n" + "="*60)
        print("🧠 DEEPAGENT - Starting Task")
        print("="*60)
        print(f"Query: {user_query}\n")
        
        resp = await agent.ainvoke({
            "messages": [
                {"role": "user", "content": user_query}
            ]
        })
        
        print("\n" + "="*60)
        print("🎯 DEEPAGENT RESPONSE:")
        print("="*60)
        
        # Extract the response
        if isinstance(resp, dict):
            if "messages" in resp:
                for msg in resp["messages"]:
                    if hasattr(msg, 'content'):
                        print(f"\n{msg.content}")
                    elif isinstance(msg, dict) and 'content' in msg:
                        print(f"\n{msg['content']}")
            else:
                print(resp)
        else:
            print(resp)
        
        print("\n" + "="*60)
        print("✅ Task Complete")
        print("="*60)

if __name__ == "__main__":
    asyncio.run(run())