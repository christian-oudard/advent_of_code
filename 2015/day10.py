"""
>>> look_and_say('211')
'1221'
>>> look_and_say('1')
'11'
>>> look_and_say('11')
'21'
>>> look_and_say('21')
'1211'
>>> look_and_say('1211')
'111221'
>>> look_and_say('111221')
'312211'
>>> look_and_say('1', reps=5)
'312211'
"""

def look_and_say(string, reps=1):
    nums = [ int(c) for c in string ]
    for _ in range(reps):
        nums = list(_look_and_say(nums))
    return ''.join( str(n) for n in nums )

def _look_and_say(seq):
    seq = iter(seq)
    buffer = []
    for number in seq:
        if len(buffer) == 0:
            buffer.append(number)
        else:
            last = buffer[0]
            if number == last:
                buffer.append(number)
            else:
                yield len(buffer)
                yield last
                buffer = [number]
    if len(buffer) > 0:
        yield len(buffer)
        yield buffer[0]


if __name__ == '__main__':
    with open('day10_input') as f:
        s = f.read().strip()
    part_1_result = look_and_say(s, reps=40)
    print(len(part_1_result))
    part_2_result = look_and_say(part_1_result, reps=10)
    print(len(part_2_result))
