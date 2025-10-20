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
    if len(scores) < 1:
        return result
    for score in scores:
        if score == scores[0]:
            print(score)
    return result 


order_discgolfers(scores)