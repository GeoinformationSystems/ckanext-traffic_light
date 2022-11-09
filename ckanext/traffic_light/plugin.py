import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import os
import inspect
import json

DEFAULT_KEYS =  ["author", "author_email", "license_title",
        "notes", "url", "tags", "extras"]

def load_json(json_name):
    json_contents = None
    module = 'ckanext.traffic_light'
    try:
        # __import__ has an odd signature
        m = __import__(module, fromlist=[''])
    except ImportError:
        return None
    p = os.path.join(os.path.dirname(inspect.getfile(m)), json_name)
    if os.path.exists(p):
        with open(p) as file:    
            json_contents = json.load(file)
    return json_contents
    

def evaluate_fields(pkg):
    schema = None
    weights = apply_weights()
    if weights:
        schema = load_json('fields_weighted.json')
    else:
        schema = load_json('fields.json')

    # select subset of keys based on package type
    try: 
        fields = schema[pkg['type']]
    # use fallback if no matching type was found
    except KeyError :
        fields = DEFAULT_KEYS
        weights = False

    if weights:
        max_value = 0
        filled_value = 0
        for field in fields:
            max_value = max_value + field["weight"]
            if field["field_name"] in pkg:
                if pkg[field["field_name"]]:
                    filled_value = filled_value + field["weight"] 
        return float(filled_value)/float(max_value)
    else:
        filled_fields = 0
        for key in fields:
            # check if key exists
            if key in pkg:
                # check if key has value (None, "", [] and {} are
                # evaluated as false in python)
                if pkg[key]:
                    filled_fields = filled_fields + 1
        percentage = 0
        # this if is only for safty reasons
        if len(fields):
            percentage = (float(filled_fields)/float(len(fields)))
        return percentage

def apply_weights():
    # toolkit.config.get(...) reads value of "ckanext.traffic_light.weights" 
    # from ckan.ini and sets value to false if no variable is provided.

    # toolkit.asbool(...) evaluates a string as bool.

    # with try ... except ValueError we catch typos from ckan.ini, e.g.,
    # "ckanext.traffic_light = fasle" and set the variable to False in case.

    try:
        return toolkit.asbool(toolkit.config.get('ckanext.traffic_light.weights', 'false'))
    except ValueError:
        return False

def get_yellow_limit():
    try:
        return float(toolkit.config.get('ckanext.traffic_light.yellow_limit', '0.3'))
    except ValueError:
        return 0.3

def get_green_limit():
    try:
        return float(toolkit.config.get('ckanext.traffic_light.green_limit', '0.8'))
    except ValueError:
        return 0.8

class TrafficLightPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # implement ITemplateHelpers interface 
    # (to register new helper fucntions)
    plugins.implements(plugins.ITemplateHelpers)

    # implement IDatasetForm interface 
    # (to access the dataset schemes)
    # plugins.implements(plugins.IDatasetForm)


    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'traffic_light')
    
    # get_helpers() is a method from ITemplateHelpers
    def get_helpers(self):
        '''register the evaluate_fields() function
        as a template helper function.'''

        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {
            'traffic_light_evaluate_fields': evaluate_fields,
            'traffic_light_apply_weights': apply_weights,
            'traffic_light_get_yellow_limit': get_yellow_limit,
            'traffic_light_get_green_limit': get_green_limit
        }

