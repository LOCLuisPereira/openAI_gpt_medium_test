from keybert import KeyBERT


doc = "Google is being investigated by the UK’s antitrust watchdog for its dominance in the \"ad tech stack,\" the set of services that facilitate the sale of online advertising space between advertisers and sellers. Google has strong positions at various levels of the ad tech stack and charges fees to both publishers and advertisers. A step back: UK Competition and Markets Authority has also been investigating whether Google and Meta colluded over ads, probing into the advertising agreement between the two companies, codenamed Jedi Blue."


print('>>>> keyBert #1 Keywords ')

kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc)
for k in keywords :
    print(k)

print('>>>> keyBert #2 -  Keyphrases')

keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(2,2), stop_words=None)
for k in keywords :
    print(k)



print('>>>> keyBert #3 - Diversify Results')

keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(3, 3), stop_words='english', use_maxsum=True, nr_candidates=20, top_n=5)
for k in keywords :
    print(k)




print('>>>> keyBert #4 - Diversify keyword extraction')
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc, use_mmr=True, diversity=0.7)
for k in keywords :
    print(k)



import spacy
doc = "Google is being investigated by the UK’s antitrust watchdog for its dominance in the \"ad tech stack,\" the set of services that facilitate the sale of online advertising space between advertisers and sellers. Google has strong positions at various levels of the ad tech stack and charges fees to both publishers and advertisers. A step back: UK Competition and Markets Authority has also been investigating whether Google and Meta colluded over ads, probing into the advertising agreement between the two companies, codenamed Jedi Blue."

nlp = spacy.load("en_core_web_sm")
doc = nlp(doc)
for x in doc :
    print( x.lemma_ )



