import asyncio
import os

from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Load variables from the .env file into the environment
load_dotenv()


async def main() -> None:
    # Read the API key from the environment (loaded from .env)
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not found. Add it to your .env file.")

    # Model client
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        api_key=api_key,
    )

    # Assistant agent
    hr_agent = AssistantAgent(
        name="hr_assistant",
        model_client=model_client,
        system_message="You are an HR assistant.",
    )

    try:
        # Run the task and stream the reply to the console
        await Console(
            hr_agent.run_stream(
                task=(
                "Write a job description for a Junior Python Developer in exactly 5 lines. "
                "Put each line on its own line, with no heading and no extra text."
                )
            )
        )
    finally:
        # Always close the client, or the script can hang
        await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())