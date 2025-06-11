import json

def iter_numbers(data, ignore_red=False):
    items = []
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict):
        items = data.values()
        if ignore_red and 'red' in items:
            return
    else:
        return

    for item in items:
        if isinstance(item, (int, float)):
            yield item
        elif isinstance(item, (list, dict)):
            yield from iter_numbers(item, ignore_red=ignore_red)

if __name__ == '__main__':
    with open('day12_input') as f:
        data = json.load(f)
    print(sum(iter_numbers(data)))
    print(sum(iter_numbers(data, ignore_red=True)))
