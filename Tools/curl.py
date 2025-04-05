import os
from dotenv import load_dotenv
import subprocess


# Specify the path to the .env file
env_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(env_path)  # load environment variables from .env


# F5 device
IP_ADDRESS = os.getenv('IP_ADDRESS')
# Auth string
API_string = os.getenv('Authorization_string')

url = f"https://{IP_ADDRESS}/mgmt/tm/ltm/pool/"

def curl_tool(input_data):
    """
    Executes a curl POST request with the provided input_data.

    Args:
        input_data (dict): The JSON payload for the POST request.

    Returns:
        tuple: A tuple containing stdout and stderr from the curl command.
    """
    # Convert input_data dictionary to JSON string
    json_payload = str(input_data).replace("'", '"')  # Ensures proper JSON formatting

    # The command you would type in the terminal
    command = [
        "curl",
        "-X", "POST",
        "-H", "Content-Type: application/json",
        "-H", f"Authorization: Basic " + f"{API_string}",
        "-kvvv",
        url,
        "-d", json_payload
        ]


    # Run the command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Get the output and error message (if any)
    output = result.stdout
    error = result.stderr

    # Check if it was successful
    if result.returncode == 0:
        return(f"Success: {output}")
    else:
        return(f"Error: {output}")

