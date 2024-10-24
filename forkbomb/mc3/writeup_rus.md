
# Сайт: forkbomb.ru 
# Задание: Want The Flag ?
# Автор: mrvos (Vlad Roskov) 
# Сложность: Easy


Подходим к третьему заданию из серии MicCheck. В данном задании используется тот же бинарный файл, что и в задании `String`.
Логика все та же <br />
![image](https://github.com/user-attachments/assets/49251edd-f185-417b-842e-ed716a626bdd) <br /> 
С помощью функции `strcmp` у нас сравниваются две строки `dont_give_flag` и `I_WANT_THE_FLAG!`. Если строки совпадают переходим в эту ветку:  <br /> 
![image](https://github.com/user-attachments/assets/e56207a6-9dbf-485d-aca5-81e34e6bce1a) <br /> 
Если нет, то в эту: <br /> 
![image](https://github.com/user-attachments/assets/c4922860-b643-4264-8115-cc2220d33d85) 

Для того, чтобы получить флаг необходимо пропатчить память и изменить строку с `dont_give_flag` на `I_WANT_THE_FLAG!`. Сделаем это в отладчике edb.
![image](https://github.com/user-attachments/assets/093adf95-e9f5-4a60-a0f2-815fb17c7045)

