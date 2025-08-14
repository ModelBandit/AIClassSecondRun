# XOR (2-2-1) — slide-style training
# - Init weights = slide values
# - Train with BCE (with logits): dZ2 = sigmoid(Z2) - y
# - Plot MSE curve for visualization (like slide 8)

import numpy as np
import matplotlib.pyplot as plt

# ----- data -----
X = np.array([[0,0],
              [1,0],
              [0,1],
              [1,1]], dtype=float)           # (4,2)
y = np.array([[0],[1],[1],[0]], dtype=float) # (4,1)

# ----- hyperparams -----
lr = 0.02
epochs = 100_000

# ----- init weights/bias (same as slide 7) -----
# Input(2) -> Hidden(2)
W1 = np.array([[ 0.40, -0.30],
               [-0.35,  0.45]], dtype=float)   # (2x2)
b1 = np.array([[0.30, 0.30]], dtype=float)     # (1x2)

# Hidden(2) -> Output(1)
W2 = np.array([[ 0.50],
               [-0.60]], dtype=float)          # (2x1)
b2 = np.array([[0.40]], dtype=float)           # (1x1)

def sigmoid(z): return 1.0/(1.0+np.exp(-z))
def sigmoid_prime(a): return a*(1.0-a)         # a = sigmoid(z)

m = len(X)
mse_curve = []

# ----- train -----
for _ in range(epochs):
    # forward
    Z1 = X @ W1 + b1        # (4,2)
    A1 = sigmoid(Z1)        # (4,2)
    Z2 = A1 @ W2 + b2       # (4,1) logits
    Yhat = sigmoid(Z2)      # (4,1) probs (monitoring)

    # record MSE for the plot (no 0.5 factor, slide-style)
    mse_curve.append(np.mean((Yhat - y)**2))

    # backward — BCE with logits: dZ2 = sigmoid(Z2) - y
    dZ2 = (Yhat - y) / m                # (4,1)
    dW2 = A1.T @ dZ2                    # (2,1)
    db2 = np.sum(dZ2, axis=0, keepdims=True)  # (1,1)

    dA1 = dZ2 @ W2.T                    # (4,2)
    dZ1 = dA1 * sigmoid_prime(A1)       # (4,2)
    dW1 = X.T @ dZ1                     # (2,2)
    db1 = np.sum(dZ1, axis=0, keepdims=True)  # (1,2)

    # update
    W2 -= lr * dW2; b2 -= lr * db2
    W1 -= lr * dW1; b1 -= lr * db1

# ----- results -----
final_probs = Yhat                   # (4,1)
pred = (final_probs >= 0.5).astype(int)
acc = float((pred == y).mean())

print("Final outputs (prob.):", final_probs.ravel().tolist())
print("Predictions:", pred.ravel().tolist())
print("Accuracy:", acc)

# weights incl. bias as last row (like the slide table)
W1_full = np.vstack([W1, b1])  # (3,2)
W2_full = np.vstack([W2, b2])  # (3,1)
print("\nFinal Weights (Input -> Hidden):\n", W1_full)
print("\nFinal Weights (Hidden -> Output):\n", W2_full)

# ----- plot MSE curve -----
plt.figure()
plt.plot(mse_curve)
plt.title("Error reduction (MSE)")
plt.xlabel("Epochs")
plt.ylabel("Mean Squared Error")
plt.show()
