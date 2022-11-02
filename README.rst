.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/rue-a/ckanext-traffic_light.svg?branch=master
    :target: https://travis-ci.org/rue-a/ckanext-traffic_light

.. image:: https://coveralls.io/repos/rue-a/ckanext-traffic_light/badge.svg
  :target: https://coveralls.io/r/rue-a/ckanext-traffic_light

.. image:: https://img.shields.io/pypi/v/ckanext-traffic_light.svg
    :target: https://pypi.org/project/ckanext-traffic_light/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/ckanext-traffic_light.svg
    :target: https://pypi.org/project/ckanext-traffic_light/
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/status/ckanext-traffic_light.svg
    :target: https://pypi.org/project/ckanext-traffic_light/
    :alt: Development Status

.. image:: https://img.shields.io/pypi/l/ckanext-traffic_light.svg
    :target: https://pypi.org/project/ckanext-traffic_light/
    :alt: License

=============
ckanext-traffic_light
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!


------------
Requirements
------------

For example, you might want to mention here which versions of CKAN this
extension works with.


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-traffic_light:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-traffic_light Python package into your virtual environment::

     pip install ckanext-traffic_light

3. Add ``traffic_light`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/ckan.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


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

The default content of the file is based on the GeoKur metadata schemas 
(https://github.com/GeoinformationSystems/ckanext-scheming, 
https://zenodo.org/record/4916698):

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


-----
Tests
-----

To run the tests, do::

    pytest --ckan-ini=test.ini

To run the tests and produce a coverage report, first make sure you have
``pytest-cov`` installed in your virtualenv (``pip install pytest-cov``) then run::

    pytest --ckan-ini=test.ini  --cov=ckanext.traffic_light


----------------------------------------
Releasing a new version of ckanext-traffic_light
----------------------------------------

ckanext-traffic_light should be available on PyPI as https://pypi.org/project/ckanext-traffic_light.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Make sure you have the latest version of necessary packages::

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version::

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI::

       twine upload dist/*

5. Commit any outstanding changes::

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags
