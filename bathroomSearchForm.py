from wtforms import Form, StringField, BooleanField, RadioField
from wtforms.validators import InputRequired


class BathroomSearchForm(Form):
    ''' Contains a form inherited from the parent class Form, which is built-in functions provided by Flask '''

    # this field is required, the UI shows error if it's blank
    location_input = StringField('Enter a Search Location', validators=[InputRequired()])
    
    unisex = BooleanField('Unisex')
    ada_accessible = BooleanField('ADA Accessible')
    changing_table = BooleanField('Changing Table')
    radio_options = RadioField('Prioritize By:', choices=[('upvote', 'Most Upvotes'), ('directions', 'Includes Directions'), ('comment', 'Includes Comments')])

