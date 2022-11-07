from bathroomSearchForm import BathroomSearchForm
from bathroomSearch import BathroomSearch
from bathroomResponse import BathroomResponse

# each class doesn one job: main.py-does only routing (try to have main.py less dependencies), this class - does functionality
class Service:
    ''' Returns locations, form, and number of locations
    backend code take cares of any works need to be done for returning bathroom response '''

    def index_route(self, request):   # request = GET or POST
        location_input = ''
        ada_accessible = False
        bathrooms = []
        error_msg = None    # initialize the error_msg to be None

        # sends a form request to IGottaGo API and saves the response to the form object 
        form = BathroomSearchForm(request.form) 

        # the code below represents user's form data
        if request.method == "POST":
            # print('request.form', request.form)

            location_input = form.data['location_input']   # access to the location data
            unisex = form.data["unisex"]                   # access to the unisex data
            # print('unisex: ', unisex)
            ada_accessible = form.data["ada_accessible"]  # if ada-accessible is checked then empty string is return otherwise (unchecked) None is returned
            # print('ada_accessible: ', ada_accessible) 
            changing_table = form.data["changing_table"]  # access to the changing_table data
            # print('changing_table: ', changing_table)
            prioritized_by = form.data["radio_options"]   # access to one of the options in the radio button data
            # print('prioritized_by: ', prioritized_by)

            # get a list of bathrooms (response) from Refuge Restroom API by calling run_query() with the user's selections of search location, unisex and/or ADA accessible
            bathroom_search = BathroomSearch(location_input, unisex, ada_accessible)
            bathroom_response, error_msg = bathroom_search.run_query()

            # if error_msg is None, run the following code return no error_msg (as None), otherwise return error_msg with msg set up in the BathroomSearch class
            if error_msg == None:
                # once you get the bathroom list above, get the filtered and prioritized bathroom list and return locations, form, and num_locations
                list_bathroom = BathroomResponse(bathroom_response, changing_table)
                bathrooms = list_bathroom.get_bathrooms(prioritized_by)

        locations = bathrooms
        num_locations = len(locations)

        return locations, form, num_locations, error_msg
        