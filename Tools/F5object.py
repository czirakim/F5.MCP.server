"""
    this is a class for create,update,list or delete and object on an F5 device.
    It uses the  iControl REST API to make  requests to the F5 device.
   
"""

import os
from dotenv import load_dotenv
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Specify the path to the .env file
env_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(env_path)  # load environment variables from .env


# F5 device
IP_ADDRESS = os.getenv('IP_ADDRESS')
# Auth string
API_string = os.getenv('Authorization_string')

headers = {
    'Authorization': f'Basic {API_string}',
    'Content-Type': 'application/json'
   }

class F5_object:
    
    """this is a class for create action. It can create virtuals,pools,irules and profiles.
    It uses the  iControl REST API to make POST requests to the F5 device and sends data as a payload.
    
    """

    def __init__(self, **kwargs):
        """Initialize the F5list class with the specified parameters using kwargs."""
        self.payload = kwargs.get('url_body', None)
        self.object_type = kwargs.get('object_type', None)
        self.object_name = kwargs.get('object_name', None)
        self.lines_number = kwargs.get('lines_number', None)
    
    def stats(self):
        """This tool shows the stats of an object from an F5 device using the iControl REST API.         
    
        Args:
            object_name is the name of the object. 
            object_type is the type of the object to be created. It can be : virtual,pool,irule or profile.
                    
        """

        url = f"https://{IP_ADDRESS}/mgmt/tm/ltm/{self.object_type}/{self.object_name}/stats"
        

        try:
            response = requests.request("GET", url, headers=headers, verify=False, timeout=20)
            response.raise_for_status()   
        except requests.exceptions.HTTPError:
            if (response.status_code == 400 or response.status_code == 404):
                return f"An error occurred while making the request: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text
        
    def logs(self):
        """ This tool shows the lines_number of logs from an F5 device using the iControl REST API.         
    
        Args:
            lines_number is the number of lines to be returned.
                    
        """ 

        url = f"https://{IP_ADDRESS}/mgmt/tm/util/bash"
        
        payload = {
            'command': 'run',
            'utilCmdArgs': f"-c 'cat /var/log/ltm | tail -n {self.lines_number}'"
        }

        try:
            response = requests.request("POST", url, headers=headers, json=payload, verify=False, timeout=20)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            if (response.status_code == 400 or response.status_code == 404):
                return f"An error occurred while making the request: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text
        

    def list(self):
        """This tool lists an object on an F5 device using the iControl REST API.         
    
        Args:
            object_name is the name of the object. 
            object_type is the type of the object to be created. It can be : virtual,pool,irule or profile.
                    
        """

        url = f"https://{IP_ADDRESS}/mgmt/tm/ltm/{self.object_type}/{self.object_name}"
        # Convert input_data dictionary to JSON string
        #json_payload = str(self.payload).replace("'", '"')  # Ensures proper JSON formatting

        try:
            response = requests.request("GET", url, headers=headers, verify=False, timeout=20)
            response.raise_for_status()   
        except requests.exceptions.HTTPError:
            if (response.status_code == 400 or response.status_code == 404):
                return f"An error occurred while making the request: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text
        
    def create(self):
        """This tool creates an object on an F5 device using the iControl REST API.         
    
        Args:
            url_body is the configuration of teh object.
            object_type is the type of the object to be created. It can be : virtual,pool,irule or profile.
                    
        """

        url = f"https://{IP_ADDRESS}/mgmt/tm/ltm/{self.object_type}/"

        try:
            response = requests.request("POST", url, headers=headers, json=self.payload, verify=False, timeout=20)
            response.raise_for_status()   
        except requests.exceptions.HTTPError:
            if (response.status_code == 400 or response.status_code == 404):
                return f"An error occurred while making the request: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text
        
    def update(self):
        """ This tool updates an object on an F5 device using the iControl REST API.

        Args:
            url_body is the configuration of teh object.
            object_type is the type of the object to be created. It can be : virtual,pool,irule or profile.
            object_name is the name of teh object to be updated.                       

        """

        url = f"https://{IP_ADDRESS}/mgmt/tm/ltm/{self.object_type}/{self.object_name}"

        try:
            response = requests.request("PATCH", url, headers=headers, json=self.payload, verify=False, timeout=20)
            response.raise_for_status()           
        except requests.exceptions.HTTPError:
            if (response.status_code == 400 or response.status_code == 404):
                return f"An error occurred while making the request: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text    

    def delete(self):
        """ This tool deletes an object from an F5 device using the iControl REST API.

        Args:
            object_type is the type of the object to be created. It can be : virtual,pool,irule or profile.                      
            object_name is the name of teh object to be deleted.
        """

        url = f"https://{IP_ADDRESS}/mgmt/tm/ltm/{self.object_type}/{self.object_name}"

        try:
            response = requests.request("DELETE", url, headers=headers, verify=False, timeout=20)
            response.raise_for_status()           
        except requests.exceptions.HTTPError:
            if (response.status_code == 400 or response.status_code == 404):
                return f"An error occurred while making the request: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text   
