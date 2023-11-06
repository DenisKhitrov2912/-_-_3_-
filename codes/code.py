# Импортируем функции:
from functions import (json_encode, operation_date, last_five_operations, sorted_last_five, replace_number)

# Код для операций:
list_main = sorted_last_five(
    last_five_operations(json_encode("operations.json"), operation_date(json_encode("operations.json"))))
for every in list_main:
    try:
        date = every["date"].strftime("%d.%m.%Y")
        desc = every["description"]
        from_who = replace_number(every.get("from", ""))
        to_who = replace_number(every["to"])
        sum_oper = every["operationAmount"]["amount"]
        currency = every["operationAmount"]["currency"]["name"]
        print(f"""{date} {desc}
{from_who} -> {to_who}
{sum_oper} {currency}
""")
    except KeyError:
        continue
