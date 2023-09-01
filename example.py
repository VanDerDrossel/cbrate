from cbrate import get_val_curs, filtred_by_char_code


# Получаем актуальный список курсов валют
current_rate = get_val_curs()

# Первый элемент (словарь) из списка. 
print(current_rate[0])

# Получаем информацию по интересующим нас валютам, 
# передав функции filtred_by_char_code буквенный код валюты, согласно ISO_4217
for valute in filtred_by_char_code(current_rate, 'AUD', 'EUR', 'USD', 'KGS'):
    print(f'Курс {valute["Name"]} на {valute["Date"]} составляет {valute["Value"]/valute["Nominal"]}')
