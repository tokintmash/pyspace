scores = [{
    'bob': 3,
    'patric': 2,
    'squidward': 4,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 3,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 2,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 3,
}]

def order_discgolfers(scores):
    result = []
    if len(scores) < 1 or scores == None:
        return result
    
    while len(result) < len(scores[0]):
        for i in range(len(scores) -1, -1, -1):
            if len(set(scores[i].values())) == len(scores[i]):
                lowest = min(scores[i], key=scores[i].get)
                if lowest not in result:
                    result.append(lowest)
            if len(set(scores[i].values())) < len(scores[i]) and len(set(scores[i].values())) > 1:
                
            
        
    return result 


print(order_discgolfers(scores))