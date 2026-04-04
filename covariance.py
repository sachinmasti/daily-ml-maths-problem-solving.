
import numpy as np

def corelation(x,y)->float:
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    x_std = np.std(x)
    y_std = np.std(y)
    
    x = np.array(x)
    y = np.array(y)

    covariance = sum((x - x_mean) * (y - y_mean)) / len(x)
    print(covariance)

    return covariance /( x_std * y_std)


x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
print(corelation(x,y))

