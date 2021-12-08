with open('day8_sample.txt') as f:
    result = f.read().splitlines()

"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
 """


example = 'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb'

# with open('day8_sample.txt') as f:
#     result = f.read().splitlines()
with open('day8_input.txt') as f:
    result = f.read().splitlines()

print(sum(1 for line in result
          for seq in line.split('|')[-1].split()
          if len(seq) not in (5, 6)))

result_list = []
for line in result:
    numbers, output = line.split('|')
    numbers = numbers.split()
    output = output.split()
    encoded_num = [set(num) for num in sorted(numbers, key=len)]
    decode = {}
    decode[1] = encoded_num[0]
    decode[6], = [number
                  for number in [num for num in encoded_num
                                 if len(num) == 6]
                  if len(decode[1] - number) == 1]
    decode[5], = [number
                  for number in [num for num in encoded_num
                                 if len(num) == 5]
                  if len(decode[6] & number) == 5]
    decode[4] = encoded_num[2]
    decode[7] = encoded_num[1]
    decode[3], = [number
                  for number in [num for num in encoded_num
                                 if len(num) == 5]
                  if len(decode[7] & number) == 3]
    decode[8] = encoded_num[-1]
    decode[2], = [number
                  for number in [num for num in encoded_num
                                 if len(num) == 5]
                  if number != decode[3] and number != decode[5]]

    decode[9], = [number
                  for number in [num for num in encoded_num
                                 if len(num) == 6]
                  if len(decode[3] & number) == 5]
    decode[0], = [number
                  for number in [num for num in encoded_num
                                 if len(num) == 6]
                  if number != decode[6] and number != decode[9]]

    encode = {out: set(list(out)) for out in output}

    output_value = ''.join([str(key) for encoded_number in output
                            for key, value in decode.items()
                            if encode[encoded_number] == value])
    result_list.append(int(output_value))

print(sum(result_list))