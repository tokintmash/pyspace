def identify_ninja(ninja_name, all_villagers):
    result = []
    # flag = False
    for i in range(len(all_villagers)):
    # for villager in all_villagers:
        if sorted(ninja_name) == sorted(all_villagers[i]):
            result.append(all_villagers[i])
    # if len(result) == 0:
    #     return TypeError
    return result

# print(identify_ninja('obb', ['bob', 'richard']))
# print(identify_ninja('toidz', ['bob', 'richard']))