start = eval(input("Enter the start point N:\n"))
end = eval(input("Enter the end point M:\n"))
print("The palindromic primes are:")

length = 0
prime_palindrome = 0
count = 0

for i in range(start + 1,end):
    temp = i
    reverse = 0
    while temp:
        rem = temp % 10
        temp = temp // 10
        reverse = reverse * 10 + rem
    if i == reverse:
        if reverse > 1:
            for j in range(2,reverse):
                if (reverse % j == 0):
                    break
            else:
                print(reverse)