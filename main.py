from agents import Agent,Runner
from agents.extensions.models.litellm_model import LitellmModel
MODEL_NAME="gemini/gemini-2.0-flash"
API_KEY=config("Gemini_API_KEY")
assistant=Agent(
    name="Testing_Agent" ,
                instuctions="Your are a helpful assistint",
                model=LitellmModel(model=MODEL_NAME,api_key=API_KEY),
                api_key=API_KEY)
output =await Runner.run(starting_agent=assistant, input="How are you?")
print(output.final_output)
          
