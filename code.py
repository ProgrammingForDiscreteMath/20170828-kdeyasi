from math import sqrt, atan, log
class ComplexNumber:
    """
    The class of complex numbers.
    """
    def __init__(self, real_part, imaginary_part):
        """
        Initialize ``self`` with real and imaginary part.
        """
        self.real = real_part
        self.imaginary = imaginary_part
    def __repr__(self):
        """
        Return the string representation of self.
        """
        return "%s + %s i"%(self.real, self.imaginary)
    def __eq__(self, other):
        """
        Test if ``self`` equals ``other``.
        
        Two complex numbers are equal if their real parts are equal and
        their imaginary parts are equal.
        """
        return self.real == other.real and self.imaginary == other.imaginary
    def modulus(self):
        """
        Return the modulus of self.
        
        The modulus (or absolute value) of a complex number is the square
        root of the sum of squares of its real and imaginary parts.
        """
        return sqrt(self.real**2 + self.imaginary**2)
    def sum(self, other):
        """
        Return the sum of ``self`` and ``other``.
        """
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    def product(self, other):
        """
        Return the product of two complex numbers
        
        Product of two complex numbers z = a + bi and w = c + di is equal to a*c - b*d + (a*d + b*c)i
        """
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)
    def complex_conjugate(self):
        """
        Return the complex conjugate of complex number
        
        This function does not return anything only replaces the instance for getting complex conjugate
        complex conjugate of z = a + bi is a - bi
        """
        self.real = self.real
        self.imaginary = - self.imaginary

class NonZeroComplexNumber(ComplexNumber):
    def __init__(self, real_part, imaginary_part):
        """
        Initialize ``self`` with real and imaginary parts after checking validity.
        """
        if real_part == 0 and imaginary_part == 0:
            raise ValueError("Real or imaginary part should be nonzero.")
        return ComplexNumber.__init__(self, real_part, imaginary_part)
    def inverse(self):
        """
        Return the multiplicative inverse of ``self``.
        """
        den = self.real**2 + self.imaginary**2
        return NonZeroComplexNumber(self.real/den, -self.imaginary/den)
    def polar_coordinates(self):
        """
        Return the polar co-ordinates from cartesian
        
        The formula of changing from cartesian (x + iy ) to polar (r, theta) is
              r = sqrt(x**2 + y**2), theta = atan(y/x) 
        """
        return self.real/self.modulus(), atan(self.imaginary/self.real)
    def logarithm(self):
        """
        Return the logarithm of complex number 
        
        Formula is that log(a + bi) = log(r) + theta i
        """
        a = self.polar_coordinates()
        
        return NonZeroComplexNumber(log(a[0]), a[1])