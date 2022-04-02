sec_input = int(input('Введите секунды: '))

hour_in_sec = sec_input // 3600
min_in_sec = (sec_input // 60) % 60
sec_in_sec = sec_input % 60
if hour_in_sec < 10:
    hour_in_sec = '0' + str(hour_in_sec)
else:
    hour_in_sec = str(hour_in_sec)
if min_in_sec < 10:
    min_in_sec = '0' + str(min_in_sec)
else:
    min_in_sec = str(min_in_sec)
if sec_in_sec < 10:
    sec_in_sec = '0' + str(sec_in_sec)
else:
    sec_in_sec = str(sec_in_sec)
print(f'{hour_in_sec}:', f'{min_in_sec}:', f'{sec_in_sec}')