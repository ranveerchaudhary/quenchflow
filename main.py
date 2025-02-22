import sys
import requests

def quenchflow(USER_KEY, API_TOKEN):
    requests.post("https://api.pushover.net/1/messages.json", data={
    "token":  API_TOKEN,
    "user": USER_KEY,
    "message": "quenchflow triggered"
})

if len(sys.argv) == 3:
    quenchflow(sys.argv[1], sys.argv[2])
else:
    print("Invalid arg length :", len(sys.argv))
    print("Script failed")
