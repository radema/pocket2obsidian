import os
import webbrowser

import requests

"""Script to build pocket client access method"""


class PocketClient:
    """
    Class to request data from Pocket App
    """

    CONSUMER_KEY = os.getenv("WEB_CONSUMERKEY")
    REDIRECT_URI = os.getenv("REDIRECT_URI")

    def makeLoginRequest(self):
        """
        Make Login Request based on oauth method
        Return:
            - access_token, str
        """

        REQUEST_URL = "https://getpocket.com/v3/oauth/request"
        ACCESS_URL = "https://getpocket.com/v3/oauth/authorize"

        LoginRequest = requests.get(
            REQUEST_URL,
            {"consumer_key": self.CONSUMER_KEY, "redirect_uri": "www.google.it"},
        )
        REQUEST_TOKEN = LoginRequest.text.replace("code=", "")
        OAUTH_URL = (
            "https://getpocket.com/auth/authorize?request_token="
            + REQUEST_TOKEN
            + "&redirect_uri="
            + self.REDIRECT_URI
        )
        webbrowser.open(OAUTH_URL)
        input("Press anything...")
        return (
            requests.get(
                ACCESS_URL, {"consumer_key": self.CONSUMER_KEY, "code": REQUEST_TOKEN}
            )
            .text.replace("access_token=", "")
            .split("&")[0]
        )

    def makeRequest(self, access_token, n_items=10):
        """
        Make Request to retrieve data from Pocket API
        Return:
            - data in json format
        """
        URL = "https://getpocket.com/v3/get"

        data = requests.get(
            URL,
            params={
                "consumer_key": self.CONSUMER_KEY,
                "access_token": access_token,
                "state": "unread",
                "contentType": "article",
                "sort": "newest",
                "count": n_items,
                "detailType": "simple",
            },
        )
        return data.json()

    def __init__(self) -> None:
        "Init function"
        pass
