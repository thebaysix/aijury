import os
from mistralai import Mistral

MISTRAL_API_KEY =  os.environ.get('MISTRAL_API_KEY')

class MistralChatClient:
    """Client which offers and interface through which to chat with Mistral"""

    def __init__(self):
        self.client = Mistral(api_key=MISTRAL_API_KEY)
        self.model = "mistral-large-latest"

    def chat_with_mistral(self, prompt, conversation_id=None) -> str:
        """
        Send a prompt to Mistral API and receive a response.

        :param prompt: The user message to send.
        :param conversation_id: An optional ID to maintain conversation context.
        :return: The response from Mistral.
        """

        chat_response = self.client.chat.complete(
            model= self.model,
            messages = [
                {
                    "role": "user",
                    "content": prompt,
                },
            ]
        )

        return chat_response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    conversation_id = None
    print("Chat with Mistral! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        mistral_client = MistralChatClient()
        response = mistral_client.chat_with_mistral(user_input, conversation_id)
        if response:
            print("Mistral:", response)
