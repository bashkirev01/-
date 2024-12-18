# TODO импортировать необходимые молули
import csv
import json


def csv_to_json(csv_filename: str, json_filename: str, delimiter: str = ',', line_terminator: str = '\n'):
    data = []

    # Чтение CSV файла
    with open(csv_filename, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter, lineterminator=line_terminator)

        # Обходим строки CSV и добавляем их в список
        for row in reader:
            data.append(row)

    # Преобразование списка словарей в JSON
    json_data = json.dumps(data, indent=4, ensure_ascii=False)

    # Запись результатов в JSON файл
    with open(json_filename, mode='w', encoding='utf-8') as jsonfile:
        jsonfile.write(json_data)

    # Выводим JSON строку
    print(json_data)


if __name__ == '__main__':
    csv_filename = 'input.csv'
    json_filename = 'data.json'
    csv_to_json(csv_filename, json_filename)

