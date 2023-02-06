import requests
import json

# Get the config file
try:
    with open("config.json", 'r') as f:
        config = json.load(f)
# If the file doesn't exist or it's not valid
except (FileNotFoundError, json.JSONDecodeError):
    config = {}

while True:
    # If the token is not in the config file
    if "token" not in config:
        print("Enter your bot token:")
        config["token"] = "MTA3MjEzODUxNTg3NTM3NzI1NA.G-8iUS.ImyYiRjjcMCVSjdrsuSIQWhGuoAFCT0pZiwNs4"
    # Check if the token is valid
    token = config["token"]
    head = {
        "Authorization": f"Bot {token}"
    }
    try:
        data = requests.get(
            "https://discord.com/api/v10/users/@me", headers=head).json()
    except requests.exceptions.RequestException as e:
        if e.__class__ == requests.exceptions.ConnectionError:
            exit(f"ConnectionError: Discord is blocked on public networks, make sure you can access https://discord.com")
        elif e.__class__ == requests.exceptions.Timeout:
            exit(f"Timeout: Connecting to Discord APIs took too long (Are you rate limited?)")
        exit(f"Unknown error! Further information:\n{e}")
    # If the token is valid, break the loop
    if "id" in data:
        break
    # If the token is not valid, ask again
    print(f"Invalid token! Re-enter token: ")
    config.pop("token", None)

# Save the token
if "volume" not in config:
    print("Insert volume default (0-200): ")
    volume = int(input("> "))
    while volume <= 0 or volume > 200:
        print("The volume must be between 0 and 200. Reinsert volume: ")
        volume = input("> ")
    config["volume"] = volume / 200
    
if "youtubeApiKey" not in config:
    print("Insert Youtube API key: ")
    youtubeApiKey = input("> ")
    config["youtubeApiKey"] = youtubeApiKey
    
def get_config():
    return config["token"], config["volume"]

def get_youtube_api_key():
    return config["youtubeApiKey"]

with open("config.json", "w") as f:
    f.write(json.dumps(config, indent=4))