import fractions

def is_it_true(anything):
   	if anything:
     		print("yes, it's true")
   	else:
     		print("no, it's false")


is_it_true(1) 

is_it_true(-1)

is_it_true(0)

is_it_true(0.1) 

is_it_true(0.0)



is_it_true(fractions.Fraction(1, 2)) 

is_it_true(fractions.Fraction(0, 1))

is_it_true([]) 

is_it_true(['a'])  

 is_it_true([False]) 

is_it_true(())     

is_it_true(('a', 'b'))   

is_it_true((False,)) 

type((False)) 

type((False,))

 is_it_true(set())     

 is_it_true({'a'})  

is_it_true({False}) 

#NONE

type(None)

None == False

None == 0

None == ''

None == None

x = None

x == None

y = None

x == y

is_it_true(None)

is_it_true(not None)
