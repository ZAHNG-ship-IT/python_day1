# 启用内联绘图（仅适用于 Jupyter Notebook）
try:
    %matplotlib inline
except NameError:
    pass  # 如果不是在 Notebook 中运行，则跳过

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 检查 Matplotlib 后端
import matplotlib
print("当前 Matplotlib 后端:", matplotlib.get_backend())

# 定义符号变量
t, w = sp.symbols('t w', real=True)

# 定义信号表达式：2e^{-3t}u(t)
f1 = 2 * sp.exp(-3 * t) * sp.Heaviside(t)

# 计算傅里叶变换
F1 = sp.fourier_transform(f1, t, w, noconds=True)

# 简化结果
F1_simplified = sp.simplify(F1)
print("傅里叶变换结果:", F1_simplified)

# 将符号表达式转换为数值计算函数
F1_magnitude = sp.Abs(F1_simplified)
f_func = sp.lambdify(w, F1_magnitude, modules='numpy')

# 生成频率点
w_values = np.linspace(-10, 10, 1000)
magnitude_values = f_func(w_values)

# 检查计算结果
print("频率点:", w_values[:10])  # 打印前 10 个频率点
print("幅度值:", magnitude_values[:10])  # 打印前 10 个幅度值

# 绘图
plt.figure(figsize=(10, 5))
plt.plot(w_values, magnitude_values, linewidth=1.5, color='blue')
plt.xlabel('频率 ω (rad/s)', fontsize=12)
plt.ylabel('|F(ω)|', fontsize=12)
plt.title('幅度频谱: |2/(3 + jω)|', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(-10, 10)
plt.tight_layout()

# 强制保存图像到文件
plt.savefig('plot.png')  # 保存图像到文件
print("图像已保存为 'plot.png'")
