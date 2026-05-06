import numpy as np
import matplotlib.pyplot as plt


iter = np.array([4, 6, 8, 12, 16])
incorrect = np.array([13571, 21165, 28219, 42326, 56434])
mispred = np.array([43699.49, 70825.49, 94534.73, 141949.48, 189367.96])


# Scale cache misses for easier comparison on a single y-axis.
mispred_scaled = mispred / 10.0

plt.figure(figsize=(8, 5))
plt.plot(iter, mispred_scaled, marker='o', linestyle='-', linewidth=2, color='red', label='10 flushed cycles')
plt.plot(iter, incorrect, marker='s', linestyle='-', linewidth=2, color='cyan', label='Number of incorrect predictions')

plt.xlabel('Iterations')
plt.title('Number of incorrect predictions and attributed flushed cycles for CCh bench')
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend()
plt.tight_layout()
plt.savefig('cch_iter_scaling')
