
'''
Напишите программу, которая проверяет, являются ли два введённых слова
анаграммами. Программа должна вывести True в случае, если введённые слова
являются анаграммами, и False в остальных случаях.

Sample Input:
Два слова, каждое на отдельной строке.
Слово может состоять только из латинских символов произвольного регистра.
Регистр символов не должен влиять на ответ.

Sample Output:
True или False.
'''
print(sorted(list(input().lower())) == sorted(list(input().lower())))