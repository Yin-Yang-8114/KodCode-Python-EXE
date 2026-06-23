# part 1 section 1
agent = {'name': 'Alpha', 'level': 3, 'active': True}
print(agent)
# part 1 section 2
print(agent['name'])
# part 1 section 3
print(agent.get('level'))
print(agent.get(0))
# part 1 section 4
agent['score'] = 95
print(agent)
# part 1 section 5
agent['level'] = 5
print(agent)
# part 1 section 6
del agent['active']
print(agent)
# part 1 section 7
print(agent.keys())
print(agent.values())
print(agent.items())
# part 1 section 8
print("score" in agent)
# part 1 section 9
scores = {'Alpha': 80, 'Bravo': 95, 'Charlie': 70}
# high_score = max(scores.values())
# print(scores.keys(high_score))
print(max(scores.values()),max(scores, key=scores.get))
# part 1 section 10
agents_copy = agent.copy()
agents_copy["name"] = "Bravo"
print(agent)
print(agents_copy)
# part 2 section 1
config = {}
config.setdefault("timeout",30)
print(config)
config.setdefault("timeout",31)
print(config)
# part 2 section 2
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d3 = d1 | d2
print(d3)
# part 2 section 3
print(d3.pop('c'))
print(d3)
# print(d3.pop('e'))
# part 2 section 4
nested = {'server': {'host': 'localhost', 'port': 8080}}
print(nested['server']['port'])
# part 2 section 5
items = ['a', 'b', 'a', 'c', 'b', 'a']
items_frequency ={}
for item in items:
    if item in items_frequency:
        items_frequency[item]  += 1
    else:
        items_frequency[item] = 1
print(items_frequency)
# part 3 section 1

