list_status = []
list_operations = ['create', 'set_wrk_status', 'set_attributes']



def map_method(operation):
    print(operation)
    status = True if get_status(operation) == True else False
    return status

def get_status(operation):
    return False


my_l = map(map_method, list_operations)
print(list(my_l))


#
# def out(val):
#     return val
# output = map(out, [1,2,3])
# print(list(output))

import re
import requests


def verify_pve(self, key):
    status = True
    xid = self.helper.get_xid(key)
    rally_url, rally_id = self.helper.get_url_id(key)

    match_obj = re.match('\d+', xid)
    if match_obj is None:
        status = False

    resp = requests.get(rally_url)
    if resp.status_code != 200:
        status = False

    match_obj = re.match('[IF]\d+', rally_id)
    if match_obj is None:
        status = False

    result = 1 if status else 0

    logger.logs('XID: %s \nRally_URL: %s \nRally_ID: %s  \nResult: %s' % (xid, rally_url, rally_id, result), 'info')
    logger.logs('PVE verification successful', 'info')
    return xid, rally_url, rally_id, result


def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o : (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return added, removed, modified, same

x = dict(a=1, b=2)
y = dict(a=2, b=2)
added, removed, modified, same = dict_compare(x, y)