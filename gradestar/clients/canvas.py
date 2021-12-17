from canvasapi.canvas import Canvas
from canvasapi.paginated_list import PaginatedList
import logging
import pathlib

import appdirs


from gradestar.clients.client import Client

class CanvasClient(Client):

    def __init__(self, base_url="", api_key="", *args, **kwargs):
        """
        Client for interacting with Canvas via its REST API
        
        """
        super().__init__(base_url, api_key, *args, **kwargs)
        self._client = Canvas(self._base_url, self._api_key)
    
    
    def get_courses(self, *args, **kwargs):
        return self._parse(self._retrieve_courses(*args, **kwargs), *args, **kwargs)
    
    def _retrieve_courses(self, *args, **kwargs):
        return self._client.get_courses()    

    def _parse(self, input,  *args, **kwargs):
        if type(input) == PaginatedList:
            return self._parse_paginated_list(input, *args, **kwargs)
        else:
            logging.error("Uanble to parse Canvas data")
    
    def _parse_paginated_list(self, input, *args, **kwargs):
        output = []
        for item in input:
            dict = item.__dict__
            dict.pop("_requester")
            output.append(dict)
        
        return output


def GetClient(url, api_key, *args, **kwargs):
    return CanvasClient(url, api_key)