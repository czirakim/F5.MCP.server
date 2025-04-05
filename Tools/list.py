"""
    this is a class for list action. It can list vips,pools,irules nad profiles.
    It uses the F5 REST API to make GET requests to the F5 device.
    It reads the names of the vip,pool,irule or profile and makes a GET request to the F5 device 
   
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

class F5list:
    
    """this is a class for list action. It can list vips,poolsm,irules nad profiles.
    It uses the F5 REST API to make GET requests to the F5 device.
    It reads the names of the vip,pool,irule or profile and makes a GET request to the F5 device """

    def __init__(self, **kwargs):
        """Initialize the F5list class with the specified parameters using kwargs."""
        self.vip_name = kwargs.get('vip_name', None)
        self.pool_name = kwargs.get('pool_name', None)
        self.irule_name = kwargs.get('irule_name', None)
        self.profile_type = kwargs.get('profile_type', None)
        self.profile_name = kwargs.get('profile_name', None)


    def list_vip(self):
        """Make a request to the F5 API with proper error handling.
        The vip name should be a string and not a list of string.     
    
        Args:
            vip_name (str): The name of the virtual server. If vip_name is empty, all virtual servers will be listed.
        """

        # make the request 
        if (self.vip_name in ['', None, 'all']): 
            url = f"https://{IP_ADDRESS}/mgmt/tm/ltm/virtual/"
        else:
            url = f"https://{IP_ADDRESS}/mgmt/tm/ltm/virtual/{self.vip_name}"
        try:
            response = requests.request("GET", url, headers=headers, verify=False, timeout=20)
            response.raise_for_status()
            formatted_json = response.json()
        except requests.exceptions.HTTPError:
            if (response.status_code == 404 or response.status_code == 400):
                return f"An error occurred while making the request:  {response.text}"            
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:        
            return response.text
        
    def list_pool(self):
        """Make a request to the F5 API with proper error handling.
        The pool name should be a string and not a list of string.     
    
        Args:
            pool_name (str): The name of the pool of servers/nodes. If pool_name is empty or None, all pools  will be listed.
        """
    
        # make the request
        if (self.pool_name in ['', None, 'all']): 
            url = f"https://{IP_ADDRESS}/mgmt/tm/ltm/pool/"
        else:
            url = f"https://{IP_ADDRESS}/mgmt/tm/ltm/pool/{self.pool_name}/members"

        try:
            response = requests.request("GET", url, headers=headers, verify=False, timeout=20)
            response.raise_for_status()
            formatted_json = response.json()
        except requests.exceptions.HTTPError:
            if (response.status_code == 400 or response.status_code == 404):
                return f"An error occurred while making the request: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text
    
    def list_irule(self):
        """Make a request to the F5 API with proper error handling.
        The irule name should be a string and not a list of string.     
    
        Args:
            irule_name (str): The name of the irule . If irule_name is empty or None, all irules  will be listed.
        """
             
        # make the request
        if (self.irule_name in ['', None, 'all']): 
            url = f"https://{IP_ADDRESS}/mgmt/tm/ltm/rule/"
        else:
            url = f"https://{IP_ADDRESS}/mgmt/tm/ltm/rule/{self.irule_name}" 
        try:
            response = requests.request("GET", url, headers=headers, verify=False)
            response.raise_for_status()
            formatted_json = response.json()
        except requests.exceptions.HTTPError:
            if (response.status_code == 404 or response.status_code == 400):
                return f"An error occurred while making the request:  {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text

    def list_profile(self):
        """Make a request to the F5 API with proper error handling.
        The profile name should be a string and not a list of string.
        The profile type should be a string and not a list of string.    
    
        Args:
            profile_type (str): The type of the profile . 
            profile_name (str): The name of the profile .
        If profile is empty or None, all profiles of the specific type will be listed.
        """
    
        base_url = f"https://{IP_ADDRESS}/mgmt/tm/ltm/profile"

        # make the request
        if (self.profile_name in ['', None,'all']): 
            url = f"{base_url}/{self.profile_type}"
        else:
            url = f"{base_url}/{self.profile_type}/{self.profile_name}"
        try:
            response = requests.request("GET", url, headers=headers, verify=False)
            response.raise_for_status()
            formatted_json = response.json()
        except requests.exceptions.HTTPError:
            if (response.status_code == 404 or response.status_code == 400):
                return f"An error occurred while making the request:  {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text
        