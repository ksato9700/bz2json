#
# Copyright 2016 Kenichi Sato
#
from __future__ import print_function
import bugzilla
import simplejson as json

class BzClient:
    def __init__(self, url):
        self.bz = bugzilla.Bugzilla(url)

    def query(self, query):
        return self.bz._query(query)["bugs"]
        

def _dump_handler(obj):
    if hasattr(obj, 'value'):
        return obj.value
    else:
        raise TypeError


def jsondump(data, indent=None):
    return json.dumps(data, indent=indent, default=_dump_handler)
