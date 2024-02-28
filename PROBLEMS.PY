# #1.CHECKING WHETHER THE YEAR IS LEAP YEAR OR NOT
# year=int(input("Enter the year"))
# if year%4==0:
#     print("its an leap year")
# else:
#     print("its not an leap year")   


# 2.check whether the function is prime or not
# num=int(input("enter any number"))
# x=(num/2)+1
# if num>1 and x:
#     print(x,"entered number is a prime number")
# elif num==1:
#     print(num,"is either composite nor prime ")    
# else:
#     print(x,"entered number is not a prime number")


# #3.check the string is palindrome or not. 
word=str(input("enter any word"))
def palindrome(word):
    word=str(word)
    return word==word[::-1]
print(palindrome(word))

# #4.check the number of vowels in a string
# name=str(input("enter a sentance"))
# vowels='a','e','i','o','u'
# a=name.count('a')
# print("count of vowel a is",a)
# b=name.count('e')
# print("count of vowel e is",b)
# c=name.count('i')
# print("count of vowel i is",c)
# d=name.count('o')
# print("count of vowel o is",d)
# e=name.count('u')
# print("count of vowel u is",e)


# #5.multiplication table of 6.
# num=6
# i=1
# for i in range(1,11):
#     y=num*i
#     print(i,'x',num,'=',y)


