#!/usr/bin/env python
# coding: utf-8

# # 0. Наибольший общий делитель - 1 балл
# Напишите функцию, которая на вход принимает два целых числа, а на выходе отдает их наибольших общий делитель. 
# 
# Пример
# 
# Ввод 
# 
# `lcd(10,2)`
# 
# Вывод
# 
# `2`
# 
# Пример
# 
# Ввод 
# 
# `lcd(10,25)`
# 
# Вывод
# 
# `5`

# In[6]:


a = int(input())
b = int(input())
 
def euclid(x, y):
   while x != y:
       if x > y:
           x = x - y
       else:
           y = y - x
   return x
 
print(euclid(a, b))


# # 1. Задачка про перевод из `camel_case`'a в `snake_case` - 1.5 балла
#  Напишите функцию, которая на вход принимает строку, записанную в `CamelCase`, а переводит ее в `snake_case`.
#  Подсказка: идите по строке циклом, обрабатывайте каждый символ, если символ заглавный, к обработанным ранее добавляйте нижнее подчеркивание и нынешний переводите в `lower case` 
#  
#  Пример:
# 
# **Вход**: `'camelCaseVar'`
# 
# **Выход**: `'camel_сase_var'`

# In[3]:


s = input()
 
 
def snake_case(x):
   s1 = ''
   for i in range(len(x)):
       if x[i].isupper():
           s1 += '_' + x[i].lower()
       else:
           s1 += x[i].lower()
   return s1
 
 
print(snake_case(s))


# # 2. Про Поросёнка Петра - 2 балла
# На плоскости в точке `(0,0)` стоит Поросёнок Пётр. Он умеет ходить налево, направо, вверх и вниз. Расстояние его прохода в какую-либо сторону измеряется в шагах. Когда он идет вправо, его первая координата увеличивается, когда влево - уменьшается. Когда он идет вверх, его вторая координата увеличивается, а когда вниз - уменьшается.
# С клавиатуры считывается число `N` - число ходов, которые сделает Пётр. После чего на каждом шаге спрашивается, сколько шагов и в какую сторону за этот ход Пётр сделает. Так происходит, пока Пётр не осуществит все N ходов.
# Программа должна вывести, сколько шагов Пётр должен был бы сделать, чтобы кратчайшим путем прибыть из свое начальной точки `(0,0)` в свою конечную точку. 
# 
# Напоминание: Пётр умеет ходить только вверх-вниз, и влево-вправо, но не по диагонали.
# 
# Пример ввода:
# 
# Введите N: `3`
# 
# Ход 1: `Вверх 1`
# 
# Ход 2: `Вниз 1`
# 
# Ход 3: `Вверх 1`
# 
# Пример вывода:
# `Пётр находится на расстоянии 1 от (0,0)`

# In[10]:


n  = int(input())
x = 0
y = 0
 
for i in range(n):
   a = input(f'Ход {i+1}: ').split(' ')
   if a[0] == "Вверх":
       y += int(a[1])
   elif a[0] == "Вниз":
       y -= int(a[1])
   elif a[0] == "Вправо":
       x += int(a[1])
   elif a[0] == "Влево":
       x -= int(a[1])
print(f"Пётр находится на расстоянии {abs(x)+abs(y)} от (0, 0)")


# In[ ]:





# # 3. Sort the keys of the dictionary from a to z.  - 0.5 балла

# In[11]:


d = {
   "tiramisu":5,
   "chocolate":2,
   "pudding":3,
   "cheesecake":4
   }
 
print(sorted(d.keys()))


# # 4. Compare three values, return true only if 2 or more values are equal - 0.5 балла

# In[12]:


a = int(input())
b = int(input())
c = int(input())
 
if (a == b) or (a == c) or (b == c) or (a == b == c):
   print('True')
else:
   print("False")


# # 5. Given a list with pairs, sort on the sum of pairs - 0.5 балла

# In[14]:


x = [(3,6),(4,7),(5,9),(8,4),(3,1)]
 
for i in range(len(x) - 1):
   for j in range(len(x) - 1 - i):
       if sum(x[j]) < sum(x[j + 1]):
           x[j], x[j + 1] = x[j + 1], x[j]
          
print(x)


# # 6. Create a function that takes a list of numbers. Return the largest number in the list. - 0.5 балла

# In[17]:


A = []
 
def findLargestNum(x):
   maxx = -10000
   for i in x:
       if int(i) > maxx:
           maxx = int(i)
   return maxx
 
 
