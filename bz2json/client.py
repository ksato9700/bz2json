#
# Copyright 2016 Kenichi Sato
#
from __future__ import print_function
import bugzilla
import simplejson as json

class BzClient:
    def __init__(self, *args, **kwargs):
        self.bz = bugzilla.Bugzilla(*args, **kwargs)

    def query(self, query):
        return self.bz._query(query)["bugs"]
        

    def get_comments(self, idlist):
        return self.bz.get_comments(idlist)["bugs"]


def _dump_handler(obj):
    if hasattr(obj, 'value'):
        return obj.value
    else:
        raise TypeError


def jsondump(data, indent=None):
    return json.dumps(data, indent=indent, default=_dump_handler)
