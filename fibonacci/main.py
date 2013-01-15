
class fibonacci():
        
        def exponential( self, n ):
                # 'n' cannot be a class variable because it is not being shared, each time we call a member function we start with a new value of n

                if (n==0):
                        return 0
                elif (n==1):
                        return 1

                return self.exponential(n-1) + self.exponential(n-2)

        def polynomial( self, n ):
                if (n==0):
                        return 0
                fibonaaci_series = [-1 for x in range(0, n+1)]  # to force 'close interval' to python's range function

                fibonaaci_series[0] = 0;
                fibonaaci_series[1] = 1;

                for i in range(2, n+1):
                        fibonaaci_series[i] = fibonaaci_series[i-1] + fibonaaci_series[i-2]
                return fibonaaci_series[n]



if __name__ == "__main__":
        import cProfile
        fib = fibonacci()
        cProfile.run('fib.exponential(30)')
        cProfile.run('fib.polynomial(30)')
        print fib.exponential(20)
        print fib.polynomial(20)



## Message in readme : I am doing a fun project to test my skill. I am doing by S. Dasgupta, C.H. Papadimitriou, and U.V. Vazirani book. I have developed a personal theory over the time that if I am working out a mathematical model of something and I can repsent the same thing using a programming toolset that means I sense what really it is. So as I am doing stuffs and programming things I thought it would be great to push this code on github. Reference post : Less rules more life and then just life.
