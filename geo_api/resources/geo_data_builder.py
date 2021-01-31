import requests
import json
import ipaddress

import config
from geo_api.models.geo_data_model import GeoDataModel

def build_geo_data(address: string):
    '''
    Helper function used for GeoData creation. FactoryPattern.

    Args:
        address (str): IP or domain address. Base addresses allowed only.

    Returns:
        Configured GeoDataModel object
    '''

    if not validators.domain(address) and not is_proper_ip:
        raise ValueError("address is not valid domain or ip address")

    r = requests.get(f"{config.ipstack_API_address}/{address}?access_key={config.ipstack_API_KEY}")

    if r.status_code != 200:
        raise Exception("External API not available")

    api_response = json.loads(r.text)

    item = GeoDataModel(
            address, 
            api_response['type'],  
            api_response['continent_name'],  
            api_response['country_name'], 
            api_response['region_name'],  
            api_response['latitude'],  
            api_response['longitude']
        )

    return item


def is_proper_ip(address)
    '''
    Validator for IP address

    Args:
        address (str): IPv4 or IPv6. Base addresses allowed only.

    Returns:
        True/False
    '''

    try:
        ip = ipaddress.ip_address(address)
        return True
    except ValueError:
        return False
