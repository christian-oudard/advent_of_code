def match_aunt(target, aunt, gt=None, lt=None):
    for key, value in target.items():
        aunt_value = aunt.get(key)
        if aunt_value is None:
            continue
        if gt is not None and key in gt:
            if not (aunt_value > value):
                return False
        elif lt is not None and key in lt:
            if not (aunt_value < value):
                return False
        elif not (aunt_value == value):
            return False
    return True


if __name__ == '__main__':
    with open('day16_input') as f:
        aunts = []
        for line in f.readlines():
            line = line.strip()
            name, props = line.split(': ', 1)
            aunt = {'name': name}
            for prop_str in props.split(', '):
                key, value = prop_str.split(': ')
                aunt[key] = int(value)
            aunts.append(aunt)

    target_props = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }
    for aunt in aunts:
        if match_aunt(target_props, aunt):
            print(aunt)
        if match_aunt(target_props, aunt, gt=['cats', 'trees'], lt=['pomeranians', 'goldfish']):
            print(aunt)
