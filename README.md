


# ckanext-traffic_light

The extension will add a picture of a red, yellow or green traffic light to each metadata record. The color indicates the proportion of the filled optional metadata fields for the according record. The picture is furthermore attached to each dataset in the search results.

------------
Requirements
------------

CKAN 2.9 with Python 2.7


---------------
Config settings
---------------

Edit `keys_included.json` to define which metadata fields should be included in the 
calculation of the percentage of filled optional metadata fields. Don't include any
mandatory field here, since it obviously doesn't make sense. Fields can be defined for 
differnet metadata schemas (The file you download with the extension, defines fields 
that are included in the calculation for the three different metadata schemas `dataset`,
`process` and `workflow`.). If a metadataset has a schema that is not reference in 
`keys_included.json`, it falls back to a default list of keys that is based on the default 
CKAN schema. If you want to always use this fallback keys, just set the content of 
`keys_included.json` to `{}`. The general schema of `keys_included.json` is:

```json
{
    "<metadata_schema_name_1>": [
        "key_1_of_metadata_schema_1",
        "key_2_of_metadata_schema_1",
        "key_3_of_metadata_schema_1",
        ...
    ],
    "<metadata_schema_name_2>": [
        "key_1_of_metadata_schema_2",
        "key_2_of_metadata_schema_2",
        "key_3_of_metadata_schema_2",
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


----------------------
Developer installation
----------------------

To install ckanext-traffic_light for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/rue-a/ckanext-traffic_light.git
    cd ckanext-traffic_light
    python setup.py develop
    pip install -r dev-requirements.txt

