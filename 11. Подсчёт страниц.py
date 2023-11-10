# Результат пошуку згенерував n записів (вводиться користувачем). 
# Скільки сторінок потрібно для відображення цих записів, якщо на 1 сторінку виводиться 10 записів.

# Input - 64
# Output - 7

# Input - 10
# Output - 1

RECORD_PER_PAGE = 10

count_of_records = int(input("Enter counts of records: "))
pages_count = (count_of_records - 1) // RECORD_PER_PAGE + 1
print(f"Pages is equal to {pages_count}")