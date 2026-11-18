import math as m
#Basic calculation
def check_positive(*values):
    if any(value <= 0 for value in values):
        raise ValueError("All dimensions must be positive")
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if (b==0):
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return a/b
def remainder(a,b):
    if (b==0):
         raise ZeroDivisionError("Cannot divide by zero")
    else:
        return a%b
def power(a,b):
    if a==0 and b<0:
        raise ZeroDivisionError("Zero cannot have a negative power")
    return a**b
def square(a):
    return a**2
def cube(a):
    return a**3
def square_root(a):
    if a<0:
        raise ValueError("Negative Number not allowed")
    return m.sqrt(a)
#Scientific
def sin(a):
    return m.sin(m.radians(a))
def cos(a):
    return m.cos(m.radians(a))
def tan(a):
    return m.tan(m.radians(a))
def log(a):
    if a <= 0:
        raise ValueError("Log requires a positive number")
    return m.log(a)
def factorial(a):
    if a<0 or type(a)!=int:
        raise ValueError("Factorial requires a non-negative integer")
    return m.factorial(a)
# Length Conversion
def m_to_cm(a):
    return a*100
def cm_to_m(a):
    return a/100
def km_to_m(a):
    return a*1000
def cm_to_mm(a):
    return a*10
def m_to_km(a):
    return a/1000
def mm_to_cm(a):
    return a/10
def km_to_mile(a):
    return a*0.621371
def mile_to_km(a):
    return a*1.609344
def inch_to_cm(a):
    return a*2.54
def feet_to_m(a):
    return a*0.3048
def m_to_feet(a):
    return a*3.28084
def yard_to_m(a):
    return a*0.9144
#Mass Convrsion
def g_to_kg(a):
    return a/1000
def kg_to_g(a):
    return a*1000
def g_to_mg(a):
    return a*1000
def mg_to_g(a):
    return a/1000
def pound_to_kg(a):
    return a*0.45359237
def kg_to_pound(a):
    return a*2.2046226218
def tonne_to_kg(a):
    return a*1000
def kg_to_tonne(a):
    return a/1000
def ounce_to_g(a):
    return a*28.3495
#Temperature
def C_to_F(a):
    return (a*9/5)+32
def K_to_C(a):
    if a < 0:
        raise ValueError("Kelvin cannot be negative")
    return a-273.15
def F_to_C(a):
    return (a-32)*5/9
def C_to_K(a):
    return a+273.15
def f_to_k(a):
    return (a-32)*5/9+273.15
def k_to_f(a):
    if a < 0:
        raise ValueError("Kelvin cannot be negative")
    return (a-273.15)*9/5+32
#Speed
def KMPH_to_MPS(a):
    return a/3.6
def MPS_to_KMPH(a):
    return a*3.6
def MPH_to_KMPH(a):
    return a*1.609344
def KMPH_to_MPH(a):
    return a/1.609344
def MPH_to_MPS(a):
    return a*0.44704
def MPS_to_MPH(a):
    return a/0.44704
#TIME

def h_to_m(a):
    return a*60
def m_to_s(a):
    return a*60
def h_to_s(a):
    return a*3600
def day_to_h(a):
    return a*24
def week_to_days(a):
    return a*7
def week_to_h(a):
    return a*168
def days_to_min(a):
    return a*1440
def year_to_days(a):
    return a*365
def ms_to_s(a):
    return a/1000
#volume 
def l_to_ml(a):
    return a*1000
def ml_to_l(a):
    return a/1000
def l_to_cubicmeter(a):
    return a/1000
def cubicmeter_to_l(a):
    return a*1000
def l_to_us_gallon(a):
    return a*0.264172
def us_gallon_to_l(a):
    return a*3.78541
def cubic_cm_to_ml(a):
    return a*1
#Area conversion
def square_m_to_square_cm(a):
    return a*10000
def square_km_to_square_m(a):
    return a*1000000
def hectare_to_square_m(a):
    return a*10000
def acre_to_square_m(a):
    return a*4046.86
def square_foot_to_square_m(a):
    return a*0.092903
#pressure conversion
def bar_to_pascal(a):
    return a*100000
def kilopascal_to_pascal(a):
    return a*1000
def atmosphere_to_pascal(a):
    return a*101325
def PSI_to_Pascal(a):
    return a*6894.76
def Bar_to_PSI(a):
    return a*14.5038
#data Storage conversion
def kb_to_bytes(a):
    return a*1000
def mb_to_kb(a):
    return a*1000
def gb_to_mb(a):
    return a*1000
def tb_to_gb(a):
    return a*1000
#                    GEOMETRY
#area
def square_area(a):
    check_positive(a)
    return a**2
def rectangle_area(l,b):
    check_positive(l,b)
    return l*b
def circle_area(r):
    check_positive(r)
    return m.pi*r*r
def triangle_area(b,h):
    check_positive(b,h)
    return 1/2*b*h
def paralellogram_area(b,h):
    check_positive(b,h)
    return b*h
def rhombus_area(d1,d2):
    check_positive(d1,d2)
    return 1/2*d1*d2
def trapezium_area(a,b,h):
    check_positive(a,b,h)
    return 1/2*(a+b)*h
def equilateral_triangle_area(a):
    check_positive(a)
    return (m.sqrt(3)/4)*a**2
