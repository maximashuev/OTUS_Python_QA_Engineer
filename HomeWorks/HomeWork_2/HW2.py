import json
from csv import DictReader

list_of_dict_with_users_from_json = []
with open('users-39204-8e2f95.json', 'r') as json_file:
    users_data = json.loads(json_file.read())
for member in users_data:
    list_of_dict_with_users_from_json.append(
        {key: value for key, value in member.items() if key in ["name", "gender", "address"]})

list_of_dict_with_books_from_csv = []
with open('books-39204-271043.csv', 'r') as csv_file:
    reader = DictReader(csv_file)
    for row in reader:
        dict_1 = {key: value for key, value in row.items() if key in ["Title", "Author", "Height"]}
        list_of_dict_with_books_from_csv.append({"books": [dict_1]})

result = []
for user_dict, book_dict in zip(list_of_dict_with_users_from_json, list_of_dict_with_books_from_csv):
    user_dict.update(book_dict)
    result.append(user_dict)

with open('result.json', 'w+') as result_file:
    result_file.write(json.dumps(result))
