


# ckanext-traffic_light

The extension will add a picture of a red, yellow or green traffic light to each metadata record. The color indicates the proportion of the filled optional metadata fields for the according record. The picture is furthermore attached to each dataset in the search results.

------------
Requirements
------------

CKAN 2.9 with Python 2.7


---------------
Config settings
---------------

Edit `fields.json` to define which metadata fields should be included in the 
calculation of the percentage of filled optional metadata fields. Don't include any
mandatory field here, since it obviously doesn't make sense. 

It is assumed that this extension is used in conjunction with the [scheming](https://github.com/ckan/ckanext-scheming) extension; therefore, fields can be defined for 
different metadata schemas (The file you download with the extension, defines fields for 
the three metadata schemas `dataset`, `process` and `workflow`.). 
If a metadata record has a schema that is not referenced in 
`fields.json`, it falls back to a default list of keys that is based on the default 
CKAN schema (see `plugin.py`). If you want to always use this fallback keys, just set the content of 
`fields.json` to `{}`. __This (`{}`) is also the minimum content for the files `fields.json` and 
`fields_weighted.json`. If these files are empty or non-existent the extension might stop working.__ 

The general schema of `fields.json` is:

```json
{
    "<metadata_schema_name_1>": [
        "<key_1_of_metadata_schema_1>",
        "<key_2_of_metadata_schema_1>",
        "<key_3_of_metadata_schema_1>",
        ...
    ],
    "<metadata_schema_name_2>": [
        "<key_1_of_metadata_schema_2>",
        "<key_2_of_metadata_schema_2>",
        "<key_3_of_metadata_schema_2>",
        ...
    ],
    ...
}
```

The default content of the file (based on the GeoKur metadata schemas 
https://github.com/GeoinformationSystems/ckanext-scheming, 
https://zenodo.org/record/4916698) is:

```json
{
    "dataset": [
        "license_title",
        "temporal_resolution",
        "spatial_resolution",
        "was_derived_from",
        "theme",
        "tags",
        "is_version_of",
        "is_part_of",
        "notes",
        "quality_metrics",
        "conforms_to",
        "temporal_start",
        "temporal_end",
        "documentation",
        "url"
    ],
    "process": [
        "documentation",
        "used",
        "generated",
        "category",
        "notes"
    ],
    "workflow": [
        "documentation",
        "source_code",
        "rel_processes",
        "rel_datasets",
        "notes"
    ]
}
```

The extensions also provides a reference page that is available at
`<your-ckan-domain>/traffic-light-reference`. Clicking on a traffic
light redirects to this page. The reference page gives information 
about whether or not weights are used in the calculation, at which 
breaking points the traffic light switches color, and which fields 
(and with which weights) are used in the evaluation.

---------------
Advanced Config settings
---------------

### Weights

Users of the extension can specify weights for the metadata fields
that are included in the evaluation. They therefore have to add 
`ckanext.traffic_light.weights = true` to the `ckan.ini`. If weights 
are applied, the extension uses `fields_weighted.json` rather than 
`fields.json`. Conclusively, in this case, the definition of the included 
fields and their weights has to be done in `fields-weighted`. 
The evaluation procedure normalizes the provided weights, so that the 
result is always a value between 0 and 1. The schema of `fields_weighted` 
is as follows:

```json
{
    "<metadata_schema_name_1>": [
        {
            "field_name" : "<key_1_of_metadata_schema_1>",
            "weight": "<weight_of_key_1_of metadata_schema_1>"
        },
        {
            "field_name" : "<key_2_of_metadata_schema_1>",
            "weight": "<weight_of_key_2_of metadata_schema_1>"
        }
        ...
    ],
    "<metadata_schema_name_2>": [
        {
            "field_name" : "<key_1_of_metadata_schema_2>",
            "weight": "<weight_of_key_1_of metadata_schema_2>"
        },
        ...
    ],
    ...
}
```

### Traffic Light Limits

The default limits for the switching of the traffic light (> 0.8: green, > 0.3: yellow)
can be changed in the `ckan.ini`:

```
ckanext.traffic_light.green_limit = 0.9
ckanext.traffic_light.yellow_limit = 0.5
```

### Changing the Images

Traffic lights might not always be a feasible option to represent the metadata provision. 
Users can change the images by replacing the according PNG files in the `public` folder by
files with identical names. If the new images turn out to be wider, users might need to 
adapt the bootstrap-column-with:

In `package/read.html` at line 13 and 18 (`col-sm-<...>`), keep the sum at 12.

In `snippets/package_item.html` at line 5 and 16 (`col-sm-<...>`), keep the sum at 12.



----------------------
Developer installation
----------------------

To install ckanext-traffic_light for development, activate your CKAN virtualenv (`. /usr/lib/ckan/default/bin/activate`) and
do::

    git clone https://github.com/rue-a/ckanext-traffic_light.git
    cd ckanext-traffic_light
    python setup.py develop
    pip install -r dev-requirements.txt

