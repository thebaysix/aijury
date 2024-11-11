import json
import random
import time
from mistral_chat import MistralChatClient

# Assuming MistralChatClient is imported from somewhere, you may need to modify this import.
# from your_module import MistralChatClient 

class AgentChat:
    def __init__(self, mistral_client, agents_prompts):
        """
        Initialize the agent chat simulation with MistralChatClient and agents' prompts.
        
        :param mistral_client: An instance of MistralChatClient to simulate agent conversations.
        :param agents_prompts: A dictionary of agent names and their initial prompts.
        """
        self.client = mistral_client
        self.agents_prompts = agents_prompts

    def start_conversation(self, instructions, scenario):
        """
        Start a back-and-forth conversation between agents based on prompts.
        """
        print("Starting agent conversation...")

        # Give the overview prompt
        response = self.client.chat_with_mistral(instructions.get('overview'))
        print(f"Mistral says: {response}")

        # Give the first prompt with the trial info and the first juror (The Foreman)
        intro = (f"<BEGIN CASE>{scenario}<END CASE>"
             f"[juror_1: The Foreman] [You are the mediator of the group, responsible for guiding "
             "the discussion and ensuring everyone's voice is heard. When disagreements occur, "
             "you tend to go with the majority opinion, aiming to keep the deliberation process smooth and focused.]"
             "starts the conversation: "
        )
        response = self.client.chat_with_mistral(intro)
        print(f"Mistral says: {response}")

        # For now, randomly pick the next speaker (we'll get more sophisticated with this soon)
        last_speaker = "juror_1"
        next_speaker: str | None = None
        jurors = self.agents_prompts.items()

        for i in range(0, 30):
            if next_speaker == None:
                juror_id, speaker = random.choice(list(jurors))
            else:
                juror_id = next_speaker
                speaker = self.agents_prompts.get(juror_id)

            juror_name = speaker.get('juror_name')
            juror_prompt = speaker.get('juror_prompt')

            response: str = self.client.chat_with_mistral(f"[{juror_id}: {juror_name}] [{juror_prompt}] responds: ")
            print(f"Mistral says: {response}")

            # Sometimes the response contains a [PREPOSED NEXT SPEAKER: speaker] see if you can parse it.
            next_speaker_parse = response.split('PROPOSED NEXT SPEAKER: ')
            if next_speaker_parse.count == 2 and next_speaker_parse[1].lower() in list(jurors.keys):
                # 67% of the time, obey the LLM's proposed speaker.
                next_speaker = random.choice([next_speaker_parse[1].lower(), next_speaker_parse[1].lower(), None])
            else:
                next_speaker = None
            time.sleep(1)  # Adding delay for readability                 


# Example usage:
if __name__ == "__main__":
    # Instantiate MistralChatClient (assuming it has already been implemented)
    mistral_client = MistralChatClient()

    # Load agents' prompts from juror_prompt.json
    with open("prompts/jury_prompts.json", "r") as file:
        agents_prompts = json.load(file)

    # Create the AgentChat instance
    agent_chat = AgentChat(mistral_client, agents_prompts)

    with open("prompts/instructions_prompts.json", "r") as file:
        instructions = json.load(file)
    with open("prompts/cases.json", "r") as file:
        scenarios = json.load(file)

    # Start the conversation simulation
    scenario1 = json.dumps(scenarios.get('scenario_1'))
    agent_chat.start_conversation(instructions, scenario1)

    # Retrieve and print conversation history
    history = agent_chat.get_conversation_history()
    print("\nConversation History:")
    for agent, messages in history.items():
        print(f"\n{agent} History:")
        for msg in messages:
            print(f"  - {msg}")
