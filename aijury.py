import requests

# Replace 'YOUR_API_KEY' with your actual Mistral API key.
API_KEY = 'YOUR_API_KEY'
API_URL = 'https://api.mistral.ai/v1/chat'

# Set up headers with the API key.
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def chat_with_mistral(prompt, conversation_id=None):
    """
    Send a prompt to Mistral API and receive a response.

    :param prompt: The user message to send.
    :param conversation_id: An optional ID to maintain conversation context.
    :return: The response from Mistral.
    """
    data = {
        "prompt": prompt,
        "conversation_id": conversation_id  # Optional, for maintaining context.
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        response_json = response.json()
        # Extract and print Mistral's response from the JSON.
        response_text = response_json.get("response", "No response text found.")
        new_conversation_id = response_json.get("conversation_id", conversation_id)
        return response_text, new_conversation_id
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None, None

# Example usage
if __name__ == "__main__":
    conversation_id = None
    print("Chat with Mistral! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response, conversation_id = chat_with_mistral(user_input, conversation_id)
        if response:
            print("Mistral:", response)
