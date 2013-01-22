def x_modulo_N(x, N):
        return x % N # Merry goes round

def is_x_y_congruent_modulo_N(x, y, N):
        if( x_modulo_N(x, N) == x_modulo_N(y, N) ):
                return 1
        else:
                return 0

def equivalence_classes(N, integer_range):
        '''
        @integer_range : left and right limits for elements to be printed in one equvivalence class of 'N'

        Now things get interesting here :
        {i + kN : where k `belongs to` `integers Z`} for  0< i <= N-1
        two loops :
                'i' is ranging over (0,N-1]
                        and for each 'i' k is ranging over [integer_range) - '[' denotes close interval and ')' denotes open interval
        '''
        for i in range(0, N): # this is actually from 0 to N-1
                this_class = [ i + k*N for k in integer_range ] # Kudos to list comprehension 
                print this_class

def imply_substitution_rule( x, x1, y, y1, N ):
        '''
        if x===x1 (mod N) and y===y1 (mod N) then :
                x+y === x1+y1 (mod N)  AND xy = x1y1 (mod N)
        for example :
                25 x 3 mod 24 => 1 x 3 mod 24 [ As 25 === 1 mod 24 ]
                xy mod N => x1y mod N [ As x === x1 mod 24 ] ( here y = y1 if we are following the definition )
        '''
        if ( is_x_y_congruent_modulo_N( x, x1, N) and is_x_y_congruent_modulo_N( y, y1, N ) ):
                if ( is_x_y_congruent_modulo_N ( x+y, x1+y1, N ) and is_x_y_congruent_modulo_N( x*y, x1*y1, N ) ):
                        return 1
        
        return 0


        

if __name__ == "__main__":
        print x_modulo_N(75,24)

        print is_x_y_congruent_modulo_N(25,75,24)
        
        print is_x_y_congruent_modulo_N(75, x_modulo_N(75, 24), 24)  # 75 === 3 MOD 24 

        equivalence_classes(3, range(-5,5))

        print imply_substitution_rule( 25,1, 12, 36, 24) 
        # We can also test this substituion rule against 'equivalence classes of N within a given integer range Z
        # i.e. [ ... 25, 1, -23 .... ] or [ ....12, 36, 60.... ] is a snapshot of two equivalence class of 24 with center element being '1' and '12'
        # and we just used 25,1 and 12,36

'''
Output :
3
0
1
[-15, -12, -9, -6, -3, 0, 3, 6, 9, 12]
[-14, -11, -8, -5, -2, 1, 4, 7, 10, 13]
[-13, -10, -7, -4, -1, 2, 5, 8, 11, 14]
1
'''
