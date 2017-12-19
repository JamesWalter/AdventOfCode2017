""" Advent of Code 2017 Day 16 Permutation Promenade """
# You come upon a very unusual sight; a group of programs here appear to be 
# dancing.
# 
# There are sixteen programs in total, named a through p. They start by 
# standing in a line: a stands in position 0, b stands in position 1, and so 
# on until p, which stands in position 15.
# 
# The programs' dance consists of a sequence of dance moves:
# 
# Spin, written sX, makes X programs move from the end to the front, but 
# maintain their order otherwise. (For example, s3 on abcde produces cdeab).
# Exchange, written xA/B, makes the programs at positions A and B swap 
# places.
# Partner, written pA/B, makes the programs named A and B swap places.
# For example, with only five programs standing in a line (abcde), they 
# could do the following dance:
# 
# s1, a spin of size 1: eabcd.
# x3/4, swapping the last two programs: eabdc.
# pe/b, swapping programs e and b: baedc.
# After finishing their dance, the programs end up in order baedc.
# 
# You watch the dance for a while and record their dance moves (your puzzle 
# input). In what order are the programs standing after their dance?
# 
# Your puzzle answer was fgmobeaijhdpkcln.
# 
# --- Part Two ---
# Now that you're starting to get a feel for the dance moves, you turn your 
# attention to the dance as a whole.
# 
# Keeping the positions they ended up in from their previous dance, the 
# programs perform it again and again: including the first dance, a total of 
# one billion (1000000000) times.
# 
# In the example above, their second dance would begin with the order baedc, 
# and use the same dance moves:
# 
# s1, a spin of size 1: cbaed.
# x3/4, swapping the last two programs: cbade.
# pe/b, swapping programs e and b: ceadb.
# In what order are the programs standing after their billion dances?
import collections
import re

def spin(sequence, rotate):
    sequence.rotate(int(rotate))

def exchange(sequence, pos_a, pos_b):
    temp_val = sequence[int(pos_a)]
    sequence[int(pos_a)] = sequence[int(pos_b)]
    sequence[int(pos_b)] = temp_val
    
def partner(sequence, val_a, val_b):
    temp_list = list(sequence)
    pos_a = temp_list.index(val_a)
    pos_b = temp_list.index(val_b)
    exchange(sequence, pos_a, pos_b)

def dance(sequence, dance_move):
    if dance_move[0] == 's':
        num = re.search(r'\d+', dance_move).group(0)
        spin(sequence, num)
    elif dance_move[0] == 'x':
        pos = re.split('/', dance_move[1:])
        exchange(sequence, pos[0], pos[1])
    else:
        vals = re.split('/', dance_move[1:])
        partner(sequence, vals[0], vals[1])

def dance_list(filename):
    with open(filename, "r") as inputfile:
        return inputfile.readline()

def solve1(dance_list, sequence):
    progs = collections.deque(sequence)
    for move in re.split(',', dance_list):
        dance(progs, move)
    return list(progs) 

#Solution is that the solution 1 results repeat after 24 iterations
def solve2(dance_list, sequence, num_iters):
    possible = [reduce(lambda x, y: x + y, sequence)]
    progs = sequence
    for ___ in xrange(23):
        progs = solve1(d_list, progs) 
        possible.append(reduce(lambda x, y: x + y, progs))
    indx = num_iters % 24
    return possible[indx]

programs = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p']
d_list = dance_list("./2017/day16.txt")
#solve1(d_list, programs)
#print reduce(lambda x, y: x + y, programs)
print solve2(d_list, programs, 1000000000)