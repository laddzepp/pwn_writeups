
# Сайт: forkbomb.ru 
# Автор: mvros (Влад Росков)
# Сложность: easy 


Разберем первое задание из сезона pwn от spbctf. Дизассемблируем полученный 
бинарный файл и разберем алгоритм программы.

![image](https://github.com/user-attachments/assets/7452c046-5bf8-4c0c-9c51-3be1ad27a4fc)

Пробежавшись по программе сразу же понимаем, что ввода в данном случае не происходит, поэтому перезаписать адрес 
на стэке не получится. Данное задание предполагает работу в отладчике. В отладчике, в регистр RIP(Instruction Pointer) положим желаемый адрес 
и отпустим отладчик. Осталось только понять, какая функция отвечает за выдачу флага, перечислим их в формате `(name_of_func, address)`: \
`(_7_obfuscated_print_flag_obfuscated_print_flag_split_4, 0000000000400541)`,
`(_7_obfuscated_print_flag_obfuscated_print_flag_split_3, 00000000004005A0)`, 
`(_7_obfuscated_print_flag_obfuscated_print_flag_split_2, 00000000004005C0)`
`(_7_obfuscated_print_flag_obfuscated_print_flag_split_1, 00000000004014D0)`


