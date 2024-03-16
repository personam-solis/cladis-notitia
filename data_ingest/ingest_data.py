import global_decorator as gd
import requests
import json
import pandas as pd
import os
from typing import AnyStr, Dict, List, Any


# @gd.log
def gdacs_pull(url: str) -> AnyStr:
    """
    Pull GDACS XML data from the URL and store it in memory

    Args:
        url (str): URL to pull data from

    Returns:
        str: GDACS XML data un-formatted
    """

    try:
        http_response = requests.get(url)
        # Raise error based on status
        http_response.raise_for_status()
        return http_response.text
    except requests.exceptions.HTTPError as error:
        print("HTTP Error!\n{}".format(error.args[0]))
    except requests.exceptions.ReadTimeout as error:
        print("Time out!\n{}".format(error))


# @gd.log
def openfema_pull(url: str, from_date: str) -> List:
    """
    Pull openFEMA data from their API interface and store it in memory

    Args:
        from_date (str): Start date of the data to be collected (YYYY-MM-DD)
        url: Full API base URL

    Returns:
        list: OpenFEMA filtered data as a list with JSON dictionaries
    """

    try:
        api_response = requests.get("{}?$filter=declarationDate gt {}&$format=jsona".format(
            url, from_date))
        # Raise error based on status
        api_response.raise_for_status()
        return json.loads(api_response.text)
    except requests.exceptions.HTTPError as error:
        print("HTTP Error!\n{}".format(error.args[0]))
    except requests.exceptions.ReadTimeout as error:
        print("Time out!\n{}".format(error))


# @gd.log
def emdat_open(filename: str) -> pd.core.frame.DataFrame:
    """
    Open the EM-DAT CSV that is included in the repo. This is obtained manually
    per European Union webpage requirements.

    Args:
        filename (str): Filename to import

    Returns:
        DataFrame: PANDAS Dataframe object
    """

    local_path = os.path.dirname(__file__)
    full_path = os.path.join(local_path, filename)

    try:
        return pd.read_csv(filename, header=0, skip_blank_lines=True,
                           parse_dates=True, date_format="%Y-%m-%d")
    except FileNotFoundError:
        print("FILE WAS NOT FOUND!\n{}".format(full_path))


"""
############################# MAIN #############################
"""


# This module can only be imported
if __name__ == '__main__':

    pass