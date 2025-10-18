from collections import Counter
from collections import defaultdict

#with open('../testdata/7_testdata.dat') as f:
with open('../data/7_data.dat') as f:
    lines = [x.strip() for x in f]

plays = [] # (hand, bid)
    
for line in lines:
    hand, bid = line.split()
    plays.append((hand,int(bid)))

# Each type of play can be uniquely described by the number of unique cards
types =  defaultdict(list)
for play in plays:
#    print(play)
    cnter = Counter(play[0])
    cnt = list(cnter.values())
    cnt.sort(reverse = True)
    type = tuple(cnt)
    types[type].append(play)
# types are new a dict with type of play as key

# keys in order from lowest to highest range
keys = [(1, 1, 1, 1, 1), (2, 1, 1, 1),  (2, 2, 1), (3, 1, 1), (3, 2), (4, 1), (5,)]

# custom sort (nice to know)

# Define custom card strength
card_order = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, 
              '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, 
              '4': 4, '3': 3, '2': 2}

def hand_strength(hand_str):
    """Convert hand string to tuple of card values for comparison"""
    return tuple(card_order[card] for card in hand_str)

def prob1():
    #Loop from loest to highest, does not need to be optimized.
    rang = 1
    res = 0
    for key in keys:
        plays = types[key]
        sorted_plays = sorted(plays, key=lambda x: hand_strength(x[0]))
        # after this we now should have each type sorted from low to high, and the type from low to high
        for play in sorted_plays:
            res += play[1]*rang
            rang += 1
    print(res)
prob1()
