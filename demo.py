def sonic_how_many_rings_did_you_get(input_string):
    
    counter = 0
    for c in input_string:
        if c in ['a', 'b', 'd', 'D', 'e', 'g', 'o', 'O', 'p', 'P', 'q', 'Q', 'R', '0', '6', '9']:
            counter += 1
        elif c in ['B', '8']:
            counter += 2
            
    return counter

print(sonic_how_many_rings_did_you_get("Helloo"))