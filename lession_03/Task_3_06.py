"""6. Реализовать функцию int_func(),
принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func()."""
def int_func(t):
    return t.title()

print(int_func('text'))
print(int_func('teЧП'))
print(int_func('text ad dw wqd qwd qwf wef  wef ew fwef wef ewfwe f wfwef  fdd'))
print(int_func('textW ad dw Wqd qwWd qwf wef  weWf eWWWw fwef wWef ewWWfwe f wWfwefW rW Wr Wfdd'))


