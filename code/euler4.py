def isPalindrome(num):
    num = str(num)
    return num == num[::-1]

products = {}
for x in range(1, 1000):
    for y in range(1,1000):
        product = x*y 
        if isPalindrome(product):
            products[x,y] = product 
print products
print max(products.values())