import sqlite3

db = sqlite3.connect('default.dp')

query = '''
    select count(*)
    from terms
'''
for x in db.execute(query) :
    print( x )

query = '''
    select count(distinct name)
    from terms
'''
for x in db.execute(query) :
    print( x )

query = '''
    select name
    from terms
    limit 10
'''
for x in db.execute(query) :
    print( x )

query = '''
    select term, keyword, score
    from keywords
    limit 10
'''
for x in db.execute(query) :
    print( x )

query = '''
    select term, keyphrase, score
    from keyphrases
    limit 10
'''
for x in db.execute(query) :
    print( x )




with open('current.csv','w') as hand :
    print('x,y',file=hand)
    query = '''
        select term, keyword, score
        from keywords
    '''
    for x,y,z in db.execute(query) :
        print(f'{x},{y}',file=hand)