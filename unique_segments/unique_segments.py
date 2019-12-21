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
def find_repeating_segments(list_of_dicts):
    repeats = {}
    unique_cache = []

    for index, obj in enumerate(list_of_dicts):
        unique_cache.append(''.join(obj.values())) # send all values to a preliminary cache
        repeats[''.join(obj.values())] = [] #give each key a value of an empty list

    unique = list(set(unique_cache)) # make cache unique values

    for i in range(len(list_of_dicts)): # loop through list_of_dicts
        for u in range(len(unique)): # loop through unique list
            if ''.join(list_of_dicts[i].values()) == unique[u]: #if list_of_dicts value is in unique
                    repeats[''.join(list_of_dicts[i].values())].append(''.join(list_of_dicts[i].keys())) # append to repeats

    # write results to file
    with open('data12_17ca.txt', 'w') as outfile:
        for i in repeats:
            if len(repeats[i]) > 1:
                json.dump( 'repeats: '+ ', '.join(repeats[i]), outfile)
            outfile.write('\n')

# find_repeating_segments(ca_12_17_2019)

# how man unique messages are there?
def unique_messages(list_of_dicts):
    all_messages = list()

    for i in range(len(list_of_dicts)):
        foo = list(list_of_dicts[i].values())

        animals_per_seg = ''.join(foo)
        cleaned_animals_per_segment = animals_per_seg.replace('-|-|-|-|-|', '').replace('|-|-', '')
        cleaned_animals_list = cleaned_animals_per_segment.split(";")

        for i in cleaned_animals_list:
            all_messages.append(i)
        
    return list(set(all_messages))

# print(unique_messages(ca_12_17_2019 ))
# print(len(unique_messages(ca_12_17_2019)))

# print(len(ca_12_17_2019))

# what segments changed month over month?
def changed_segments(prevSeg, currentSeg):
    for index, obj in enumerate(currentSeg):
        if(currentSeg[index][''.join(obj.keys())] is ''.join(prevSeg[index].values())):
           pass
        else:
            print(''.join(obj.keys()) + ' has changed in december')

#changed_segments(ca_11_01_2019, ca_12_17_2019)

#  given a list of dicts, tell me what segments each individual message is in
def get_segments(list_of_dicts):
    list_of_strings = list()
    segments_by_message = {}

    # populates the list_of_strings with banner message strings
    for i in list_of_dicts:
       banner_list = ''.join(i.values()).replace('-|-|-|-|-|', '').replace('|-|-', '').split(';')
       for i in banner_list:
           list_of_strings.append(i)
    
    # unique banners
    list_of_unique_strings = list(set(list_of_strings))
    
    # pushes segments to segments_by_message
    for i in list_of_unique_strings:
        segments_by_message[i] = []
        for j in list_of_dicts:
            if i in ''.join(j.values()):
                segments_by_message[i].append(''.join(j.keys()))
    
    return segments_by_message
            

# prints to file
data = get_segments(mx_11_19_2019)
with open('name_of_file.txt', 'w') as fout:
    json.dump(data, fout, indent=4)