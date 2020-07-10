import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        return Complex(self.real+no.real,self.imaginary+no.imaginary)
        
    def __sub__(self, no):
         return Complex(self.real-no.real,self.imaginary-no.imaginary)        
    def __mul__(self, no):
         return Complex(self.real*no.real,self.imaginary*no.imaginary)
    def __truediv__(self, no):
         return complex(self.real*no.real-self.imaginary*no.imaginary, self.real*no.imaginary+self.imaginary*no.real)
    def __div__(self, no):
        try: 
            return self.__mul__(complex(no.real, -1*no.imaginarg)).__mul__(complex(1.0/(no.mod().real)**2, 0))
        except ZeroDivisionError as e:
            print (e)
            return None
    def mod(self):
        return complex(pow(self.real**2+self.imaginary**2, 0.5), 0)
    # def __str__(self, precision=2):
    #     return str(("%."+"%df"%precision)%float(self.real))+('+' if self.imag>=0 else '-')+str(("%."+"%df"%precision)%float(abs(self.imag)))+'i'        
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':