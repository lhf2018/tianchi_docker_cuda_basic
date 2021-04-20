import torch
import numpy as np

device = torch.device("cuda")

# load array data
a = np.load("/tcdata/a.npy")
b = np.load("/tcdata/b.npy")

# transfer to tensor
a = torch.from_numpy(a)
b = torch.from_numpy(b)
a = a.to(device)
b = b.to(device)
c = torch.matmul(a, b)

# transfer to array and save data
c = c.cpu().numpy()
np.save("result.npy", c)
print(c)