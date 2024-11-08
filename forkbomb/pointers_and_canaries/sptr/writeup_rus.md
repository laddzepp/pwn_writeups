# Сайт: forkbomb.ru 
# Автор: @korniltsev (Anatoly Korniltsev)
# Название: sptr
# Сложность: Easy

В данном блоке предложены задачи на перетирание адресов. Перетирание адреса и изменения поведения программ является одним из ключевых навыков на любом CTF. В данных задачах важно понимать суть атаки, поэтому на небольших задачах листниг в ассемблере больше разбирать не будем. Начнем решение: <br />
![image](https://github.com/user-attachments/assets/d382dd4b-817d-4dc3-a60d-ba50a2bd6b16)

Изначально указатель содержит адрес указывающий на строку `NO WIN`. Наша задача его перезаписать. Для того, чтобы его перезаписать нам необходимо переполнить статический
массив `auStack_18`, а рядом, написать новый адрес (естественно в little endian). Найдем адрес, указывающий на строку `WIN`. Обратим внимание на данный код: <br />

![image](https://github.com/user-attachments/assets/6c95d6e3-22c6-464e-9063-f1164cc14087)

Здесь используется функция `strcmp`, которая сравнивает две строки. Регистр `RDI` кладется первый аргумент, который представляет из себя строчку `NO WIN`. В регистр `RSI` пойдет второй аргумент, который адресом указывающий на строчку `WIN`. Нажмем на `DAT_00402058` и узнаем адрес: <br />

![image](https://github.com/user-attachments/assets/bdc1b672-2b91-4d87-9ff9-1ef5bbf7bc38)

Напишем скрипт, который отправит наш ввод. Сначала получим локальный флаг, а затем настоящий: 

```py
p = process('./sptr')
win_addr = 0x402058
p.sendline(b"AAAAAAAA" + p64(win_addr))
p.interactive()

```
![image](https://github.com/user-attachments/assets/bdec7ead-e676-4f20-acac-fc21bc677591) <br />

Получилось, а значит можем запустить программу на сервере:

```py
from pwn import * 

p = remote('109.233.56.90', 11600)
win_addr = 0x402058
p.sendline(b"AAAAAAAA" + p64(win_addr))
p.interactive()
```

![image](https://github.com/user-attachments/assets/c86f4aa4-1813-4dd4-9966-ca2ec9cc49c4) <br />

Ответ: `spbctf{b0e0b0cedc622b2396e0069cd5a5f568}`
