import torch
import numpy as np

# initialising a tensor
d = [["A", "B", "C"], 
        ["D", "E", "F"]]

data = [[1, 2,3], [4, 5, 6]]
t1 = torch.tensor(data)
print(t1)
print(type(t1))

arr = np.ones_like(data)
t2 = torch.from_numpy(arr)



# NOTE: UNLIKE NUMPY ARRAYS, TENSORS IN PYTORCH DO NOT SUPPORT STRINGS OR CHARACTERS. ONLY INT, FLOAT, BOOL
# AND  COMPLEX DATATYPES ARE SUPPORTED

# ATTRIBUTES: shape, dtype and device


# USING AN ACCERLERATOR
# print(torch.__version__)
# print(torch.accelerator.is_available())
# print(torch.accelerator.current_accelerator())


[
    [[1, 2, 3], [3, 4, 5]]
    [[6, 7, 8], [8, 9, 10]]
    [[11, 12, 13], [13, 14, 15]]
]

[[2, 4], [7, 9], [12, 14]]