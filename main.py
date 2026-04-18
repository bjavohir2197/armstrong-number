def son_armstrong(n):
    son = str(n)
    uzunlik = len(son)
    result = 0
    for i in range(uzunlik):
        result += int(son[i]) ** uzunlik
    return result == n

n = int(input("Sonni kiriting: "))
if son_armstrong(n):
    print(n, "Armstrong sonidir.")
else:
    print(n, "Armstrong soni emas.")
```

```python
def son_armstrong(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))

n = int(input("Sonni kiriting: "))
if son_armstrong(n):
    print(n, "Armstrong sonidir.")
else:
    print(n, "Armstrong soni emas.")
