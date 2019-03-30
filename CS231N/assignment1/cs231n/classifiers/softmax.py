import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  num_data,num_class = X.shape[0],W.shape[1]
  #############################################################################
  #       Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  for i in range(num_data):
      score = X[i].dot(W)
      score -= max(score)  #stablebility
      exp_score = np.exp(score)
      loss += np.log(np.sum(exp_score)) - score[y[i]]
      dW[:,y[i]] -= X[i].T
      for j in range(num_class):
          dW[:,j] += (X[i].T)*(exp_score[j]/np.sum(exp_score))
  loss = loss/num_data + reg*np.sum(W*W)
  dW = dW/num_data + reg*W
  return loss, dW

def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_class, num_data  = W.shape[1],X.shape[0]
  #############################################################################
  #Compute the softmax loss and its gradient using no explicit loops.         #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  score_matrix = X.dot(W)
  C_score = score_matrix - np.max(score_matrix,axis = 1).reshape(-1,1) #since we sum over axis ,hence we get all the column maximum for each coulmn
  exp_score = np.exp(C_score)/np.sum(np.exp(C_score),axis = 1).reshape(-1,1)
  #sum all the y_i
  loss = -np.sum(np.log(exp_score[range(num_data),list(y)]))/num_data + reg*np.sum(W*W)


  id_matrix = exp_score
  id_matrix[range(num_data),list(y)] += -1
  dW = (X.T).dot(id_matrix)/num_data + reg*W
  return loss, dW
