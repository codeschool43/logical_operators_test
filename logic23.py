def  bool_1(a):
   result = (a%10 + a//10%10 + a//100)%2 == 1
   return result