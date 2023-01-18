import sqlite3

db = sqlite3.connect('default.dp')

for item in db.execute('select * from terms limit 10') :
    print(item)

for item in db.execute('select * from keywords limit 10') :
    print(item)

for item in db.execute('select * from keyphrases limit 10') :
    print(item)

for x in db.execute('select count(distinct(name)) from terms') :
    print(x)


query = '''
select t.name, k.keyword
from keywords as k
left join terms as t
on k.term_id=t.id
'''
cursor = db.execute(query)

with open('current.csv', 'w') as hand :
    print("x,y", file=hand)
    for c in cursor :
        print(f'{c[0]}, {c[1]}', file=hand)

query = '''
select name, count(*) as cnt
from terms
group by name
order by cnt asc
'''
cursor = db.execute(query)
for c in cursor :
    print(c)