# Hãy thay thế các hàm lượng giác trong công thức của f(x) bằng khai triển Maclaurin bậc 3 (chứa x^3) và thực hiện lại phần (a).
# Maclaurin bậc 3:
# x*cos(x)= x-x^3/2!
# sin(x)= x-x^3/3!
# f = (x^3/3!-x^3/2!)/(x^3/3!)
import math
x = float(input("Input oX: "))
def giaithua(n):
    if n==0 or n==1:
        return 1
    else:
        return n*giaithua(n-1)
f = ((x**3)/giaithua(3)-(x**3)/giaithua(2))/((x**3)/giaithua(3))

print(round(f, 6))
