import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
import os
from rich.console import Console

load_dotenv()

async def run_memory_chat():
    #load environment variables for API keys
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    #configure file path
    config_file = "browser_mcp.json"

    console = Console()
    console.print("""
        [bold pink]
        🌷 Hi, I’m MochiBot — your cozy AI companion! 🧋
        I’m here to chat, giggle, and help however I can~ 💖
        Type 'help' to see what I can do!
        [/bold pink]
        """)

    #Create MCP client and agent with memory enables
    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="qwen-qwq-32b")

    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True, #Enable built-in conversation memory

    )

    print("\n===== Interactive MCP Chat=====")
    print("Type 'exit' to end the conversation")
    print("Type 'clear' to clear conversation history")
    print("===============================\n")
    
    try:
        while True:
            #Get user input
            user_input = input("\nYou")

            #Check for exit command
            if user_input.lower() in ["exit", "quit"]:
                print("Ending conversation......")
                break

            #Check for clear history command
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared")
                continue

            if user_input.lower() == "help":
                print("🛠 Available commands:\n• exit\n• clear\n• help\n• (Ask me anything!)")
                continue

            #Get repsonse from agent
            console.print("\n[bold cyan]🌸 GroqBot:[/bold cyan]", end=" ")



            try:
                response = await agent.run(user_input)
                print(f"{response} ✨")


            except Exception as e:
                print(f"\nError:{e}")
    finally:
        if client and client.sessions:
            await client.close_all_sessions()
            
if __name__ == "__main__":
    asyncio.run(run_memory_chat())
