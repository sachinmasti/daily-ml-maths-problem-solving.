
# This function calculates the mean (average) of a list.
def mean(lst) ->float:
    return sum(lst) / len(lst)


# This function calculates the standard deviation of a list, 
# which measures how spread out the data is from the mean.
def std(lst) -> float:
    mean_lst = mean(lst)
    std_ = sum((x - mean_lst)**2 for x in lst) / len(lst)
    return std_ ** 0.5

# This function calculates the covariance between two variables (x and y),
# which indicates the direction of the linear relationship between them.
def covariance(x,y) -> float:
    mean_x = mean(x)
    mean_y = mean(y)
    return sum((x - mean_x) * (y - mean_y) for x,y in zip(x,y)) / len(x)

# This function calculates the correlation coefficient between two variables,
# which measures the strength and direction of their linear relationship.
def corelation(x,y) -> float:
    return covariance(x,y) / (std(x)* (std(y)))

x = [1,2,3,4,5,10]
y = [1,2,3,4,5,20]
print(corelation(x,y))

print(list(zip(x,y)))