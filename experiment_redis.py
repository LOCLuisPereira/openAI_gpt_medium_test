from redis import Redis

CLEAN = True
START = [
    'death',
    'science',
    'joy',
    'world',
    'future'
]

mem = Redis(db=4, decode_responses=True)

if CLEAN :
    for k in mem.keys() :
        mem.delete( k )

for k in START :
    mem.lpush( 'mine', k )

for k in START :
    mem.set(k, 1)

print(mem.get('hello'))