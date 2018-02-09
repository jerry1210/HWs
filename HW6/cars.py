'''
Given the provided cars dict:

1. Get all Jeeps
2. Get the first car of every manufacturer.
3. Get all vehicles containing the string "Trail" in their names (should work for other grep too)
4. Sort and output dict alphabetically (both keys and values)

See the docstrings and tests for more details.
'''


cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

def get_all_jeeps():
    """return a comma separated list of jeep models (original order)"""
    return ', '.join(cars.get("Jeep"))

def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    return [cars[m][0] for m in cars]

def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    return sorted([item for car in cars for item in cars[car] if grep.lower() in item.lower()])

def sort_dict_alphabetically():
    """sort both keys and values of cars returning resulting dict"""
    return {key: sorted(cars[key]) for key in sorted(cars)}

