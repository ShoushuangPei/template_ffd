import numpy as np


def mesh3d(x, y, z, dtype=np.float32):
    grid = np.empty(x.shape + y.shape + z.shape + (3,), dtype=dtype)
    #np.empty产生随机矩阵
    #x.shape返回(x,y)类型
    #np.newaxis增加一个维度
    grid[..., 0] = x[:, np.newaxis, np.newaxis]
    grid[..., 1] = y[np.newaxis, :, np.newaxis]
    grid[..., 2] = z[np.newaxis, np.newaxis, :]
    return grid


def extent(x, *args, **kwargs):
    return np.min(x, *args, **kwargs), np.max(x, *args, **kwargs)
