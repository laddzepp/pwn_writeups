
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

