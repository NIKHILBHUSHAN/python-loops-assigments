import numpy as np 

temp_celsius=np.array([22, 25, 28, 24, 26])

temp_fahrenheit=temp_celsius*1.8+32

print("Celsius: ",temp_celsius)
print("Fahrenheit: ",temp_fahrenheit)

avg_fahrenheit=round(temp_fahrenheit.mean(),1)

print(f"Average: {avg_fahrenheit}")