
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
Выберем строку с `dont_give_flag` нажмем левую кнопку мыши и в меню выберем пункт `Follow constant in Dump`.
![image](https://github.com/user-attachments/assets/71201306-8cb8-4522-9568-605de22ab9ce)
![image](https://github.com/user-attachments/assets/de35049a-1c6c-4c28-8f0f-075f53b2edf5)

Нажимая сочетание клавиш `ctrl+e` пропатчим память. Должно получиться вот так: 
![image](https://github.com/user-attachments/assets/de3a046b-df3f-429c-9eb6-cffc6fd9ffe2)
Отпустим программму нажав клавишу `F9` и получим флаг: 

![image](https://github.com/user-attachments/assets/bf3b6e71-187d-49d3-85d6-c23f3e9d58f3)

Ответ: `spbctf{ed1t1ng_t3h_memory_l1ke_a_PRO}`

