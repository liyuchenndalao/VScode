fahrenheit = 0
print("fahrenheit\tcelsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32)/1.8
    print("{:5d}\t{:7.2f}".format(fahrenheit,celsius))
    fahrenheit += 25