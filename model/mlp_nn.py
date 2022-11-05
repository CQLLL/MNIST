import numpy as np


class Network(object):
    def __init__(self, sizes):
        # 包含输入层、隐藏层、输出层，(权重矩阵的行，权重矩阵的列)--->(layer中神经元个数，输入进该layer的神经元个数)
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]

        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
