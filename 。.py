import numpy as np
from matplotlib import pyplot as plt
 
plt.figure(figsize=(10,6), dpi=80)
x = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(x), np.sin(x)
 
# 设置线的颜色，粗细，和线型
plt.plot(x, C, color="blue", linewidth=2.5, linestyle="-", label=r'$sin(x)$')
plt.plot(x, S, color="red",  linewidth=2.5, linestyle="-", label=r'$cos(x)$')
 
# 如果觉得线条离边界太近了，可以加大距离
plt.xlim(x.min()*1.2, x.max()*1.2)
plt.ylim(C.min()*1.2, C.max()*1.2)
 
# 当前的刻度并不清晰，需要重新设定,并加上更直观的标签
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1,0,1],
          [r'$-1$', r'$0$', r'$1$'])
 
# 添加图例
plt.legend()
 
plt.show()