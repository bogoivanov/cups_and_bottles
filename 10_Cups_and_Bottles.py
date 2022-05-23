from collections import deque

end_bottles = False
cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted_water = 0

while cups and bottles:
    bottle = bottles.pop()
    cup = cups.popleft() - bottle
    if cup > 0:
        cups.appendleft(cup)
    else:
        wasted_water += abs(cup)

if bottles:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")
else:
    print(f"Cups: {' '.join([str(x) for x in cups])}")

print(f"Wasted litters of water: {wasted_water}")

# from collections import deque
#
# end_bottles = False
# cups_capacity_liters = deque([int(x) for x in input().split()])
# bottles_capacity_liters = deque([int(x) for x in input().split()])
# wasted_litters_of_water = 0
#
# while cups_capacity_liters:
#     if bottles_capacity_liters:
#         current_bottle = bottles_capacity_liters.pop()
#         if cups_capacity_liters[0] - current_bottle <= 0:
#             current_cup = cups_capacity_liters.popleft()
#             wasted_litters_of_water += abs(current_cup - current_bottle)
#         else:
#             cups_capacity_liters[0] -= current_bottle
#             continue
#     else:
#         end_bottles = True
#         break
#
# if end_bottles:
#     print(f"Cups: {' '.join([str(x) for x in cups_capacity_liters])}")
# else:
#     print(f"Bottles: {' '.join([str(x) for x in bottles_capacity_liters])}")
# print(f"Wasted litters of water: {wasted_litters_of_water}")