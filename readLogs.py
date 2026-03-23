import requests
import time

url = "https://accontroller-85b47-default-rtdb.firebaseio.com/command.json"

# while True:
#     try:
#         response = requests.get(url)

#         if response.status_code == 200:
#             command = response.json()
#             print("Command:", command)

#         else:
#             print("Error:", response.status_code)

#     except Exception as e:
#         print("Request failed:", e)

#     time.sleep(5)  #

# def toggle():
#     # Get current state
#     response = requests.get(url)
#     current = response.json()

#     # Toggle
#     new_state = "off" if current == "on" else "on"

#     # Send new state
#     requests.put(url, json=new_state)

#     print(f"Toggled: {current} → {new_state}")

# toggle()

import requests
from datetime import datetime

url = "https://accontroller-85b47-default-rtdb.firebaseio.com/logs.json"

data = requests.get(url).json()

for key, value in data.items():
    t = datetime.fromtimestamp(value["time"] / 1000)

    state = value.get("state", "unknown")
    source = value.get("source", "unknown")

    print(f"{t} | {state} | {source}")
