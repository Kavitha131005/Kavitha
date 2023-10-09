def factorial(n):
  return 1 if (n==1 or n==0)else n * factorial (n-1);

#Enter input
n= int(input("enter input number:"))

print("the factorial of",n,"is", factorial (n))