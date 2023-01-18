import os
import openai
from time import sleep

# Load your API key from an environment variable or secret management service
openai.api_key = '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'

import spacy
nlp = spacy.load("en_core_web_sm")

from keybert import KeyBERT
kw_model = KeyBERT()

'''
import spacy
nlp = spacy.load("en_core_web_sm")
for k in keyphrases :
    if float(k[1]) > 0 :
        final = nlp( k[0] )
        for f in final :
            print(f.lemma_)
'''

i = 0

data = []
xs = ['joy']
xs_visited = []

for _ in range(2000) :
    i += 1
    x = xs.pop()
    print(f'>>>> {i} {x}')
    prompt = f'What is {x}?'
    obj = {'name' : x}
    xs_visited.append(x)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=256
    )

    gpt_reponse = response['choices'][0]['text'].strip()


    keywords = kw_model.extract_keywords(gpt_reponse, use_mmr=True, diversity=0.7)


    obj['keywords'] = []
    for key, value in keywords :
        if float(value) < 0 : continue
        spacy_doc = nlp( key )
        for spacy_word in spacy_doc :
            spacy_word = spacy_word.lemma_
            if spacy_word not in xs_visited :
                xs.append( spacy_word )
            obj['keywords'].append( spacy_word )


    keyphrases = kw_model.extract_keywords(gpt_reponse, keyphrase_ngram_range=(2, 3), stop_words='english', use_maxsum=True, nr_candidates=20, top_n=5)
    obj['keyphrases'] = [ k for k,v in keyphrases if float(v) > 0 ]

    data.append(obj)
    sleep(2)

import json
print(
    json.dumps(data, indent=4),
    file=open('out_1.json','w')
)