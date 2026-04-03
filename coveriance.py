import numpy as np

def coveriance(x_list,y_list) ->int:
    x_mean = np.mean(x_list)
    y_mean = np.mean(y_list)
    
    x_list = np.array(x_list)
    y_list = np.array(y_list)
    
    return sum((x_list - x_mean) * (y_list - y_mean)) / (len(x_list) - 1)

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

print(coveriance(x,y))