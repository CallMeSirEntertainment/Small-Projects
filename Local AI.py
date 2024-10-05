import requests
import json
from time import sleep
from os import system, name

def send_request(message):
    payload = {
        "messages": [
            { "role": "system", "content": system_prompt },
            { "role": "user", "content": message }
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url + "chat/completions", headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Request failed with status code " + str(response.status_code)}

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        system("cls" if name == "nt" else "clear")
        print("Generating...")
        response = send_request(user_input)
        system("cls" if name == "nt" else "clear")
        bot_response = response.get("choices")[0].get("message").get("content") if response.get("choices") else "ERROR: Could not fetch response."
        print("Bot:", bot_response)

if input("Welcome to the local AI chatbot by CallMeSirEntertainment!\nInput 'help' for use instructions or press enter to continue.\n").lower() == "help":
    system("cls" if name == "nt" else "clear")
    input("Thank you for using my program! The first step to getting it working is to download LM Studio. You can download it at this link: https://lmstudio.ai/\n\nAfter you go through the installation process, you need to install an AI model. To do this, go to the magnifying glass shaped icon to go into the 'Discover' tab.\nOnce you're there, you can choose an AI model to install. LM Studio will tell you if the model will work well on your device based on your hardware.\n\nAfter the model is installed, make sure that the setting on the bottom of the screen is set to 'Developer'. This will allow you to host a server on localhost.\n\nAfter you do that, go to the 'Developer' tab. It looks like a green box with a '>_' on it. Next, load a model and make sure you turn on 'Enable CORS'.\nThen, configure your port number. When you're done with all that, you can press the green button to start the server.\n\nYou're now ready to use my program!\nIf you have any other questions, please feel free to contact my at @callmesirentertainment on Discord or email me at callmesirentertainment@outlook.com.\nEnjoy!\n\n(Press enter to continue.)")
system("cls" if name == "nt" else "clear")
port_number = input("Please enter the localhost port number for this conversation.\n")
url = f"http://localhost:{port_number}/v1/"
system_prompt = input("\nPlease enter the custom system prompt for this conversation, or press enter to use the default.\n")
if system_prompt == "":
    system_prompt = f"You are speaking to a user who is called by the name of '{input("Please enter the nickname that the AI will call you for this conversation.\n")}'. Your goal is to respect an fulfill their queries."
print("\nInitializing connection...")
try:
    requests.get(url + "models")
except Exception as e:
    print(f"\nThere was an error initializing the connection.\nPlease make sure that the server is running and that the localhost port ({port_number}) is correct and in the range of 0 to 65535.")
    sleep(15)
    exit()
system("cls" if name == "nt" else "clear")
if __name__ == "__main__":
    main()