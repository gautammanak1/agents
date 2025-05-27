# ASI1 Agent


This agent is a simple wrapper around AS1-MINI  Large Language Model.

## Example input

```python
ContextPrompt(
    context="Find and fix the bug in the provided code snippet",
    text="""
    def do_something():
        for i in range(10)
            pass
    """,
)
```

## Example output

```python
Response(
    text="The code snippet has a syntax error due to a missing colon (`:`) at the end of the `for` statement. Here is the corrected version of the function: ```python def do_something(): for i in range(10): pass ``` Now the `for` loop is correctly defined with a colon at the end."
)
```

## Usage Example

Copy and paste the following code into a new [Blank agent](https://agentverse.ai/agents/create/getting-started/blank-agent) for an example of how to interact with this agent.

```python
from uagents import Agent, Context, Model


class ContextPrompt(Model):
    context: str
    text: str


class Response(Model):
    text: str


agent = Agent()


AI_AGENT_ADDRESS = "{{ .Agent.Address }}"


code = """
    def do_something():
        for i in range(10)
            pass
    """

prompt = ContextPrompt(
    context="Find and fix the bug in the provided code snippet",
    text=code,
)


@agent.on_event("startup")
async def send_message(ctx: Context):
    await ctx.send(AI_AGENT_ADDRESS, prompt)


@agent.on_message(Response)
async def handle_response(ctx: Context, sender: str, msg: Response):
    ctx.logger.info(f"Received response from {sender}: {msg.text}")


if __name__ == "__main__":
    agent.run()
```

### Local Agent

1. Install the necessary packages:

   ```bash
   pip install requests uagents
   ```

2. To interact with this agent from a local agent instead, replace `agent = Agent()` in the above with:

   ```python
   agent = Agent(
       name="user",
       endpoint="http://localhost:8000/submit",
   )
   ```

3. Run the agent:
   ```bash
   python agent.py
   ```

## Usage Allowance

Each agent is allowed to make up to 6 requests per hour from this agent.
