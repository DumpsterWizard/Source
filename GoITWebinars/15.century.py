# Скласти програму визначення номера століття с за номером  n(n>0)  деякого року (врахувати що, наприклад, початком 20 століття був 1901, а не 1900 рік).

current_year = int(input("Enter year: "))

current_century = (current_year - 1) // 100 + 1
print(f"Current century: {current_century}")