from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel,Agent,Runner, set_tracing_disabled
def main():
    set_tracing_disabled(True)

    key=config("GEMINI_API_KEY")
    base_url=config("base_url")
    gemini_client=AsyncOpenAI(api_key=key,base_url=base_url)
    Model=OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=gemini_client)
    agent=Agent(
        name="Kaif shamim",
        instructions="you are my helpfull assistant.",
        model=Model
    )
    res=Runner.run_sync(starting_agent=agent,input="how ai is destroying our self thonking and self confidence of achieving any thing")
    print(res.final_output)



if __name__ == "__main__":
    main()


