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

        

if __name__ == "__main__":
        print x_modulo_N(75,24)

        print is_x_y_congruent_modulo_N(25,75,24)
        
        print is_x_y_congruent_modulo_N(75, x_modulo_N(75, 24), 24)  # 75 === 3 MOD 24 

        equivalence_classes(3, range(-5,5))


'''
Output :
3
0
1
[-15, -12, -9, -6, -3, 0, 3, 6, 9, 12]
[-14, -11, -8, -5, -2, 1, 4, 7, 10, 13]
[-13, -10, -7, -4, -1, 2, 5, 8, 11, 14]
'''
