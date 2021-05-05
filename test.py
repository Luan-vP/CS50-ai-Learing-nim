from nim import *

test_player = NimAI()

# Test get_q_value()

# Test unassigned pair

print(test_player.get_q_value((1,1,1,1), (0,1)) == 0)

# Test assigned pair
test_player.q[(2,2,2,2),(1,1)] = 5
print(test_player.get_q_value((2,2,2,2),(1,1)) == 5)

# Test update_q

test_player.update_q_value([2,2,2,2], (1,1), 5, 1, 3)
print(test_player.q[(2,2,2,2),(1,1)] == 4.5) 