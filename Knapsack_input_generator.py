import random
import numpy as np  #Not necessary

n = 10 #Number of objects
min_object_weight = 1
max_object_weight = 8

approx_val_to_weight_ratio = 2
sigma_divide_value = 4 #This is the denominator of Sigma in val (line 16 & 18) - Just trying to generate sensible numbers

weights = []
for i in range(n):
    weights.append(random.randint(min_object_weight, max_object_weight))

values = []
for w in weights:
    val = int(random.gauss(mu= approx_val_to_weight_ratio*w, sigma= (max_object_weight - min_object_weight)*approx_val_to_weight_ratio/sigma_divide_value))
    while val < 1:
        val = int(random.gauss(mu= approx_val_to_weight_ratio*w, sigma= (max_object_weight - min_object_weight)*approx_val_to_weight_ratio/sigma_divide_value))
    values.append(val)

print('weights = ', weights)
print('values =  ', values)

print(np.array(values)/np.array(weights))