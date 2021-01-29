import requests
import json
import ipaddress

import config
from geo_api.models.geo_data_model import GeoDataModel

def build_geo_data(adress: string):
    '''
    Helper function used for GeoData creation. FactoryPattern.

    Args:
        Adress (str): IP or domain adress. Base adresses allowed only.

    Returns:
        Configured GeoDataModel object
    '''

    if not validators.domain(adress) and not is_proper_ip:
        raise ValueError("Adress is not valid domain or ip adress")

    r = requests.get(f"{config.ipstack_API_ADRESS}/{adress}?access_key={config.ipstack_API_KEY}")

    if r.status_code != 200:
        raise Exception("External API not available")

    api_response = json.loads(r.text)

    item = GeoDataModel(
            adress, 
            api_response['type'],  
            api_response['continent_name'],  
            api_response['country_name'], 
            api_response['region_name'],  
            api_response['latitude'],  
            api_response['longitude']
        )

    return item


def is_proper_ip(adress)
    '''
    Validator for IP adress

    Args:
        Adress (str): IPv4 or IPv6. Base adresses allowed only.

    Returns:
        True/False
    '''

    try:
        ip = ipaddress.ip_address(adress)
        return True
    except ValueError:
        return False
