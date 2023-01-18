''' PARAMENTERS '''
DEFAULT_MAX = 5000
CLEAN = False
START = [
    'death',
    'science',
    'joy',
    'world',
    'future'
]


''' IMPORTS '''
from keybert import KeyBERT
from redis import Redis
from time import sleep
import sqlite3
import openai
import spacy
import os


''' KEYS AND MODELS '''
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


def wrapper_get_gpt_answer( term, agent=0 ) :
    while True :
        try :
            answer = get_gpt_answer(term, agent)
            return answer
        except KeyboardInterrupt :
            raise Exception('Leaving')
        except : pass
    return None


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
            xs.append( (spacy_word.lemma_, value) )
    
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
    return [ (k,v) for k,v in keyphrases if float(v) > 0 ]


''' DATABASES '''
mem = Redis(db=4, decode_responses=True)
db = sqlite3.connect('default.dp')


''' FIRST TIME CLEANING '''
if CLEAN :
    db.execute('drop table if exists terms')
    db.execute('drop table if exists keywords')
    db.execute('drop table if exists keyphrases')

    for k in mem.keys() :
        mem.delete( k )

    for k in START :
        mem.lpush('__mem__', k)

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
            term text not null,
            keyword text not null,
            score float not null
        )
    ''')

    db.execute('''
        create table if not exists keyphrases(
            keyphrase_id integer primary key,
            term text not null,
            keyphrase text not null,
            score float not null
        )
    ''')

STAT = sum([1 for _ in mem.keys()]) - 1

while True :

    if STAT > DEFAULT_MAX : break

    xterm = mem.rpop('__mem__')
    
    if not xterm :
        print('> Ending')
        break
    
    if mem.get(xterm) :
        print(f'> Already done: {xterm}')
        continue


    STAT += 1
    print(f'> {STAT}: {xterm}')

    ''' Try to mine. If something happens, restart the process'''
    try :
        answer = wrapper_get_gpt_answer( xterm, 0 )
        keywords = get_keywords(answer)
        keyphrases = get_keyphrases(answer)

        answer = answer.replace('\'','').replace('\"','')

        mem.set(xterm, 1)

        query = f'''insert into terms (name,answer) values ("{xterm}","{answer}");\n'''
        query = query + f'''insert into keywords (term, keyword, score) values '''

        xs = []
        for k,v in keywords :
            mem.lpush('__mem__', k)
            xs.append(f'''('{xterm}', '{k}', {v})''')
        query = query + ','.join(xs)

        query = query + f''';\ninsert into keyphrases (term, keyphrase, score) values '''

        xs = []
        for k,v in keyphrases :
            xs.append(f'''('{xterm}', '{k}', {v})''')
        query = query + ','.join(xs)

        # print(query)
        db.executescript(query)

    except Exception as e:
        print(e)
        mem.rpush('__mem__', xterm)
        break