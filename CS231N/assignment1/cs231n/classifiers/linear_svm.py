import numpy as np
from random import shuffle

def svm_loss_naive(W, X, y, reg):
  """
  Structured SVM loss function, naive implementation (with loops).

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
  dW = np.zeros(W.shape) # initialize the gradient as zero

  # compute the loss and the gradient
  num_classes = W.shape[1]
  num_train = X.shape[0]
  loss = 0.0
  for i in range(num_train):
    scores = X[i].dot(W) #socre for different class,porjection
    correct_class_score = scores[y[i]]
    for j in range(num_classes):
      if j == y[i]:
        continue
      margin = scores[j] - correct_class_score + 1 # note delta = 1
      if margin > 0:
        loss += margin
        dW[:,j] += X[i].T
        dW[:,y[i]] += -X[i].T
        
  # Right now the loss is a sum over all training examples, but we want it
  # to be an average instead so we divide by num_train.
  loss /= num_train
  dW   /= num_train

  # Add regularization to the loss.
  loss += 0.5*reg * np.sum(W * W)
  dW   += reg*W
  #############################################################################
  # Compute the gradient of the loss function and store it dW.                #
  # Rather that first computing the loss and then computing the derivative,   #
  # it may be simpler to compute the derivative at the same time that the     #
  # loss is being computed. As a result you may need to modify some of the    #
  # code above to compute the gradient.                                       #
  #############################################################################

  return loss, dW


def svm_loss_vectorized(W, X, y, reg):
  """
  Structured SVM loss function, vectorized implementation.

  Inputs and outputs are the same as svm_loss_naive.
  """
  loss = 0.0
  dW = np.zeros(W.shape) # initialize the gradient as zero
  num_class,num_data = W.shape[1],X.shape[0]
  
  #############################################################################
  # Implement a vectorized version of the structured SVM loss, storing the    #
  # result in loss.                                                           #
  #############################################################################
  score = X.dot(W) 
  true_score = score[range(num_data),list(y)].reshape(-1,1)  #choose all the (i,y_i) reshape it to a column vector since next step needs column vector
  margins = np.maximum(0,score-true_score+1)
  margins[range(num_data),list(y)] = 0   #constraint  $j \ne y_i$ ,when sum(axis =1) ,the margin in y_i-column will b zero
  loss = np.sum(margins)/num_data+0.5*reg*np.sum(W*W)
  #############################################################################
  # Implement a vectorized version of the gradient for the structured SVM     #
  # loss, storing the result in dW.                                           #
  #                                                                           #
  # Hint: Instead of computing the gradient from scratch, it may be easier    #
  # to reuse some of the intermediate values that you used to compute the     #
  # loss.                                                                     #
  #############################################################################
  #IDEA: see the representation for m-row,n-column of dW.The high level idea is to see if no constaint how will the equation looks like,then we set all the place which has constraint be zero.
  id_matrix = np.zeros((num_data,num_class))
  id_matrix[margins>0] = 1
  id_matrix[range(num_data),list(y)] = 0
  id_matrix[range(num_data),list(y)] = -np.sum(id_matrix,axis = 1)
  dW = ((X.T).dot(id_matrix))/num_data  + reg*W
  
  return loss, dW
