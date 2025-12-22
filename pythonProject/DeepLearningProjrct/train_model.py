# train_model.py

import torch
import numpy as np

# 打印版本信息，确认库已正确安装
print(f"PyTorch version: {torch.__version__}")
print(f"NumPy version: {np.__version__}")

# 简单的张量运算练习
tensor_A = torch.rand(3, 4)
print("\nTensor A (3x4):")
print(tensor_A)

tensor_B = torch.rand(4, 2)
print("\nTensor B (4x2):")
print(tensor_B)

# 矩阵乘法
result = torch.matmul(tensor_A, tensor_B)
print("\nResult of Matrix Multiplication (3x2):")
print(result)

print("\n代码编写和运行环境准备就绪！")