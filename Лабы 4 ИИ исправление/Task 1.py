import json

def task(filename: str) -> float:
    # Чтение файла
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

        total_sum = sum(i['score'] * i['weight'] for i in data if 'score' and 'weight' in i)

    return round(total_sum, 3)

if __name__ == '__main__':
    filename = 'input.json'
    print(task(filename))