#Perimeter
def square_perimeter(a):
    check_positive(a)
    return 4*a 
def rectangle_perimeter(l,b):
    check_positive(l,b)
    return 2*(l+b)
def circle_circumference(r):
    check_positive(r)
    return 2*m.pi*r
def triangle_perimeter(a,b,c):
    check_positive(a,b,c)
    if a+b <= c or a+c <= b or b+c <= a:
        raise ValueError("Invalid triangle sides")
    return a+b+c
def parallelogram_perimeter(a,b):
    check_positive(a,b)
    return 2*(a+b)
def rhombus_perimeter(a):
    check_positive(a)
    return 4*a
def trapezium_perimeter(a,b,c,d):
    check_positive(a,b,c,d)
    return a+b+c+d
def equilateral_triangle_perimeter(a):
    check_positive(a)
    return 3*a
#volume
def volume_cube(a):
    check_positive(a)
    return a**3
def volume_cuboid(l,b,h):
    check_positive(l,b,h)
    return l*b*h
def volume_cylinder(r,h):
    check_positive(r,h)
    return m.pi*r*r*h
def volume_cone(r,h):
    check_positive(r,h)
    return 1/3*m.pi*r*r*h
def volume_sphere(r):
    check_positive(r)
    return 4/3*m.pi*r**3
def volume_hemisphere(r):
    check_positive(r)
    return 2/3*m.pi*r**3
def volume_triangular_prism(b, h, L):
    check_positive(b,h,L)
    return 0.5 * b * h * L
def volume_square_pyramid(a, h):
    check_positive(a,h)
    return (a ** 2 * h) / 3
def volume_rectangular_pyramid(l, b, h):
    check_positive(l,b,h)
    return (l * b * h) / 3

# Cube
def tsa_cube(a):
    check_positive(a)
    return 6 * a ** 2
def lateral_area_cube(a):
    check_positive(a)
    return 4 * a ** 2
# Cuboid
def tsa_cuboid(l, b, h):
    check_positive(l,b,h)
    return 2 * (l*b + b*h + h*l)
def lateral_area_cuboid(l, b, h):
    check_positive(l,b,h)
    return 2 * h * (l + b)
# Cylinder
def tsa_cylinder(r, h):
    check_positive(r,h)
    return 2 * m.pi * r * (r + h)
def curved_area_cylinder(r, h):
    check_positive(r,h)
    return 2 * m.pi * r * h
# Cone
def tsa_cone(r, h, l):
    check_positive(r, h, l)

    expected_l = m.sqrt(r**2 + h**2)

    if not m.isclose(l, expected_l):
        raise ValueError("Invalid cone dimensions")

    return m.pi * r * (r + l)
def curved_area_cone(r, slant_height):
    check_positive(r,slant_height)
    return m.pi * r * slant_height
# Sphere
def surface_area_sphere(r):
    check_positive(r)
    return 4 * m.pi * r ** 2
# Hemisphere
def tsa_hemisphere(r):
    check_positive(r)
    return 3 * m.pi * r ** 2
def curved_area_hemisphere(r):
    check_positive(r)
    return 2 * m.pi * r ** 2
# Square Pyramid
def tsa_square_pyramid(a, h, l):
    check_positive(a, h, l)

    expected_l = m.sqrt(h**2 + (a/2)**2)

    if not m.isclose(l, expected_l):
        raise ValueError("Invalid pyramid dimensions")

    return a**2 + 2*a*l
def lateral_area_square_pyramid(a, slant_height):
    check_positive(a,slant_height)
    return 2 * a * slant_height


# Number system conversion
def binary_to_decimal(n):
    return int(str(n), 2)
def binary_to_octal(n):
    return format(int(str(n), 2), 'o')
def binary_to_hexadecimal(n):
    return format(int(str(n), 2), 'X')
def decimal_to_binary(n):
    return format(int(str(n), 10), 'b')
def decimal_to_octal(n):
    return format(int(str(n), 10), 'o')
def decimal_to_hexadecimal(n):
    return format(int(str(n), 10), 'X')
def octal_to_binary(n):
    return format(int(str(n), 8), 'b')
def octal_to_decimal(n):
    return int(str(n), 8)
def octal_to_hexadecimal(n):
    return format(int(str(n), 8), 'X')
def hexadecimal_to_binary(n):
    return format(int(str(n), 16), 'b')
def hexadecimal_to_decimal(n):
    return int(str(n), 16)
def hexadecimal_to_octal(n):
    return format(int(str(n), 16), 'o')


# Number Analyzer
def is_prime(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**0.5) + 1):
            if n%i==0:
                return False
                 
        return True
def is_armstrong(n):
    if n<0:
        return False
    temp=n
    l=len(str(n))
    a=0
    while(n!=0):
        rem=n%10
        a=a+rem**l
        n=n//10
    if a==temp:
        return True
    else:
        return False
def is_palindrome(n):
    if n<0:
        return False
    n=str(n)
    if n==n[::-1]:
        return True
    else:
        return False
def is_perfect(n):
    if n<=0:
        return False
    total=0
    for i in range(1,n):
        if n%i==0:
            total=total+i
    return total==n
def fibonacci(n):
    if n<=0:
        return []
    a=0
    b=1
    result=[]
    for i in range(n):
        result.append(a)
        a,b=b,a+b
    return result

