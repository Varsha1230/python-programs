# formula:-->  (0°C × 9/5) + 32 = 32°F

def farh(cel):
    return (cel*(9/5)) + 32

c = 45
f = farh(c)
print("fahrenhite temperature is " + str(f))
