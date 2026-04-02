import numpy as np
def r2_score(y_ture,y_pred) ->float:
    y_bar = sum(y_ture) / len(y_ture)

    sse = np.sum((np.array(y_ture) - np.array(y_pred)) ** 2)

    sst = np.sum((np.array(y_ture) - y_bar) ** 2)

    return 1 - (sse / sst)

    # return sum(y_ture - y_pred)**2 / sum(y_ture - y_hat) **2

lst = [1,2,3,4,5,6,27,8,9]
lst1 = [2,3,4,5,6,7,18,9,10]
print(r2_score(lst,lst1))