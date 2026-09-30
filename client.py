
from multiprocessing.spawn import import_main_path
from PIL.ImagePalette import load
from google.genai import client
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()


import asyncio

async def my():
    client = MultiServerMCPClient({
        "hospital_server":{
            "command":"python",
            "args":["hospital.py"],
            "transport":"stdio",
        }

    })
    import os
    os.environ["GROP_API_KEY"] = os.getenv("GROQ_API_KEY")

    agent = create_agent(
        model = ChatGroq(model='openai/gpt-oss-120b',
        temperature = 0),
        tools = await client.get_tools(),
        system_prompt="""
                    You are a Hospital Chatbot.
                     
                     IMPORTANT RULES:
                     
                     1. Always use an MCP tool when the user's question is related to
                        hospital-specific information.
                     2. Do NOT create, guess, or assume hospital-specific information.
                     
                     3. If the user asks service or treament provide related question used
                        use the `service` tool and make your own answer
                     4. If the user asks for any contact information, you must use the 'contactNumber' tool to provide the response.
                     5. If the user asks for information that is not available through any tool, clearly say:
                        "Sorry, this information is not available in the Hospital system."
                     
                     MAIN RULE:
                     User Question → Select Appropriate MCP Tool → Call Tool → Get Result → Answer User
                     
                     Never skip the tool when a suitable tool is available.
                        """
                         )
    
    test_1 = await agent.ainvoke({"messages":
    [{"role":"user","content":"provide me the contact number of sita neupana ?"}]})

    print("response : ",test_1["messages"][-1].content)

asyncio.run(my())