def sonic_how_many_rings_did_you_get(input_string):
    
    counter = 0
    
    for char in input_string:
        match char:
            case 'a':
                counter += 1
            case 'b':
                counter += 1
            case 'B':
                counter += 2
            case 'd':
                counter += 1
            case 'D':
                counter += 1
            case 'e':
                counter += 1
            case 'g':
                counter += 2
            case 'o':
                counter += 1
            case 'O':
                counter += 1
            case 'p':
                counter += 1
            case 'P':
                counter += 1
            case 'q':
                counter += 1
            case 'Q':
                counter += 1
            case 'R':
                counter += 1
            case '0':
                counter += 1
            case '6':
                counter += 1
            case '8':
                counter += 2
            case '9':
                counter += 1
 	
    return counter

print(sonic_how_many_ring1s_did_you_get("Helloo"))