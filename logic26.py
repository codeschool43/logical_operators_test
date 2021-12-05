def  bool_1(a):
    a1 = a%10
    a //= 10

    a2 = a%10
    a //= 10
    
    a3 = a%10
    a //= 10
    
    a4 = a%10
    a //= 10
    
    a5 = a%10
    
    result = a5 < a4 and a4 < a3 and a3 < a2 and a2 < a1
    return result