from itertools import cycle
from collections import defaultdict

# 416 players; last marble is worth 71975 points


def calculate_score(players, marbles):
    circle = []
    scores = defaultdict(int)
    pos = 0

    next_player = cycle(range(players)).__next__

    for marble in range(marbles):
        player = next_player()

        if marble % 23 == 0 and marble != 0:
            scores[player] += marble
            next_pos = (pos - 7) % len(circle)
            scores[player] += circle[next_pos]
            del circle[next_pos]
            pos = next_pos
        else:
            next_pos = 0
            if len(circle) == 0:
                next_pos = 1
            else:
                next_pos = ((pos+1) % len(circle)) + 1
            circle.insert(next_pos, marble)
            pos = next_pos

    return max(scores.values())


print(calculate_score(416, 71975))


# part2
class Node:
    def __init__(self, value, previous_node=None, next_node=None):
        self.value = value
        self.previous = previous_node
        self.next = next_node

number_of_players = 416
number_of_marbles = 71975 * 100

n0 = Node(0)
n0.previous = n0
n0.next = n0

current_node = n0
scores = dict()

for turn in range(1, number_of_marbles+1):

    if turn % 23 == 0:
        player = (turn % number_of_players) + 1
        current_node = current_node.previous.previous.previous.previous.previous.previous.previous
        scores[player] = scores.get(player, 0) + turn + current_node.value
        current_node.previous.next = current_node.next
        current_node = current_node.next
    else:
        new = Node(turn, current_node.next, current_node.next.next)
        current_node.next.next.previous = new
        current_node.next.next = new
        current_node = new

print(max(scores.values()))
