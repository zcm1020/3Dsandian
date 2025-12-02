import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 读取数据
df = pd.read_excel(r"C:\Users\zhangchuanming\Desktop\liewen.xlsx")

x = df['X']
y = df['Y']
z = df['Z']

# 创建图形 - 使用更窄更高的比例
fig = plt.figure(figsize=(8, 10))
ax = fig.add_subplot(111, projection='3d')

# 设置背景透明
fig.patch.set_alpha(0.0)  # 图形背景透明
ax.patch.set_alpha(0.0)   # 坐标轴背景透明

# 设置坐标轴平面透明
ax.xaxis.pane.set_alpha(0.0)
ax.yaxis.pane.set_alpha(0.0)
ax.zaxis.pane.set_alpha(0.0)

# 可选：设置坐标轴平面颜色为透明
ax.xaxis.pane.set_color('none')
ax.yaxis.pane.set_color('none')
ax.zaxis.pane.set_color('none')

# 绘制散点图
# 使用与填充色相同的边缘色
scatter = ax.scatter(x, y, z, c='red', s=10, alpha=0.5,    # s控制圆球大小  aplha控制透明度
                    edgecolors='red', linewidth=1)     #线宽1像素

# 获取数据范围
x_min, x_max = x.min(), x.max()
y_min, y_max = y.min(), y.max()
z_min, z_max = z.min(), z.max()

# 计算范围
x_range = x_max - x_min
y_range = y_max - y_min
z_range = z_max - z_min

# 方法A：使用set_box_aspect调整比例
# 增加Z轴的比例因子
z_scale_factor = 1.0  # 调整这个值来控制Z轴的长度
ax.set_box_aspect([x_range, y_range, z_range * z_scale_factor])

# 移除网格线
ax.grid(False)

# 创建透明灰色长方体边框
# 定义长方体的8个顶点
vertices = np.array([
    [x_min, y_min, z_min],
    [x_max, y_min, z_min],
    [x_max, y_max, z_min],
    [x_min, y_max, z_min],
    [x_min, y_min, z_max],
    [x_max, y_min, z_max],
    [x_max, y_max, z_max],
    [x_min, y_max, z_max]
])

# 定义长方体的6个面
faces = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],  # 底面
    [vertices[4], vertices[5], vertices[6], vertices[7]],  # 顶面
    [vertices[0], vertices[1], vertices[5], vertices[4]],  # 前面
    [vertices[2], vertices[3], vertices[7], vertices[6]],  # 后面
    [vertices[1], vertices[2], vertices[6], vertices[5]],  # 右面
    [vertices[0], vertices[3], vertices[7], vertices[4]]   # 左面
]

# 创建面集合
cube = Poly3DCollection(faces, alpha=0.1, facecolor='gray', edgecolor='gray', linewidth=1)
ax.add_collection3d(cube)

# 添加标签和标题
ax.set_xlabel('Xax', fontsize=12, labelpad=10)
ax.set_ylabel('Yay', fontsize=12, labelpad=10)
ax.set_zlabel('Zaz', fontsize=12, labelpad=10)
ax.set_title('3Dscatter', fontsize=14, pad=20)

# 调整视角
ax.view_init(elev=15, azim=30)

plt.tight_layout()
plt.show()