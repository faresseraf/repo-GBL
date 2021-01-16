# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
time_per_sek = int(input('введите время в секундах'))
# count hours
hh = time_per_sek//3600
if hh < 10:
    hh = '0' + str(hh)
# count minutes
mm = (time_per_sek % 3600)//60
if mm < 10:
    mm = '0' + str(mm)
# count seconds
ss = time_per_sek % 60
if ss < 10:
    ss = '0' + str(ss)
print(f'Введеное время в секундах преобразованно в формат чч:мм:сс и равно {hh}:{mm}:{ss}')
