import global_decorator as gd
import requests
from typing import AnyStr, Dict, List


def gdacs_pull(url: str) -> AnyStr:
    """
    Pull GDACS XML data from the URL and store it in memory

    Args:
        url (str): URL to pull data from

    Returns:
        str: GDACS XML data
    """

    http_response = requests.get(url)

    return http_response.text



# This module can only be imported
if __name__ == '__main__':

    pass

"""
############################# MAIN #############################
"""


# Only run if executing, not import
if __name__ == '__main__':

    pass
