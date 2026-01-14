import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
import os

async def list_tools():
    print("Connecting to Playwright MCP...")
    
    client = MultiServerMCPClient({
        "playwright": {
            "transport": "stdio",  # REQUIRED for npx subprocess
            "command": "npx",
            "args": ["@playwright/mcp@latest"],
        }
    })
    
    print("Getting tools...")
    tools = await client.get_tools()
    
    print(f"\nPlaywright MCP tools ({len(tools)}):")
    print("-" * 60)
    for i, t in enumerate(tools, 1):
        desc = t.description[:60] if len(t.description) > 60 else t.description
        print(f"{i}. {t.name}")
        print(f"   {desc}...")
        print()

if __name__ == "__main__":
    asyncio.run(list_tools())