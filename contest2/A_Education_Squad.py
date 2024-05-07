row0 = input()
row1 = input()
row2 = input()

individual = 0
if row0[0] == row1[0] == row2[0]: individual += 1
if row0[1] == row1[1] == row2[1]: individual += 1
if row0[2] == row1[2] == row2[2]: individual += 1
if row0[0] == row0[1] == row0[2]: individual += 1
if row1[0] == row1[1] == row1[2]: individual += 1
if row2[0] == row2[1] == row2[2]: individual += 1
if row0[0] == row1[1] == row2[2]: individual += 1
if row0[2] == row1[1] == row2[0]: individual += 1

print(individual)

team = 0
teams = []
if row0[0] == row0[1]:
    current_team = sorted([row0[0], row0[2]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row0[0] == row0[2]:
    current_team = sorted([row0[0], row0[1]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row0[1] == row0[2]:
    current_team = sorted([row0[1], row0[2]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1

if row1[0] == row1[1]:
    current_team = sorted([row1[0], row1[2]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row1[0] == row1[2]:
    current_team = sorted([row1[0], row1[1]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row1[1] == row1[2]:
    current_team = sorted([row1[0], row1[1]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1


if row2[0] == row2[1]:
    current_team = sorted([row2[0], row2[2]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row2[0] == row2[2]:
    current_team = sorted([row2[0], row2[1]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row2[1] == row2[2]:
    current_team = sorted([row2[0], row2[1]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1

if row0[0] == row1[0]:
    current_team = sorted([row0[0], row2[0]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row0[0] == row2[0]:
    current_team = sorted([row0[0], row1[0]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row1[0] == row2[0]:
    current_team = sorted([row0[0], row1[0]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1

if row0[1] == row1[1]:
    current_team = sorted([row0[1], row2[1]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row0[1] == row2[1]:
    current_team = sorted([row0[1], row1[1]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row1[1] == row2[1]:
    current_team = sorted([row0[1], row1[1]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1

if row0[2] == row1[2]:
    current_team = sorted([row0[2], row2[2]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row0[2] == row2[2]:
    current_team = sorted([row0[2], row1[2]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row1[2] == row2[2]:
    current_team = sorted([row0[2], row1[2]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1

if row0[0] == row1[1]:
    current_team = sorted([row0[0], row2[2]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row0[0] == row2[2]:
    current_team = sorted([row0[0], row1[1]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row1[1] == row2[2]:
    current_team = sorted([row0[0], row1[1]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1

if row0[2] == row1[1]:
    current_team = sorted([row0[2], row2[0]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row0[2] == row2[0]:
    current_team = sorted([row0[2], row1[1]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1
if row1[1] == row2[0]:
    current_team = sorted([row0[2], row1[1]])
    if current_team not in teams:
        teams.append(current_team)
        team += 1

print(team)

