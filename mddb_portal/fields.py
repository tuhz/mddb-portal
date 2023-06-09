import os
from urllib.parse import urlsplit, urlunsplit, urlencode


def title(result):
    """The title for this Globus Search subject"""
    # return result[0]["dc"]["titles"][0]["title"]
    return result[0]['material']

'''
def globus_app_link(result):
    """A Globus Webapp link for the transfer/sync button on the detail page"""
    url = get_file(result).get("url")
    if not url:
        return
    parsed = urlsplit(url)
    query_params = {
        "origin_id": parsed.netloc,
        "origin_path": os.path.dirname(parsed.path),
    }
    return urlunsplit(
        ("https", "app.globus.org", "file-manager", urlencode(query_params), "")
    )


def https_url(result):
    """Add a direct download link to files over HTTPS"""
    url = get_file(result).get("url")
    if not url:
        return
    path = urlsplit(url).path
    return urlunsplit(("https", "g-71c9e9.10bac.8443.data.globus.org", path, "", ""))


def get_file(result):
    """To start, 'test' files are just a single file in a directory, so we'll always just look
    for the first file in the list."""
    return result[0]["files"][0]
'''

def combine_ref_details(metadata):
    doi_lst = metadata.get('reference')
    title_lst = metadata.get('reference_title')
    author_lst = metadata.get('reference_author')
    journal_lst = metadata.get('reference_journal')
    date_lst = metadata.get('reference_date')
    ref_details_lst = list()
    for doi, title, author, journal, date in zip(doi_lst, title_lst, author_lst, journal_lst, date_lst):
        ref_details = {
            "title": title,
            "author": author,
            "journal": journal,
            "DOI": doi,
            "date": date[:7] if date != '1901-01-01' else '',
        }
        ref_details_lst.append(ref_details)
    return ref_details_lst


def search_results(result):
    metadata = result[0]
    return [
        {
            "field": "material",
            "title": "Material",
            "value": metadata.get('material')
        },
        {
            "field": "descriptor",
            "title": "Descriptor",
            # "type": "int",
            "value": metadata.get('descriptor')
        },
        {
            "field": "value",
            "title": "Value",
            "value": metadata.get('value')
        },
        {
            "field": "reference",
            "title": "Reference",
            "value": combine_ref_details(metadata)
        }
    ]
