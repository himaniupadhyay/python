import json


def reverse(s):
    return s[::-1]


def is_palindrome(s):
    rev = reverse(s)

    if s == rev:
        return True
    return False


def do_process():
    with open('pala.json', 'r') as f:
        items = json.load(f)

    for item in items:
        item["is_palindrome"] = is_palindrome(item["name"])

    with open('pala_result.json', 'w') as f:
        json.dump(items, f)