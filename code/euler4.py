def isPalindrome(num):
    """Tests if a number is a Palindrome
    en.wikipedia.org/wiki/Palindrome
    """
    num = str(num)
    return num == num[::-1]
if __name__ == '__main__':
        
    products = {}
    for x in range(1, 1000):
        for y in range(1,1000):
            product = x*y 
            if isPalindrome(product):
                products[x,y] = product 
    print products
    print max(products.values())