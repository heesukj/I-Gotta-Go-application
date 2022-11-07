import requests

class BathroomSearch:
    ''' Search bathrooms based on the user's selections in the search location, unisex, ADA accessible and has changing table and 
    return a list of bathroom by calling Refuge Restrooms API'''

    def __init__(self, search_location, unisex, ada_accessible):
        ''' takes the search inputs '''
        self.search_location = search_location
        self.unisex = unisex
        self.ada_accessible = ada_accessible

    def run_query(self):
        ''' Return a list of bathrooms as the response for the GET requst to the following url API 
        with the dynamic parameters of search location, unisex and ada_accessible '''

        url = 'https://www.refugerestrooms.org/api/v1/restrooms/search?page=1&per_page=20&offset=0'
        url = url + '&query='+ self.search_location
        if self.unisex:
            url = url + '&unisex=true'
        if self.ada_accessible:
            url = url + '&ada=true'

        # sends GET request, requests call API of this url, and saves the response to bathroom_response object
        bathroom_response = None
        error_msg = None

        # sent GET request to Refuge Restrooms URL, if not being responsive, splits out the following error message
        try:
            bathroom_response = requests.get(url)
        except:
            error_msg = "Something went wrong. Try again."

        return bathroom_response, error_msg
