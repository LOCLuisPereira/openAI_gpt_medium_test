DEFAULT_MAX = 5000




from keybert import KeyBERT
from time import sleep
import sqlite3
import openai
import spacy
import os




openai.api_key = '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'

nlp = spacy.load("en_core_web_sm")

kw_model = KeyBERT()




def get_gpt_answer( term, agent=0 ) :
    if agent == 1 :
        prompt = f'how would a child explain what is {term}?'
    elif agent == 2 :
        prompt = f'how would a teen explain what is {term}?'
    elif agent == 3 :
        prompt = f'how would an elder explain what is {term}?'
    else :
        prompt = f'Long explanation. What is {term}?'

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=256
    )

    return response['choices'][0]['text'].strip()




def get_keywords( phrase ) :
    keywords = kw_model.extract_keywords(
        phrase,
        stop_words='english',
        use_mmr=True,
        diversity=0.7,
        nr_candidates=20,
        top_n=10
    )
    xs = []

    for key, value in keywords :
        if float(value) < 0 : continue
        spacy_doc = nlp( key )
        for spacy_word in spacy_doc :
            xs.append( spacy_word.lemma_ )
    
    return xs




def get_keyphrases( phrase ) :
    keyphrases = kw_model.extract_keywords(
        phrase,
        keyphrase_ngram_range=(2, 3),
        stop_words='english',
        use_maxsum=True,
        nr_candidates=20,
        top_n=5
    )
    return [ k for k,v in keyphrases if float(v) > 0 ]




db = sqlite3.connect('default.dp')
db_aux = sqlite3.connect('default.dp')

#db.execute('drop table if exists terms')

#db.execute('drop table if exists keywords')

#db.execute('drop table if exists keyphrases')

db.execute('''
    create table if not exists terms(
        id integer primary key,
        name text not null,
        answer text not null default '',
        visited int default 0
    )
''')

db.execute('''
    create table if not exists keywords(
        keyword_id integer primary key,
        term_id int not null,
        keyword text not null
    )
''')

db.execute('''
    create table if not exists keyphrases(
        keyphrase_id integer primary key,
        term_id int not null,
        keyphrase text not null
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