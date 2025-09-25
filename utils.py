import gzip, struct, numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import random

# Loader for IDX format (Oracle-MNIST is packaged like MNIST)
def read_idx(filename):
    with gzip.open(filename, 'rb') as f:
        zero, data_type, dims = struct.unpack(">HBB", f.read(4))
        shape = tuple(struct.unpack(">I", f.read(4))[0] for d in range(dims))
        data = np.frombuffer(f.read(), dtype=np.uint8)
        return data.reshape(shape)

# Update to your local path
base_path = './data/oracle'

images_train = read_idx(f'{base_path}/train-images-idx3-ubyte.gz')
labels_train = read_idx(f'{base_path}/train-labels-idx1-ubyte.gz')
images_test  = read_idx(f'{base_path}/t10k-images-idx3-ubyte.gz')
labels_test  = read_idx(f'{base_path}/t10k-labels-idx1-ubyte.gz')