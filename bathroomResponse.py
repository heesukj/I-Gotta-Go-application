# 
import json
from bathroom import Bathroom

class BathroomResponse:
    ''' Takes the user's inputs and returns filtered and proritized bathrooms based on the user's inquiry '''
    # we need to include the bathroom response to, pass raw bathroom list (json)
    def __init__(self, bathroom_list, has_changing_table):
        # define has_changing_table attribute
        self.has_changing_table = has_changing_table
        # convert JSON string object of a bathroom to Python dictionary 
        self.bathroom_list = json.loads(bathroom_list.content, object_hook=lambda d: Bathroom(**d))         

    def get_bathrooms(self, priortized_by = ''):
        '''Returns the list of filtered bathrooms the prioritized by the option user selected '''
        # print('\nself.bathroom_list[0].changing_table = ', self.bathroom_list[0].changing_table)

        # set raw bathroom list to filtered_bathrooms
        filtered_bathrooms = self.bathroom_list
        
        # filter by has cahnging table if it is set
        if self.has_changing_table:
            filtered_bathrooms = list(filter(lambda bathroom: bathroom.changing_table == True, self.bathroom_list))
        print('\ntype(filtered_bathrooms): ', type(filtered_bathrooms))
        # print('\nfiltered_bathrooms[10].upvote = ',filtered_bathrooms[10].upvote)

        # prioritize bathrooms if priortized_by is set at upvote, directions, or comment
        if priortized_by == 'upvote':
            # sort list by upvote
            filtered_bathrooms.sort(key=lambda bathroom: bathroom.upvote, reverse=True)         # in-place sorting by upvote (int value)

        elif priortized_by == 'directions':          # in-place sorting by directions (string=> find if direction is NOT empty)
        #     # sort list by directions provided
            filtered_bathrooms = sorted(filtered_bathrooms, key=lambda bathroom: bathroom.directions == '')

        elif priortized_by == 'comment':             # in-place sorting by comment (string=> find if comment is NOT empty or None)
            # sort list by comment provided
            filtered_bathrooms = sorted(filtered_bathrooms, key=lambda bathroom: bathroom.comment is None or bathroom.comment == '')

        return filtered_bathrooms
