def remove(x):
    y = "aeiou"
    z = "".join ([i for i in x if i not in y])
    return z
    


x = "hello world"
result = remove(x)
print(result)
    
       

    
