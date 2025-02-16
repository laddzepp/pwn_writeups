
# Сайт: forkbomb.ru 
# Название: Converter
# Автор: Ilya Glebov
# Сложность: Medium

Приступим к задачам, которые нацелены на умение ~~во моем случаеобучение~~ использовать библиотеку `pwntools`. Честно сказать, данная задачка заставила меня повозиться, так, как раньше `pwntools` и язык Python я использовал для 
совсем маленьких скрпитов. Тем не менее, задачу я решил и теперь могу поделиться своим решением. Приступим к решению. 
Для начала посмотрим, что из себя представляет программа: <br />
![image](https://github.com/user-attachments/assets/e7a94b52-cecc-4e75-85a0-a7850c152935) <br />
![image](https://github.com/user-attachments/assets/38e0ebb1-dbb3-413f-8585-ce54578a3cc5) <br />

Требуется перевести требуемое число в нужный формат (`Hex`, `LittleEndian64`, `BigEndian64`, `Octal`). Возникает закономерный вопрос, а как это парсить ? 
Разобьем данную задачу на три подзадачи: 
  - Извлекаем число из перевого сообщения `Conevert num_is_here to`
  - Парсим формат в который требуется перевести
  - Отправляем на сервер ввод

#### 1. Извлекаем число из перевого сообщения `Conevert num_is_here to`.
Давайте реализуем первую задачу. В `pwntools` есть функция, которая позволяет сразу считать строку в stdout'е программы. Называется она `recvline()`. Давайте попробуем 
считать первую строку stdout: 
```py
from pwn import * 

p = remote('109.233.56.90', 11573)
print(p.recvline())
```
![image](https://github.com/user-attachments/assets/8f9f3e93-167d-4630-93bf-67f4276c3d55)

Теперь попробуем извлечь число из данной строки. Данная функция присылает строку в байтах, поэтому,чтобы извлечь число нам потребуется предварительно 
перевести байты в обычные символы, разбить полученную строку по пробелам и вывести число на экран.

```py 
from pwn import * 

p = remote('109.233.56.90', 11573)
str_with_num = p.recvline().decode('utf-8').split(" ")
print(str_with_num[1])
```
![image](https://github.com/user-attachments/assets/15036042-26ff-4f69-b205-35532994ad3b) <br />

#### 2.  Парсим формат в который требуется перевести.

Итак, теперь нужно научить скрипт разпознавать формат в который требуется перевести. Можем заметить, что у всех картинок разная структура символов 
из которых они сделаны. Поэтому можем взять последнюю строчку "картинки" с форматом и на основе ее давать ответ в какой формат нужно перевести.

```py
from pwn import * 

p = remote('109.233.56.90', 11573)

str_with_num = p.recvline().decode('utf-8').split(" ")
print(str_with_num[1])
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
last_str = p.recvline().decode("utf-8")

if last_str == "|_| |_| \\___|/_/\\_\\\r\n":
    print('HEX')

elif last_str == " \\___/  \\___| \\__| \\__,_||_|\r\n":
    print('OCTAL')

elif last_str == "|____/ |_| \\__, | |_____||_| |_| \\__,_||_| \\__,_||_| |_| \\___/    |_|  \r\n":
    print('BIG ENDIAN')

elif last_str == "|_____||_| \\__| \\__||_| \\___| |_____||_| |_| \\__,_||_| \\__,_||_| |_| \\___/    |_|  \r\n":
    print('LITTLE ENDIAN')
```
![image](https://github.com/user-attachments/assets/d0ca8633-903a-481b-8bd5-0fc33ecf0631) <br />
![image](https://github.com/user-attachments/assets/b8e0b344-3da4-4678-a57a-3433c23ad094) <br />
![image](https://github.com/user-attachments/assets/db92d064-47d2-4669-9a2e-950edc10c5b8) <br />
![image](https://github.com/user-attachments/assets/83c2e7be-fb9c-4cdf-bcb6-9c191845693b) <br />

И как видим, данный способ действительно работает. Ну теперь осталось дело за малым, надо написать логику, которая переведет полученную строку в нужные форматы 
и отправить в виде байтов программе.

```py
from pwn import * 

p = remote('109.233.56.90', 11573)

while True:
    str_with_number = p.recvline()
    print(str_with_number)
    print(p.recvline())
    print(p.recvline())
    print(p.recvline())
    print(p.recvline())
    last_str = p.recvline().decode("utf-8")


    if last_str == "|_| |_| \\___|/_/\\_\\\r\n":  
        res = str_with_number.decode("utf-8").split(" ")
        hex_str = hex(int(res[1]))[2:]
        payload = bytes(hex_str , 'utf-8')
        p.sendline(payload)
        print(p.recvline())
        print(p.recvline())

    elif last_str == " \\___/  \\___| \\__| \\__,_||_|\r\n":  
        res = str_with_number.decode("utf-8").split(" ")
        oct_str = oct(int(res[1]))[2:]
        payload = bytes(oct_str , 'utf-8')
        p.sendline(payload)
        print(p.recvline())
        print(p.recvline())

    elif last_str == "|____/ |_| \\__, | |_____||_| |_| \\__,_||_| \\__,_||_| |_| \\___/    |_|  \r\n": 
        res = str_with_number.decode("utf-8").split(" ")
        num = int(res[1])
        p.sendline(p64(num, endian='big'))
        print(p.recvline())
        print(p.recvline())


    elif last_str == "|_____||_| \\__| \\__||_| \\___| |_____||_| |_| \\__,_||_| \\__,_||_| |_| \\___/    |_|  \r\n": 
        res = str_with_number.decode("utf-8").split(" ")
        num = int(res[1])
        p.sendline(p64(num))
        print(p.recvline())
        print(p.recvline())
```
Здесь я организовал цикл, для того,чтобы мы могли считать весь stdout, который нам присылает программа. В результате, мы получаем флаг: 
![image](https://github.com/user-attachments/assets/04ef5448-de1c-464a-a10c-ae5c7c283808)


Ответ: `spbctf{You_ARE_CONveRTEr_MSW600}`





