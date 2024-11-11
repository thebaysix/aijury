# aijury

Using Mistral, simulates a jury deliberation of a criminal case.

# Set up

1. Clone the repo

2. Create an empty file in the root of the repo called ".env"

3. Using your Mistral AI account (creating one if you need), generate an API Key: https://docs.mistral.ai/getting-started/quickstart/#getting-started-with-mistral-ai-api

4. Copy the generated API key and paste it in .env as follows: `MISTRAL_API_KEY={your_key}`

5. Using VS Code, Debug the agent_chat.py file. The deliberation will print out in the terminal.

# Example:

Sample:
```
PS C:\Code\aijury>  c:; cd 'c:\Code\aijury'; & 'c:\Code\aijury\venv\Scripts\python.exe' 'c:\Users\lgwst\.vscode\extensions\ms-python.debugpy-2024.8.0-win32-x64\bundled\libs\debugpy\adapter/../..\debugpy\launcher' '54334' '--' 'C:\Code\aijury\agent_chat.py'
Starting agent conversation...
Mistral says: Understood. Please provide the case details and assign me a juror ID and personality so I can contribute to the deliberation accordingly.
Mistral says: [JUROR_1] The Foreman says: "Alright, let's begin our deliberation. We've heard both sides, and it's our job to weigh the evidence and arguments presented. Let's start by discussing the security footage and what it shows. What are your thoughts on that? I'd like to hear from JUROR_2 first."

PROPOSED NEXT SPEAKER: JUROR_2
Mistral says: [JUROR_12] The Devil's Advocate Juror says: "I think we need to be careful about how much we rely on that footage. It's grainy, there's no audio, and it's partially obscured. Plus, it doesn't show what led up to the altercation. How can we be sure who the initial aggressor was based on that alone? I'd like to hear more about what the witnesses had to say. Let's not rush to judgment here. What do you think, JUROR_3?"

PROPOSED NEXT SPEAKER: JUROR_3
```