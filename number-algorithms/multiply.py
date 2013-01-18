import math

'''

8*4 Means `until ceil(4/2) becomes 1` times 8 is going to be considered for this : if in this 'recursive' context ceil(4/2) is even then return 2*8 otherwise if in this 'recursive' context ceil(4/2) is odd then return 8 + 2*( whatever the value we have from recursive calls ). We need to understand that 'primitive' number in this operation is '8' and how many times this primitve number '8' is going to be "left shifted ( doubled )" or is going to be "left shifted + added with itself" , is going to be decided by `until recursively ceil (4/2) becomes 1`

=> Abstract concept for x * y :
1. left shift cumulative value of multiplication that initializes 'x' itself, and right shift y
2. How many times we can right shift y = how many times we are going to left shift the cumuative value of multiplication ( z ) that initializes with 'x' because the innermost loop will return x + ( 2 * 0 ) = x itself.
3. If the value of y while right shifting is 'even' then we will just left shift 
4. If the value of y while right shifting is 'odd' we will ( left shift x '+' we will add x itself in this cumulative sum )

# It's fascinating, isn't it ?

Ouput :

X = 13, Y = 1 , Z = 0
X = 13, Y = 2 , Z = 13
X = 13, Y = 5 , Z = 26
X = 13, Y = 11 , Z = 65
143

'''

def multiply(x, y):
        
        if y==0: return 0

        z = multiply(x, int(math.ceil(y/2)))
        print "X = %d, Y = %d , Z = %d" % (x,y,z)

        if y%2 == 0:
                return 2*z
                #return multiply(2, z) ?
        
        else:
                return x + 2*z
                #return x + multiply(2, z) ?

if __name__ == "__main__":
        print multiply(13, 11)

                
