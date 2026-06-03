# # PyTorch 深度学习环境测试

一个用于测试 Python 深度学习开发环境的小项目。当前代码主要验证 `PyTorch` 和 `NumPy` 是否安装正确，并演示基础张量创建与矩阵乘法。

## 项目内容

- 打印当前环境中的 PyTorch 与 NumPy 版本
- 随机生成两个张量
- 使用 `torch.matmul` 执行矩阵乘法
- 输出运行结果，用于确认本地深度学习环境可正常工作

## 目录结构

```text
xiaoceshi/
├── README.md
├── AGENTS.md
└── pythonProject/
    └── DeepLearningProjrct/
        └── train_model.py
```

## 环境要求

建议使用 Python 3.9 或更高版本。

需要安装：

```powershell
pip install torch numpy
```

如果你使用虚拟环境，可以先创建并激活环境：

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install torch numpy
```

## 运行方式

在仓库根目录执行：

```powershell
python pythonProject\DeepLearningProjrct\train_model.py
```

运行后会看到类似输出：

```text
PyTorch version: ...
NumPy version: ...

Tensor A (3x4):
...

Tensor B (4x2):
...

Result of Matrix Multiplication (3x2):
...

代码编写和运行环境准备就绪！
```

## 适用场景

这个仓库适合用于：

- 检查 Python 深度学习环境是否配置成功
- 熟悉 PyTorch 张量的基础操作
- 作为后续深度学习模型训练代码的起点

## 后续可扩展方向

- 增加 `requirements.txt` 管理依赖
- 修正目录名 `DeepLearningProjrct` 中的拼写问题
- 增加简单数据集加载与模型训练示例
- 增加实验记录和结果保存目录
