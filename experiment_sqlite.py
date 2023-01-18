DEFAULT_MAX = 5000





db = sqlite3.connect('default.dp')
db_aux = sqlite3.connect('default.dp')

#db.execute('drop table if exists terms')

#db.execute('drop table if exists keywords')

#db.execute('drop table if exists keyphrases')

db.execute('''
    create table if not exists terms(
        id integer primary key,
        name text not null,
        answer text not null default ''
    )
''')

db.execute('''
    create table if not exists keywords(
        keyword_id integer primary key,
        term_id int not null,
        keyword text not null,
        score float not null
    )
''')

db.execute('''
    create table if not exists keyphrases(
        keyphrase_id integer primary key,
        term_id int not null,
        keyphrase text not null,
        score float not null
    )
''')

db.execute('begin')
try :
    db.execute('insert into terms (name) values ("death")')
    db.execute('insert into terms (name) values ("life")')
    db.execute('insert into terms (name) values ("love")')
    db.execute('insert into terms (name) values ("science")')
    db.execute('insert into terms (name) values ("bitcoin")')
    db.execute('commit')
except sql.Error :
    db.execute('rollback')



while True :
    term = db.execute('select id, name from terms where visited = 0 limit 1')
    term = [i for i in term][0]
    term_id, term = term

    if len(term) < 1 :
        print('> Nothing more left to explore')
        break

    flag = True
    while flag :
        try :
            answer = get_gpt_answer(term)
            flag = False
        except :
            print('> Retry in 30s')
            sleep(30)

    keywords = get_keywords(answer)
    keyphrases = get_keyphrases(answer)

    answer = answer.replace('\'','')
    
    db.execute('begin')
    try :
        db.execute(f'''
            update terms
            set
                answer = '{answer}',
                visited = 1
            where id = {term_id}
        ''')

        for k in keywords :
            if not [x[0] for x in db_aux.execute(f'select count(*) from terms where name="{term}"')][0] > 0 :
                continue
            db.execute(f'''insert into terms (name) values ("{k}")''')
            db.execute(f'''insert into keywords (term_id, keyword) values ({term_id}, '{k}')''')


        for k in keyphrases :
            db.execute(f'''insert into keyphrases (term_id, keyphrase) values ({term_id}, '{k}')''')
        
        db.execute('commit')
    except :
        db.execute('rollback')
        print('> Error\n> Closing program')



    mx = [k for k in db.execute('select count(id) from terms where visited=1')][0][0]
    if mx == DEFAULT_MAX :
        print('> Default reached\n> Terminating')
        break
    print( mx, term )