import numpy as np
import matplotlib.pyplot as plt


iter = np.array([4, 8, 12, 16])
cmiss = np.array([5077, 10153, 15229,  20305])
fe_stall = np.array([244132, 288244, 332357, 376470])


# Scale cache misses for easier comparison on a single y-axis.
cmiss_scaled = cmiss / 100.0
fe_stall_scaled = fe_stall / 10000

plt.figure(figsize=(8, 5))
plt.plot(iter, cmiss_scaled, marker='o', linestyle='-', linewidth=2, label='100 cache misses')
plt.plot(iter, fe_stall_scaled, marker='s', linestyle='-', linewidth=2, label='10000 front end stalls')

plt.xlabel('Iterations')
plt.title('Number of cache misses and attributed front-end stall cycles for the MIP microbenchmark')
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend()
plt.tight_layout()
plt.savefig('mip_iter_scaling')

