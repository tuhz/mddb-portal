# MDDB-portal
An ACDC portal for the Materials Descriptor Database (MDDB) project

This is a basic starter portal for visualizing datasets published into the GMCA search index.

### Development

Create your environment and install packages:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

And run the portal with:

```
python manage.py runserver
```

ACDC branding is handled by the ACDC project here:

https://github.com/globusonline/django-alcf-data-portal


### Portal modifications

In general, any custom views under `urls.py` are fine. All URLs are mounted under
the index name, and will appear under ``https://acdc.alcf.anl.gov/myindex/``.

### Publishing content

TBD
