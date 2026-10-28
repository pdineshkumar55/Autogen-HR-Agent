# AutoGen HR Agent

My first AutoGen agent: an `AssistantAgent` that acts as an HR assistant and writes a 5-line job description for a Junior Python Developer.

AutoGen runs on `asyncio`, so the script is built around an `async` function and started with `asyncio.run()`.

## Features

- An `AssistantAgent` with the system message `"You are an HR assistant."`
- A model client built with `OpenAIChatCompletionClient` (`gpt-4o-mini`)
- The reply streams to the terminal with AutoGen's `Console`
- The model client is closed in a `finally` block, so the script never hangs
- The OpenAI API key is read from a `.env` file and never hard-coded

## Tech Stack

- Python 3.10+
- [AutoGen](https://github.com/microsoft/autogen) (`autogen-agentchat`, `autogen-ext[openai]`)
- `python-dotenv`
- An OpenAI API key

## Project Structure

```
Autogen-hr-agent/
├── .venv/          # virtual environment (not committed)
├── .env            # API key (not committed)
├── .gitignore
├── hr_agent.py     # the agent script
└── README.md
```

## Setup

1. **Clone or download the project** and open the folder in VS Code.

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   ```

   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
   - macOS/Linux: `source .venv/bin/activate`

3. **Install the dependencies**

   ```bash
   pip install -U "autogen-agentchat" "autogen-ext[openai]" python-dotenv
   ```

4. **Add your API key**

   Create a file named `.env` in the project folder:

   ```
   OPENAI_API_KEY=sk-your-key-here
   ```

5. **Keep secrets out of Git**

   Add this to `.gitignore`:

   ```
   .env
   .venv/
   ```

## Run

```bash
python hr_agent.py
```

## Sample Output

```
---------- TextMessage (user) ----------
Write a 5-line job description for a Junior Python Developer.
---------- TextMessage (hr_assistant) ----------
We are seeking a motivated Junior Python Developer to join our dynamic team.
The ideal candidate will assist in designing, coding, and testing software
applications using Python. Responsibilities include collaborating with senior
developers to troubleshoot and resolve issues, maintaining documentation, and
participating in code reviews. A basic understanding of web frameworks and
databases is essential. This is an excellent opportunity for growth and
learning in a supportive environment.
```

## How It Works

1. `load_dotenv()` loads `OPENAI_API_KEY` from `.env` into the environment.
2. `OpenAIChatCompletionClient` creates the connection to the OpenAI model.
3. `AssistantAgent` is created with a name, the model client, and the HR system message.
4. `agent.run_stream(task=...)` sends the request, and `Console` prints the streamed messages.
5. `model_client.close()` runs in `finally` to release the client so the script exits cleanly.

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: autogen_agentchat` | Activate the venv and select it as the interpreter in VS Code |
| `OPENAI_API_KEY not found` | Check that the file is named exactly `.env` (not `.env.txt`) and sits next to `hr_agent.py` |
| PowerShell blocks `Activate.ps1` | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once |
| `model_not_found` | Change `model=` to a model your OpenAI account can use |

## Possible Improvements

- Make the prompt stricter so the reply comes back as exactly 5 separate lines
- Accept the job title as a command-line argument
- Add a second agent (for example, a reviewer) to refine the job description