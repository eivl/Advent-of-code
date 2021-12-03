from collections import Counter
from enum import Enum

with open('day3_input.txt') as f:
    result = f.readlines()
result = [line.strip() for line in result]


class Gas(Enum):
    O2 = '10'
    CO2 = '01'


def find_life_support_rating(gas_list, gas: Gas):
    """
    Take the binary diagnostic and returns a rating. '10' for Oxygen and
    '01' for CO2
    :param gas_list: list of all binary values
    :param gas: enum with the binary values to check for
    :return: life support score
    """
    for i, _ in enumerate(result[0]):
        gas_bits = list(zip(*gas_list))
        if gas_bits[i].count('1') >= gas_bits[i].count('0'):
            gas_list = [row for row in gas_list if row[i] == gas.value[0]]
        else:
            gas_list = [row for row in gas_list if row[i] == gas.value[1]]
        if len(gas_list) == 1:
            score, = gas_list
            return int(score, base=2)


HALF_WAY = len(result) / 2

gamma = ['1' if col.count('1') > HALF_WAY else '0' for col in zip(*result)]
epsilon = ['0' if col.count('1') > HALF_WAY else '1' for col in zip(*result)]

gamma = int(''.join(gamma), base=2)
epsilon = int(''.join(epsilon), base=2)

print(gamma * epsilon)

ogxygen_rating = find_life_support_rating(result[:], Gas.O2)
co2_rating = find_life_support_rating(result[:], Gas.CO2)


print(ogxygen_rating * co2_rating)
