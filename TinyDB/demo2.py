class Task:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return 'This is task: {} with id: {}'.format(self.name, self.id)



from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

db = TinyDB(storage=MemoryStorage)
# TinyDB.DEFAULT_STORAGE = MemoryStorage

task = Task('task1', 101)

## Remove duplicates on multiple runs
# db.purge()
db.insert({'name': task.name, 'id': task.id})

### Insert multiple values
db.insert_multiple([
    {'name': 'T3-task', 'id': 22},
    {'name': 'T5', 'id': 37}
])

print(db.all())
## Query
query = Query()
out = db.search(query.id == 37)
print('Using search', out)
#
# ## Nested Queries

out = db.search((query.id == 37) & (query.name == 'T5'))
print('Using nested Queries', out)

#Using regex
import re
out= db.search(query.name.matches('t3.*', flags=re.IGNORECASE))
print('>>> Using regex', out)

#
#
# ## Update
db.update({'name': 'task5'}, query.name == 'T5')
print('Update of T5 to task5', db.all())
#
#
# ## Remove
db.remove(query.id == 22)
print('Removing a row based on id, 22', db.all())
#
# # Using Where clause
from tinydb import where
#
# # Existence of a field
# field_exists_flag = db.search(query.id.exists())
#

out = db.search(where('name') == 'task1')
print('>>>> Using Where syntax', out)
#
# print(len(db))
# # Get operation
# out = db.get(query.id == 37)
# print(out)
#
# # Contains operation
#
flag = db.contains(query.name == 'task5')
print('<<< Check if task5 exists', flag)
#
# #Count
count= db.count(query.name == 'task5')
print('>>>Get count of occurence of task5', count)
#
# #Tables
# db.purge_table('tasks_table')
table_task = db.table('tasks_table')
table_task.insert_multiple([
    {'name': 'Task-A', 'id': 1},
    {'name': 'Task-B', 'id': 2}
])
#
# # Upsert
table_task.upsert({'name': 'Task-A', 'id': 7}, query.name == 'Task-A')
print(len(table_task))
#
table_task.insert({'category': 'tasks', 'type': 'child'})
#
for row in table_task:
    print(row)

db.close()

#
# print('--------------------------')
# # db.purge_table('cards_table')
# table_cards = db.table('cards_table')
# table_cards.insert_multiple([
#     {'name': 'Cards-A', 'id': 1},
#     {'name': 'Cards-B', 'id': 2}
# ])
#
# for row in table_cards:
#     print(row)
# db.close()
