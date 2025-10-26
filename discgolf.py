scores = [{
    'bob': 3,
    'patric': 3,
    'squidward': 2,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 3,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 3,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 3,
}]

def all_ties(scores):
    counter = 0
    for score in scores:
        if len(set(score.values())) > 1:
            counter += 1
    if len(counter) == len(scores):
        return True
    else:
        return False

def order_discgolfers(scores):
    result = []
    players = sorted(scores[0].keys())
    if len(scores) < 1 or scores == None:
        return result
    if all_ties:
        return players
    
    # while len(result) <= len(players):
    while len(result) <= 2:
        for i in range(len(scores) -1, -1, -1):
            print("i is:", i)
            if len(set(scores[i].values())) > 1:
                
                lowest = min(scores[i], key=scores[i].get)
                if lowest not in result:
                    print("lowest:", lowest)
                    result.append(lowest)
                    scores[i].pop(lowest)

            if len(set(scores[i].values())) == 1 and len(scores[i]) > 1:
                print("tied score:", scores[i])
                sorted_score = sorted(scores[i].keys())
                print("sorted score:", sorted_score)
                if sorted_score[0] not in result:
                    result.append(sorted_score[0])
            #         # print(result)
                    scores[i].pop(sorted_score[0])
            print("result:", result)
                    
        # for player in players:
        #     if player not in result:
        #         result.append(player)
        #         break
        
    print("scores:", scores)
    return result 

print(order_discgolfers(scores))