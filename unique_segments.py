import pprint
import json

segments = [
    {"segment list 1": "-|-|-|-|-|dog;cat;rabbit|-|-"},
    {"segment list 2": "-|-|-|-|-|dog;cat;pig|-|-"},
    {"segment list 3": "-|-|-|-|-|dog;cat;rabbit|-|-"},
    {"segment list 4": "-|-|-|-|-|cat;bird;rabbit|-|-"},
    {"segment list 5": "-|-|-|-|-|dog;bird;pig|-|-"},
    {"segment list 6": "-|-|-|-|-|cat;bird;rabbit|-|-"},
    {"segment list 7": "-|-|-|-|-|cat;rabbit;dog|-|-"},
    {"segment list 8": "-|-|-|-|-|dog;cat;rabbit|-|-"}
]

# what segments have the same values?
def find_repeating_segments(segments):
    repeats = {}
    unique_cache = []

    for index, obj in enumerate(segments):
        unique_cache.append(''.join(obj.values())) # send all values to a preliminary cache
        repeats[''.join(obj.values())] = [] #give each key a value of an empty list

    unique = list(set(unique_cache)) # make cache unique values

    for i in range(len(segments)): # loop through segments
        for u in range(len(unique)): # loop through unique list
            if ''.join(segments[i].values()) == unique[u]: #if segments value is in unique
                    repeats[''.join(segments[i].values())].append(''.join(segments[i].keys())) # append to repeats


    pprint.pprint(repeats)

    # write results to file
    with open('data.txt', 'w') as outfile:
        for i in repeats:
            if len(repeats[i]) > 1:
                json.dump( 'repeats: '+ ', '.join(repeats[i]), outfile)
            outfile.write('\n')

# find_repeating_segments(segments)


# how man unique animals are there?
def unique_animals(segments):
    all_animals = list()

    for i in range(len(segments)):
        foo = list(segments[i].values())

        animals_per_seg = ''.join(foo)
        cleaned_animals_per_segment = animals_per_seg.replace('-|-|-|-|-|', '').replace('|-|-', '')
        cleaned_animals_list = cleaned_animals_per_segment.split(";")

        for i in cleaned_animals_list:
            all_animals.append(i)
        
    return list(set(all_animals))


print(unique_animals(segments))
print(len(unique_animals(segments)))