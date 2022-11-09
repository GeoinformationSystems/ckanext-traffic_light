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
    

def percentage_of_filled_fields(pkg):
    keys_included = load_json('fields.json')

    # select subset of keys based on package type
    try: 
        keys_included = keys_included[pkg['type']]
    # use fallback if no matching type was found
    except KeyError :
        keys_included = DEFAULT_KEYS

    filled_fields = 0
    for key in keys_included:
        # check if key exists
        if key in pkg:
            # check if key has value (None, "", [] and {} are
            # evaluated as false in python)
            if pkg[key]:
                filled_fields = filled_fields + 1

    percentage = 0
    # this if is only for safty reasons
    if len(keys_included):
        percentage = (float(filled_fields)/float(len(keys_included)))*100

    return percentage


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
        '''register the percentage_of_filled_fields() function
        as a template helper function.'''

        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'traffic_light_percentage_of_filled_fields': percentage_of_filled_fields}
