import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


# Return fitted model parameters to the dataset at datapath for each choice in degrees.
# Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
# Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
# coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []

    file = open(datapath, 'r')
    data = file.readlines()
    x = []
    y = []
    for line in data:
        [i, j] = line.split()
        x.append(float(i))
        y.append(float(j))

    # iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    # for the model parameters in each case. Append the result to paramFits each time.
    for d in degrees:
        X = feature_matrix(x, d)
        paramFits.append(least_squares(X, y))

    return paramFits


# Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
# samples in x.
# Input: x as a list of the independent variable samples, and d as an integer.
# Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
# for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):

    # fill in
    # There are several ways to write this function. The most efficient would be a nested list comprehension
    # which for each sample in x calculates x^d, x^(d-1), ..., x^0.
    X = [[r**n for n in range(d,-1,-1)] for r in x]

    return X


# Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
# Input: X as a list of features for each sample, and y as a list of target variable samples.
# Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)
    #print(X)

    # fill in
    # Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    inv = np.linalg.inv(X.T @ X)
    B = inv @ X.T @ y

    return B


if __name__ == "__main__":
    datapath = "poly.txt"

    # Read the input file, "poly.txt", assuming it has two columns, where each row is of the form [x y]
    file = open(datapath, 'r')
    data = file.readlines()
    x = []
    y = []
    for line in data:
        [i, j] = line.split()
        x.append(float(i))
        y.append(float(j))

    # Problem 1. 
    # Complete 'main, 'feature_matrix', and 'lease_squares' functions. 
    

    # Problem 2. 
    # Write out the resulting estimated functions for each d.
    degrees = [1,2,3,4,5]
    paramFits = main(datapath, degrees)
    # print(paramFits)
    for idx in range(len(degrees)):
        print("y_hat(x_"+str(degrees[idx])+")")
        print(paramFits[idx])
        print("****************")


    # Problem 3. 
    # Visualize the dataset and these fitted models on a single graph
    # Use the 'scatter' and 'plot' functions in the `matplotlib.pyplot` module. 

    # Draw a scatter plot 
    plt.scatter(x, y, color='black', label='data')
    x.sort()
    
    for params in paramFits:
        deg = len(params) - 1
        yVals = [[params[i] * xVal ** (deg - i) for i in range(len(params))] for xVal in x]
        yVals = [sum(i) for i in yVals]
        print(r2_score(y, yVals))
        plt.plot(x, yVals, label=f'd = {deg}')
        continue
        

    plt.xlabel('x', fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.legend(fontsize=10, loc='upper left')
    plt.title("Regressions across data", fontsize=12, )

    plt.show()
    
    print(paramFits)

    