x = int(input())
A = []
for i in range(x):
   A.append(input())
 
print(findLargestNum(A))


# # 7. Create a function that takes a string and returns the concatenated first and last character. - 0.5 балла

# In[18]:


a = input()
b = int(input())
 
def repetition(x, y):
   s = x*y
   return s
 
print(repetition(a,b))


# # 8. Create a function that takes a 2D list lst returns the sum of the minimum value in each row. - 0.5 балла

# In[19]:


k = 0
A = [
 [1, 2, 3, 4, 5],
 [5, 6, 7, 8, 9],
 [20, 21, 34, 56, 100]
]
 
for i in range(len(A)):
   minn = 1000000000
   for j in range(len(A[i])):
       if A[i][j] < minn:
           minn = A[i][j]
   k += minn
print(k)


# # 9. Create a function to return the amount of potatoes there are in a string. - 0.5 балла

# In[20]:


s = 'potato'
s1 = input()
 
 
def potatoes(x):
   return x.count(s)
 
 
print(potatoes(s1))


# # 10. Create a function that takes a list of integers as an argument and returns a unique number from that list. All numbers except unique ones have the same number of occurrences in the list. - 0.5 балла

# In[39]:


x = int(input())
A = []
for i in range(x):
   A.append(input())
 
 
def find_single_number(x):
   for i in x:
       if x.count(i) == 1:
           return i
           break
 
print(find_single_number(A))


# # 11. Given a letter and a list of words, return whether the letter does not appear in any of the words. - 0.5 балла

# In[24]:


n = int(input())
A = []
for i in range(n):
   A.append([el for el in input().split(',')])
 
def forbidden_letter(x):
   k = 0
   b = ''
   for i in x[0]:
       b = i
   for i in x[1]:
       if b in str(i):
           k = 1
           return False
           break
   if k == 0:
       return True
 
print(forbidden_letter(A))


# # 12.  Define a function which create a Pattern like this one.  - 2 балла

# In[ ]:


4


# In[33]:


s = int(input())
f = ''
for i in range(s+1):
   f += str(i)
def pattern(x):
   f1 = ''
   for i in range(len(f)):
       if i % 2 == 0:
           f1 += '||     ' + f[i] + '\n'
       else:
           f1 += '-----    ' + f[i] + '\n'
   return f1
 
print(f + "\n" + pattern(s))


# # 13. Create a function that takes three numbers as arguments and returns True if it's a triangle and False if not.  - 0.5 балла

# In[31]:


A = input().split(', ')
 
def is_triangle(x):
   a = int(x[0])
   b = int(x[1])
   c = int(x[2])
   if a + b > c:
       if a + c > b:
           if c + b > a:
               return True
           else:
               return False
       else:
           return False
   else:
       return False
 
print(is_triangle(A))


# # 14. Create a "Code" Generator that takes text as input and replaces some letter with another letter, and outputs the "encoded" message. Create funcs to encode and decode messages

# In[32]:


A = {
   'a': 'd',
   'b': 'e',
   'c': 'f',
   'd': 'g',
   'e': 'h',
   'f': 'i',
   'g': 'j',
   'h': 'k',
   'i': 'l',
   'j': 'm',
   'k': 'n',
   'l': 'o',
   'm': 'p',
   'n': 'q',
   'o': 'r',
   'p': 's',
   'q': 't',
   'r': 'u',
   's': 'v',
   't': 'w',
   'u': 'x',
   'v': 'y',
   'w': 'z',
   'x': 'a',
   'y': 'b',
   'z': 'c',
}
 
B = {
   'd': 'a',
   'e': 'b',
   'f': 'c',
   'g': 'd',
   'h': 'e',
   'i': 'f',
   'j': 'g',
   'k': 'h',
   'l': 'i',
   'm': 'j',
   'n': 'k',
   'o': 'l',
   'p': 'm',
   'q': 'n',
   'r': 'o',
   's': 'p',
   't': 'q',
   'u': 'r',
   'v': 's',
   'w': 't',
   'x': 'u',
   'y': 'v',
   'z': 'w',
   'a': 'x',
   'b': 'y',
   'c': 'z',
}
 
s = input()
 
def encode(x):
   s1 = ''
   for i in x:
       first = A[i]
       s1 += first
   return s1
s1 = encode(s)
def decode(x):
   s1 = ''
   for i in x:
       first = B[i]
       s1 += first
   return s1
print(encode(s), decode(s1))


# In[ ]:




