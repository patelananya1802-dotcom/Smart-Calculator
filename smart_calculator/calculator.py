import math as m
#Basic calculation
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
    return m.log(a)
def factorial(a):
    if a<0 or not isinstance(a,int):
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
    return a*2.204622
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
    return a-273.15
def F_to_C(a):
    return (a-32)*5/9
def C_to_k(a):
    return a+273.15
def f_to_k(a):
    return (a-32)*5/9+273.15
def k_to_f(a):
    return (a-273.15)*9/5+32
#Speed
def KMPS_to_MPS(a):
    return a/3.6
def MPS_to_KMPS(a):
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
    if a<=0:
        raise ValueError("side always be positive")
    return a**2
def rectangle_area(l,b):
    if l<=0 and b<=0:
        raise ValueError("Length,breath always be positive")
    return l*b
def circle_area(r):
    if r<=0:
        raise ValueError("Radius always be positive")
    return m.pi*r*r
def triangle_area(b,h):
    return 1/2*b*h
def paralellogram_area(b,h):
    return b*h
def rhombus_area(d1,d2):
    return 1/2*d1*d2
def trapezium_area(a,b,h):
    return 1/2*(a+b)*h
def equilateral_triangle_area(a):
    return (m.sqrt(3)/4)*a**2
#Perimeter
def square_perimeter(a):
    if a>0:
            raise ValueError("side always be positive")
    return 4*a 
def rectangle_perimeter(l,b):
    if l>0 and b>0:
            raise ValueError("Length,breath always be positive")
    return 2*(l+b)
def circle_perimeter(r):
    if r>0:
            raise ValueError("Radius always be positive")
    return 2*m.pi*r
def triangle_perimeter(a,b,c):
    return a+b+c
def parallelogram_perimeter(a,b):
    return 2*(a+b)
def rhombus_perimeter(a):
    return 4*a
def trapezium_primeter(a,b,c,d):
    return a+b+c+d
def equilateral_triangle_perimeter(a):
    return 3*a
#volume
def volume_cube(a):
    return a**3
def volume_cuboid(l,b,h):
    return l*b*h
def volume_cylinder(r,h):
    return m.pi*r*r*h
def volume_cone(r,h):
    return 1/3*m.pi*r*r*h
def volume_sphere(r):
    return 4/3*m.pi*r**3
def volume_hemisphere(r):
    return 2/3*m.pi*r**3
def volume_triangular_prism(b, h, L):
    return 0.5 * b * h * L
def volume_square_pyramid(a, h):
    return (a ** 2 * h) / 3
def volume_rectangular_pyramid(l, b, h):
    return (l * b * h) / 3

# Cube
def tsa_cube(a):
    return 6 * a ** 2
def lateral_area_cube(a):
    return 4 * a ** 2
# Cuboid
def tsa_cuboid(l, b, h):
    return 2 * (l*b + b*h + h*l)
def lateral_area_cuboid(l, b, h):
    return 2 * h * (l + b)
# Cylinder
def tsa_cylinder(r, h):
    return 2 * m.pi * r * (r + h)
def curved_area_cylinder(r, h):
    return 2 * m.pi * r * h
# Cone
def tsa_cone(r, slant_height):
    return m.pi * r * (r + slant_height)
def curved_area_cone(r, slant_height):
    return m.pi * r * slant_height
# Sphere
def surface_area_sphere(r):
    return 4 * m.pi * r ** 2
# Hemisphere
def tsa_hemisphere(r):
    return 3 * m.pi * r ** 2
def curved_area_hemisphere(r):
    return 2 * m.pi * r ** 2
# Square Pyramid
def tsa_square_pyramid(a, slant_height):
    return a ** 2 + 2 * a * slant_height
def lateral_area_square_pyramid(a, slant_height):
    return 2 * a * slant_height
