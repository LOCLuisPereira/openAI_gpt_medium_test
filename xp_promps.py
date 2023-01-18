import openai

openai.api_key = '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'

prompt = 'What is death'
prompt = 'Long explanation. What is death'
prompt = 'how would a child explain what is death'
prompt = 'how would a teen explain what is death'
prompt = 'how would an elder explain what is death'

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=256
)

gpt_reponse = response['choices'][0]['text'].strip()

print(gpt_reponse)