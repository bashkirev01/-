import json


def task(filename: str) -> float:
    total_sum = 0.0

    # Чтение файла
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

        for i in data:
            if 'score' and 'weight' in i:
                total_sum += i['score'] * i['weight']

    return round(total_sum, 3)


if __name__ == '__main__':
    filename = 'input.json'
    print(task(filename))

