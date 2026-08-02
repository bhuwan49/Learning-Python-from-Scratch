# problem statement :- 1+x+x²+x³+x⁴+x⁵+ ... + xⁿ
x = int(input('enter a number: \n'))
n = int(input('enter the range: \n'))
sum = 0
print('\n\n')
for i in range(n+1):
    sum = sum + x**i
print('\n\n')

print('sum = ', sum)

print('\n\n')

# C++ version of the same program
"""
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int x, n;
    long long sum = 0;

    cout << "enter a number: \n";
    cin >> x;

    cout << "enter the range: \n";
    cin >> n;

    for (int i = 0; i <= n; i++) {
        sum += pow(x, i);
    }

    cout << "\n\n";
    cout << "sum = " << sum << endl;
    cout << "\n\n";

    return 0;
}
"""

print('\n\n\n\n\n\n\n')


# 1+x+x²+x³+x⁴+x⁵+ ... + xⁿ

x = int(input('enter a number: \n'))
n = int(input('enter the range: \n')) 

total = 1

for i in range(1,n+1):
    total = total + pow(x,i)
print('\n\n')
print('total = ', total)

print("\n\n\n")


# 1-x+x²-x³+x⁴-x⁵+ ... + xⁿ

x = int(input('enter a number: \n'))
n = int(input('enter the range: \n')) 

total = 1

for i in range(1,n+1):
    total = total + pow((-x),i)
print('\n\n')
print('total = ', total)

print("\n\n\n")


# x-(x²/2)+(x³/3)-(x⁴/4)+(x⁵/5) ...  (xⁿ/n)

x = int(input('enter a number: \n'))
n = int(input('enter the range: \n')) 

total = 0

for i in range(1,n+1):
    total = total + ((-1)*(pow((-x),i)/i))
print('\n\n')
print('total = ', total)

print("\n\n\n")

## x+(x²/2!)-(x³/3!)+(x⁴/4!)-(x⁵/5!) ...  (xⁿ/n!)

import math

x = int(input('enter a number: \n'))
n = int(input('enter a range: \n'))

total = x
for i in range(2,n+1):
    total = total + (pow((-x), i)/(math.factorial(i)))
print('\n\n')

print('total = ',total)
    
print('\n\n\n')