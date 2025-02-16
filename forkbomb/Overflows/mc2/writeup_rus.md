
# Сайт: forkbomb 
# Задание: String
# Автор: mrvos (Vlad Roskov) 
# Сложность: Easy


Еще один таск из серии MicCheck. В данном случае потребуется отыскать 
строку в дампе памяти. Загрузим бинарный файл в IDA и попробуем разобраться, что к чему.

![image](https://github.com/user-attachments/assets/23faa652-a99c-42cd-a614-a389727ef29e)

Видим функцию `obfuscated_prepare_memory`. Как видно, данная функция деобфусцирует некоторый участок памяти, соответственно, мы не сможем 
увидеть содержимое в дампе памяти. Проверим это. Нажимаем клавишу `g` и IDA откроет меню, где мы можем указать на какой адрес мы хотим прыгнуть.

![image](https://github.com/user-attachments/assets/1cb2d55a-83ca-4f08-a124-7f32e0e14061)

Как и ожидалось, IDA не смогла распознать содержимое
![image](https://github.com/user-attachments/assets/14680bc5-900c-4f97-99c9-d0e35c0d023b)

Чтобы узнать желаемую строку необходимо вызвать функцию `obfuscated_prepare_memory` и в дампе памяти прыгнуть на адрес `0x61ebce`.
Осуществим это с помощью отладчка `edb`. 

Проходим функцию `obfuscated_prepare_memory` 
![image](https://github.com/user-attachments/assets/ef6a27d9-e7cf-46b3-bb59-deccd60497dc)

И в дампе памяти с помощью комбинации клавиш `ctrl+g` открываем меню `Go to Expression` и указываем в окне адрес `0x61ebce`. Получаем строку по данному адресу.

![image](https://github.com/user-attachments/assets/2142fc38-d647-4d19-931e-739c227454a1)

Ответ: westgate1697

