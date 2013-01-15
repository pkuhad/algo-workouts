import math

'''
8*4 Means `until ceil(4/2) becomes 1` times 8 is going to be considered for this : if in this 'recursive' context ceil(4/2) is even then return 2*8 otherwise if in this 'recursive' context ceil(4/2) is odd then return 8 + 2*( whatever the value we have from recursive calls ). We need to understand that 'primitive' number in this operation is '8' and how many times this primitve number '8' is going to be "left shifted ( doubled )" or is going to be "left shifted + added with itself" , is going to be decided by `until recursively ceil (4/2) becomes 1`

if we do 4*8 then it is vice-versa
'''

def multiply(x, y):
        
        if y==0: return 0

        z = multiply(x, int(math.ceil(y/2)))
        print "X = %d, Y = %d , Z = %d" % (x,y,z)

        if y%2 == 0:
                return 2*z
        
        else:
                return x + 2*z

if __name__ == "__main__":
        print multiply(13, 11)

                
