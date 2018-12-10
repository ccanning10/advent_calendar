import re
from collections import defaultdict
from itertools import cycle


class Marble(object):
    def __init__(self, number):
        self.number = number
        self.next = self
        self.prev = self

    def __str__(self):
        return str(self.number)

    def marble_details(self):
        return (str(self.prev), str(self), str(self.next))


class CircleBoard(object):
    def __init__(self):
        marble = Marble(0)
        self.__current_marble = marble
        self.__first_marble = marble

    def get_current_marble(self):
        return self.__current_marble

    def move_next(self):
        self.__current_marble = self.__current_marble.next

    def move_prev(self):
        self.__current_marble = self.__current_marble.prev

    def place_marble(self, number):
        # (A), B, [],  C, D
        new_marble = Marble(number)
        # A, (B), [], C, D
        self.move_next()

        # [] <- C
        self.__current_marble.next.prev = new_marble
        # [] -> C
        new_marble.next = self.__current_marble.next
        # B <- []
        new_marble.prev = self.__current_marble
        # B -> []
        self.__current_marble.next = new_marble

        # A, B, ([]), C, D
        self.move_next()

    def remove_current_marble(self):
        current_number = self.__current_marble.number
        self.__current_marble.prev.next = self.__current_marble.next
        self.__current_marble.next.prev = self.__current_marble.prev
        self.__current_marble = self.__current_marble.next
        return current_number

    def remove_marble(self, shift):
        if shift < 0:
            shift = abs(shift)
            move = self.move_prev
        else:
            move = self.move_next

        for i in range(0, shift):
            move()

        return self.remove_current_marble()

    def __repr__(self):
        start = self.__first_marble
        current = start
        nodes = []
        if current == self.__current_marble:
            nodes.append('({})'.format(str(current)))
        else:
            nodes.append('{}'.format(str(current)))

        current = current.next
        while current != start:
            if current == self.__current_marble:
                nodes.append('({})'.format(str(current)))
            else:
                nodes.append('{}'.format(str(current)))
            current = current.next
        return ', '.join(nodes) if nodes else ''


input_values = '448 players; last marble is worth 71628 points' # 394486
match = re.search('([0-9]+)(\splayers;\slast\smarble\sis\sworth\s)([0-9]+)', input_values)

num_players = int(match.group(1))
last_marble_points = int(match.group(3))

scores = defaultdict(int)
next_marble_number = 0
current_score = 0
circle = CircleBoard()
players = cycle(iter(range(1, num_players+1)))
current_player = 1
top_score = 0

print('Number of players: {}'.format(num_players))
print('Number of final marble points: {}'.format(last_marble_points))
print('Starting game...')
while (next_marble_number != last_marble_points):
    current_score = 0
    next_marble_number += 1
    current_player = next(players)
    current_marble = circle.get_current_marble()

    if next_marble_number % 23 == 0:
        current_score = next_marble_number
        removed_number = circle.remove_marble(-7)
        current_score += removed_number
    else:
        circle.place_marble(next_marble_number)

    scores[current_player] += current_score
    top_score = scores[current_player] if scores[current_player] > top_score else top_score

print('Ending game...')
print('Top Score: {}'.format(top_score))
