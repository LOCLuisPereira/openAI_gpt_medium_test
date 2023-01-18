'''
from revChatGPT.ChatGPT import Chatbot

chatbot = Chatbot({
    "session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..pgGVYLGpxTrDgxZz.8SlrWhCcyPdlC9eveH_qU5vCa5_3dd6x4GRznBRbuk7gUQVY7rRokWKHdWHb38myRbXVhbf3q4xFnjPvUXo9GJMjU24WhXM7-TEFRy8bX3KTPAZb8sU_BYYaJLgJL6ThCsY8ktrhCjfcKPy9REA0dvxjV1cnE0vgGCgl4QeCuZNF18LkV35hYxKBn8Hd0W1cCVSXg83rhtk5ufqgfg9n7fywAkM4JLOXrq3sbrpQaC_R6qHNEHrU9_0m4YQF07u8vd6vgNEpCt5zK0fHwe-0OnASuPETxbw2zN3g_hrlLAc0xpkSQl-5dw78o-zbUqqdQI3OxvwsxkzD_jP32kHIoIBnPXC_jD6LW_xL_Efm14g1mwfqg1osJq-_MfuIWkcwmAeMi2r4Uu4HX8tsVwEkm12Qyk0mzcUbHTBB2OyZgdu8KHMwDgT3LoR5oQkv5AZmWabVTWnZWlJrzpItJv2Qjpxqg7JRD-an204F7hShesXTEhdJuYWIrcQmj4xk74gTeubxSLIEX77jT7vWGwAZbB-QHrQe9GFO5BBZRmxNOwItXjU61yrEQZXqb9SuuVXmpXOM8trFBMIrDA-CY5YazcxLO7b-b1aksFnvfSiuQUHfOH7YU7PLsxdHdflQhwE97GXfIv89mLuRzx_QKbyDUWu3oCugo6HPdSRkm9Vmb7ovG_8_FU18HowlrBLCJO3oUE4h9iNISyWBEsCmFt-UBG3Xz7Bim0yzJh-CFE583KsoTPCeqt5r6IcsAEA_n4UNdY-fDToKjPqXBqDYwB2mwBYA_IfZhrn_R9cxZTkyf7CgBxaxU2JEO3JqYZQI2-L6M9ZJVGf8iD_051zD-FtEoMG5VJEqSnn_DJY7pEFcYTG6xjrhpn3OSDYqNQ6nB_o--LUrMzAcQSHYzu96blZYqZJ7uf2_JXpNBBDgzqWSJYELjaVsjygdWbyvjiIyIMWyDQj8Qv5I9HGXvAxItDBS1Bii2eaBT10Pyd2ki9n5l73b4wUqyR7JeBSl58n7UIPjGvOydmD-cLPhAsKRZk9F0c1n1wEuhMeaF2fCepO-YXRrZNt-BA_mLqJngwlwnKxuJLbrqGzgmwyTGgyRDGtZHVT71Z11aToUDKkPr2VDZxbfXPHk_fHLsV0PbwxZeksjiX3eecH9yawn6Fwsau4K6uUM5c8oC6rn9V6JdNrv1z7y4TeP4fObIB5NYWOxXhANonFf6ObA0-AaTGAaqcialogxmcmvj4S1a6QjEgwxYE7DVd9rV6v8WCe6ts_WK242O7I3ufFN2qnEQYXlRnR69rF3hfZOe-QZFQLPl94zxU3w8DsRUYOxyd8KD5cXelhHRW1LsK8P0wCvUNm4FmTItp39n6l_6mu1Et2J7YhurP4DBeZ_pF5XJstC62KNRDyeX4EG8omg0g5q9U8ByK8Pisu-TGuPPBt_yh1bx7CU_jBJlvImRf69ex3ulv1pNGO753C9dlaWRG1TJ-cH_vgVotrWOQEbXxPgbVi4ncWlzQO7l9xPgDKny21_aPFXOpOC5aQfkt2jJyXAG_XvKbDT0kNEXa_mvwpdtORDpjzEVTWhzIwzK7Qym7Bfms8F72H4I9eBWU8b5LecaI58rIkTgf-8l3ECMFa-MNqv80cBpnkYrIxlxzn9-C-7XRh1mx-dZ9hCpW-LFDiPNBj86G-xjYwPIENi0ouowcS9eNfRxvvV80LwZz1l9R62xHS-UZ5o3vVYKj0P1bN2G_RpukHfdg7ZwemLG5VJOfxMVAlOCqyDPKLQ1eHoAUB1Wuaak1dEL1au-vJ19_Zxv0jS_OJMYSrf0moDE_xIiQy_xPaTJy-nSfcirCsyyl1C_zQOWhqN8dXdIH_Y5jq9eMXzBiy0HmrZu1BKkkBLp8POpIRd_iFgtFmGJuShpD_8rEAG7fW4N2kZUP9uxB4f7q752PCz-9YLL19jhOAsdHe7cu_9yWKtOwC0TX5ogN_kzAcPcuPs6BBiWKGLI2ec5Wyadl9Zo0BP0a13D_7L_HBXg768vp5CmNlZlc1FzpUgMEySi4UX3WO84WTrtYz0kO3YBkaTuC3BjA9qV-OBs24O2XAKnMXQl-AzWAT6D3n2VsqGcLyKEW94UQ7Lt1DHfalZluKINyKpiJGZs8Xih-5zhrYfqpPtcJEbvgYY8dbMLS_MDYJPVJC1XmSO3mAYHXvTxK041y7kC_yqXleDU-CpG56_euh9eLqrxas63YwMWkOWX5CYLgkT5XYqhU23xz_TxtwOFW4rhM2JT1T5th6yTiNRssw.caeBMewQmUlL_y5KF5YApw"
}, conversation_id=None, parent_id=None) # You can start a custom conversation

response = chatbot.ask("Prompt", conversation_id=None, parent_id=None) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)

print(response)
'''


from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("yanekyuk/bert-keyword-extractor")
tokenizer = AutoTokenizer.from_pretrained("yanekyuk/bert-uncased-keyword-extractor")

model = AutoModelForTokenClassification.from_pretrained("yanekyuk/bert-keyword-extractor")
model = AutoModelForTokenClassification.from_pretrained("yanekyuk/bert-uncased-keyword-extractor")


doc = "Google is being investigated by the UK’s antitrust watchdog for its dominance in the \"ad tech stack,\" the set of services that facilitate the sale of online advertising space between advertisers and sellers. Google has strong positions at various levels of the ad tech stack and charges fees to both publishers and advertisers. A step back: UK Competition and Markets Authority has also been investigating whether Google and Meta colluded over ads, probing into the advertising agreement between the two companies, codenamed Jedi Blue."

from transformers import pipeline
pipe = pipeline('ner', model=model, tokenizer=tokenizer)

import json
xs = pipe(doc)

for x in xs :
    print( x['word'] )







print('>>>> keyBert #1 Keywords ')

from keybert import KeyBERT
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