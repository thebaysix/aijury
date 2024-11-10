import os
from mistralai import Mistral

MISTRAL_API_KEY =  os.environ.get('MISTRAL_API_KEY')

class MistralChatClient:
    """Client which offers and interface through which to chat with Mistral"""

    def __init__(self):
        self.chat_history = []
        self.client = Mistral(api_key=MISTRAL_API_KEY)
        self.model = "mistral-large-latest"

    def chat_with_mistral(self, prompt, conversation_id=None) -> str:
        """
        Send a prompt to Mistral API and receive a response.

        :param prompt: The user message to send.
        :param conversation_id: An optional ID to maintain conversation context.
        :return: The response from Mistral.
        """

        self.chat_history.append(
            {
                "role": "user",
                "content": prompt,
            }
        )
        chat_response = self.client.chat.complete(
            model=self.model,
            messages=self.chat_history
        )

        chat_response_message = chat_response.choices[0].message
        self.chat_history.append(chat_response_message)
        return chat_response_message.content

# Example usage
if __name__ == "__main__":
    conversation_id = None
    mistral_client = MistralChatClient()
    print("Chat with Mistral! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = mistral_client.chat_with_mistral(user_input, conversation_id)
        if response:
            print("Mistral:", response)
