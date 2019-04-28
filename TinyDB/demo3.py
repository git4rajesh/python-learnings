from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

db = TinyDB('test.json', sort_keys=True, indent=4, separators=(',', ': '))
db.purge()
db.insert({'b': 1})
db.insert({'c': 3})
db.insert({'a': 1})

