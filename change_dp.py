# Uses python3
import sys
import math
import numpy as np

def get_change(m):
    #write your code here
    coins = np.array([1,3,4])
    mini_coins = [0]
    mini_coins.extend(math.inf*np.ones(m))
    for i in range(1, m+1):
        indx = np.where(coins<=i)[0]
        for j in indx:
            temp = mini_coins[i-coins[j]] + 1
            if temp < mini_coins[i]:
                mini_coins[i] = temp
    return mini_coins[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    
    print(get_change(m))
