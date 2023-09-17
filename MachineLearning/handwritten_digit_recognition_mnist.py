##########################################################################
#                                                                        #
#                    Handwritten Digit Recognition                       #
#                                                                        #
##########################################################################

'''
This script was originally from Samson Zhang Kaggle notebook.

The NN has a simple two-layer architecture. Input layer a[0] has 784 units 
corresponding to the 784 pixels in each 28x28 input image. A hidden layer 
a[1] has 10 units with ReLU activation. Finally the output layer a[2] has 
10 units corresponding to the ten digit classes with softmax activation.

* Forward propagation
Z[1]=W[1]X+b[1]
A[1]=gReLU(Z[1]))
Z[2]=W[2]A[1]+b[2]
A[2]=gsoftmax(Z[2])

* Backward propagation
dZ[2]=A[2]−Y
dW[2]=1mdZ[2]A[1]T
dB[2]=1mΣdZ[2]
dZ[1]=W[2]TdZ[2].∗g[1]′(z[1])
dW[1]=1mdZ[1]A[0]T
dB[1]=1mΣdZ[1]

* Parameter updates
W[2]:=W[2]−αdW[2]
b[2]:=b[2]−αdb[2]
W[1]:=W[1]−αdW[1]
b[1]:=b[1]−αdb[1]

* Variables and shapes

- Forward prop
A[0]=X: 784 x m
Z[1]∼A[1]: 10 x m
W[1]: 10 x 784 (as W[1]A[0]∼Z[1])
B[1]: 10 x 1
Z[2]∼A[2]: 10 x m
W[1]: 10 x 10 (as W[2]A[1]∼Z[2])
B[2]: 10 x 1

- Backprop
dZ[2]: 10 x m ( A[2])
dW[2]: 10 x 10
dB[2]: 10 x 1
dZ[1]: 10 x m ( A[1])
dW[1]: 10 x 10
dB[1]: 10 x 1
'''

############################### Imports ##################################
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


############################ Fetching Dataset ############################
# Only train data contain labels
data = pd.read_csv('../Data/Datasets/Mnist/train.csv')

# Converts to numpy array
data = np.array(data)
m, n = data.shape
# Shuffle before splitting into dev and training sets
np.random.shuffle(data) 

# Train data
data_train = data[1000:m].T
Y_train = data_train[0]
X_train = data_train[1:n]
X_train = X_train / 255.

# Test data
data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]
X_dev = X_dev / 255.

########################### Traning Functions ############################
def init_params():
    W1 = np.random.rand(10, 784) - 0.5
    b1 = np.random.rand(10, 1) - 0.5
    W2 = np.random.rand(10, 10) - 0.5
    b2 = np.random.rand(10, 1) - 0.5
    return W1, b1, W2, b2

def ReLU(Z):
    return np.maximum(Z, 0)

def softmax(Z):
    A = np.exp(Z) / sum(np.exp(Z))
    return A
    
def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

def ReLU_deriv(Z):
    return Z > 0

def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y

def backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y):
    one_hot_Y = one_hot(Y)
    dZ2 = A2 - one_hot_Y
    dW2 = 1 / m * dZ2.dot(A1.T)
    db2 = 1 / m * np.sum(dZ2)
    dZ1 = W2.T.dot(dZ2) * ReLU_deriv(Z1)
    dW1 = 1 / m * dZ1.dot(X.T)
    db1 = 1 / m * np.sum(dZ1)
    return dW1, db1, dW2, db2

def update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha):
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * db1    
    W2 = W2 - alpha * dW2  
    b2 = b2 - alpha * db2    
    return W1, b1, W2, b2

def get_predictions(A2):
    return np.argmax(A2, 0)

def get_accuracy(predictions, Y):
    return np.sum(predictions == Y) / Y.size

def gradient_descent(X, Y, alpha, iterations):
    W1, b1, W2, b2 = init_params()
    for i in range(iterations):
        Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
        dW1, db1, dW2, db2 = backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y)
        W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)
        if i % 50 == 0:
            print("Iteration: ", i)
            predictions = get_predictions(A2)
            print("Accuracy: ",get_accuracy(predictions, Y))
    return W1, b1, W2, b2

########################### Testing Functions ############################
def make_predictions(X, W1, b1, W2, b2):
    _, _, _, A2 = forward_prop(W1, b1, W2, b2, X)
    predictions = get_predictions(A2)
    return predictions

def test_prediction(index, W1, b1, W2, b2):
    current_image = X_train[:, index, None]
    prediction = make_predictions(X_train[:, index, None], W1, b1, W2, b2)
    label = Y_train[index]
    print("Prediction: ", prediction)
    print("Label: ", label)
    
    current_image = current_image.reshape((28, 28)) * 255
    plt.gray()
    plt.imshow(current_image)
    plt.show()


############################## Execution #################################
if __name__ == '__main__':
	print('############################################################')
	print('#                     MNIST Dataset                        #')
	print('############################################################')
	# Training the model
	print("####################   Training Model   ####################")
	W1, b1, W2, b2 = gradient_descent(X_train, Y_train, 0.10, 500)
	# Displaying a few test cases
	print("####################  Testing few cases ####################")
	test_prediction(0, W1, b1, W2, b2)
	test_prediction(1, W1, b1, W2, b2)
	test_prediction(2, W1, b1, W2, b2)
	# Testing final accuracy with untrained data
	print("####################    Testing model   ####################")
	dev_predictions = make_predictions(X_dev, W1, b1, W2, b2)
	print("Model accuracy: "+ str(get_accuracy(dev_predictions, Y_dev))+ "%")

