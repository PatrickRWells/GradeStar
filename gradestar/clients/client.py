class Client:
    
    def __init__(self, base_url: str, api_key: str, *args, **kwargs):
        """
        Base class for interacting with online
        grade management tools using a REST API
        """
        self._base_url = base_url
        self._api_key = api_key
        