import bz2json
from oktest import ok

def test_import():
    ok(bz2json).is_truthy()
    ok(bz2json.BzClient).is_truthy()

def test_instance():
    url = "bugzilla.redhat.com"
    client = bz2json.BzClient(url)

    query = {
        "product": ["Fedora"],
        "component": ["python-bugzilla"],
        "status": "POST"
    }
    bugs = client.query(query)
    ok(bugs).is_a(list)
    ok(len(bugs)) > 0

    print(bz2json.jsondump(bugs, indent=4))
