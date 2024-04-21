# Speaking Practice Through Role Playing AI
**Demonstration Video URL** :  https://youtu.be/tJ-JmxiTZIU

## Execution File
**To execute** : streamlit app.py
  		    uvicorn backend:app --reload
		    
**app.py** : Streamlit to provide an interactive and engaging platform for users to practice English through various real-life scenarios. 
**backend.py** : FastAPI web server to support an interactive role-playing application for practicing conversational English. It integrates OpenAI's GPT models and Whisper for voice recognition, and it is structured to handle various role-play scenarios where users can practice real-world interactions.


## Fine_Tuning
**finetuning.ipynb** :  Build a Further Fine-Tuning model by incorporating a pre-trained model with training data generated through simulated conversations between two AI agents acting out a scenario. This model aims to improve its performance within the designated context.

 **prepare_data.ipynb** : Create reference training data to assist AI in delivering fluent responses within a specified scenario.
 
