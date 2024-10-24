
# Сайт: forkbomb.ru 
# Автор: mvros (Влад Росков)
# Сложность: easy 


Разберем первое задание из сезона pwn от spbctf. Дизассемблируем полученный 
бинарный файл и разберем алгоритм программы.

![image](https://github.com/user-attachments/assets/7452c046-5bf8-4c0c-9c51-3be1ad27a4fc)

#### Шаг 1. Статический анализ
Пробежавшись по программе сразу же понимаем, что ввода в данном случае не происходит, поэтому перезаписать адрес 
на стэке не получится. Данное задание предполагает работу в отладчике. В отладчике, в регистр RIP(Instruction Pointer) положим желаемый адрес 
и отпустим отладчик. Осталось только понять, какая функция отвечает за выдачу флага, перечислим их в формате `(name_of_func, address)`: \
`(_7_obfuscated_print_flag_obfuscated_print_flag_split_4, 0000000000400541)`,
`(_7_obfuscated_print_flag_obfuscated_print_flag_split_3, 00000000004005A0)`, 
`(_7_obfuscated_print_flag_obfuscated_print_flag_split_2, 00000000004005C0)`, 
`(_7_obfuscated_print_flag_obfuscated_print_flag_split_1, 00000000004014D0)`, <br />
`(obfuscated_print_flag, 00 00 00 00 00 4009E0)`


#### Шаг 2. Решение

Запустим отладичк командой `edb --run ./mc1`. Запустим программу с точки входа, нажав кнопку F9 и модифицируем RIP.
Перебрав все адреса фнукций начинающиеся на _7_..., можем предположить, что функция `obfuscated_print_flag` и есть та функция, которая 
выдаст флаг. Проверим данное предположение: <br />
![image](https://github.com/user-attachments/assets/829502a3-f158-4aec-af3d-643adf339990)
![image](https://github.com/user-attachments/assets/f230e127-bc1e-4e92-a828-9e6788687904)

Как видим, наше предположение оказалось верным и флаг был выдан.
![image](https://github.com/user-attachments/assets/9b17311b-db68-4e3b-9ac7-7a24c258b730)


Ответ: `spbctf{jumpy_jump_t0_th3_n33ded_func}`









