'''
Given the provided cars dict:

1. Get all Jeeps
2. Get the first car of every manufacturer.
3. Get all vehicles containing the string "Trail" in their names (should work for other grep too)
4. Sort and output dict alphabetically (both keys and values)

See the docstrings and tests for more details.
'''


from cars import (get_all_jeeps, get_first_model_each_manufacturer,
                  get_all_matching_models, sort_dict_alphabetically)

def test_get_all_jeeps():
    expected = 'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'
    actual = get_all_jeeps()
    assert type(actual) == str
    assert actual == expected

def test_get_first_model_each_manufacturer():
    actual = get_first_model_each_manufacturer()
    expected = ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
    assert actual == expected

def test_get_all_matching_models():
    expected = ['Trailblazer', 'Trailhawk']
    assert get_all_matching_models() == expected
    expected = ['Accord', 'Commodore', 'Falcon']
    assert get_all_matching_models(grep='CO') == expected

def test_sort_dict_alphabetically():
    actual = sort_dict_alphabetically()
    expected = {
        'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
        'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
        'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
        'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk'],
        'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
    }
    assert actual == expected
