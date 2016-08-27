import pytest
import bz2json
from oktest import ok

url = "bugzilla.redhat.com"

@pytest.fixture
def bzclient():
    return bz2json.BzClient(url=url)

def test_import():
    ok(bz2json).is_truthy()
    ok(bz2json.BzClient).is_truthy()

def test_instantiation():
    client = bz2json.BzClient(url, None, None)
    ok(client).is_truthy()

    client = bz2json.BzClient(password=None, user=None, url=url)
    ok(client).is_truthy()

def test_query(bzclient):
    query = {
        "product": ["Fedora"],
        "component": ["python-bugzilla"],
        "status": "POST"
    }
    bugs = bzclient.query(query)
    ok(bugs).is_a(list)
    ok(len(bugs)) > 0

def test_get_comments(bzclient):
    idlist = ['1297637']
    resp = bzclient.get_comments(idlist)
    for bid in idlist:
        ok(resp).has_key(bid)
        bug = resp[bid]
        ok(bug).is_a(dict)
        ok(bug).has_key("comments")
        comments = bug['comments']
        ok(comments).is_a(list)
        ok(len(comments)) > 0
        print(bz2json.jsondump(comments, indent=4))
