# part 1 section 1
agents = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']
print(agents)
# part 1 section 2
print(agents[0],agents[-1])
# part 1 section 3
print(agents[2])
# part 1 section 4
print(agents[1:4])
# part 1 section 5
agents.append('Foxtrot')
print(agents)
# part 1 section 6
agents.insert(2,'Zulu')
print(agents)
# part 1 section 7
agents.remove('Bravo')
print(agents)
# part 1 section 8
print(len(agents))
# part 1 section 9
scores = [42, 17, 95, 8, 61]
print(max(scores))
print(min(scores))
# part 1 section 10
agents2 = agents.copy()
agents2[0]="ZuZU"
print(f'agents : {agents}\nagents 2 : {agents2}')
