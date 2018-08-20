# # Score categories
# # Change the values as you see fit
# YACHT = "yatch"
# ONES = "ones"
# TWOS = "twos"
# THREES = "threes"
# FOURS = "fours"
# FIVES = "fives"
# SIXES = "sixes"
# FULL_HOUSE = "full"
# FOUR_OF_A_KIND = "kind"
# LITTLE_STRAIGHT = "little"
# BIG_STRAIGHT = "big"
# CHOICE = "choice"
#
# def score(dice, category):
#     return globals()[category](dice)
#
#
# def yatch(dice):
#     if len(set(dice)) == 1:
#         return 50
#     return 0
#
# def ones(dice):
#     return dice.count(1)*1
#
# def twos(dice):
#     return dice.count(2)*2
#
# def threes(dice):
#     return dice.count(3)*3
#
# def fours(dice):
#     return dice.count(4)*4
#
# def fives(dice):
#     return dice.count(5)*5
#
# def sixes(dice):
#     return dice.count(6)*6
#
# def full(dice):
#     tdice = set(dice)
#     if len(tdice) == 2:
#         if dice.count(tdice.pop()) in [2,3]:
#             return sum(dice)
#
#     return 0
#
# def kind(dice):
#     tdice = set(dice)
#     if len(tdice) == 1:
#         return tdice.pop()*4
#
#     if len(tdice) == 2:
#         temp = list(tdice)
#         if dice.count(temp[0]) == 4:
#             return temp[0]*4
#         elif dice.count(temp[1]) == 4:
#             return temp[1]*4
#
#     return 0
#
# def little(dice):
#     dice = set(dice)
#     if len(dice) == 5 and 1 in dice and 6 not in dice:
#         return 30
#     return 0
#
# def big(dice):
#     dice = set(dice)
#     if len(dice) == 5 and 6 in dice and 1 not in dice:
#         return 30
#     return 0
#
# def choice(dice):
#     return sum(dice)


from collections import defaultdict


def full_house(original):
    d = defaultdict(int)
    for x in original:
        d[x] += 1
    if min(d.values()) != 2 or max(d.values()) != 3:
        return 0
    return sum(original)

def four_of_a_kind(l):
    result = [x for x in l if l.count(x) >= 4]
    if len(result) > 0:
        return result[0] * 4
    return 0


YACHT = lambda l: 50 if l.count(l[0]) == 5 else 0
ONES = lambda l: l.count(1) * 1
TWOS = lambda l: l.count(2) * 2
THREES = lambda l: l.count(3) * 3
FOURS = lambda l: l.count(4) * 4
FIVES = lambda l: l.count(5) * 5
SIXES = lambda l: l.count(6) * 6
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = lambda l: 30 if sorted(l) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda l: 30 if sorted(l) == [2, 3, 4, 5, 6] else 0
CHOICE = lambda l: sum(l)


def score(dice, category):
    return category(dice)