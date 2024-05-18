import numpy as np


def calculate(list):
  
  a=list
  if len(a)==9:
    arr1 = np.array([a[0:3],a[3:6],a[6:]])

    #Finding the Mean
    Mean_ax1 = (np.mean(arr1, axis=0)).tolist()
    Mean_ax2 = (np.mean(arr1, axis=1)).tolist()
    Mean_flat = (np.mean(arr1)).tolist()

    #Finding the Variance
    Var_ax1 = (np.var(arr1, axis=0)).tolist()
    Var_ax2 = (np.var(arr1, axis=1)).tolist()
    Var_flat = (np.var(arr1)).tolist()

    #Finding the Standard Deviation
    Std_ax1 = (np.std(arr1, axis=0)).tolist()
    Std_ax2 = (np.std(arr1, axis=1)).tolist()
    Std_flat = (np.std(arr1)).tolist()

    #Finding the Maximum value
    Max_ax1 = (np.max(arr1, axis=0)).tolist()
    Max_ax2 = (np.max(arr1, axis=1)).tolist()
    Max_flat = (np.max(arr1)).tolist()

    #Finding the Minimum value
    Min_ax1 = (np.min(arr1, axis=0)).tolist()
    Min_ax2 = (np.min(arr1, axis=1)).tolist()
    Min_flat = (np.min(arr1)).tolist()

    #Finding the Sum
    Sum_ax1 = (np.sum(arr1, axis=0)).tolist()
    Sum_ax2 = (np.sum(arr1, axis=1)).tolist()
    Sum_flat = (np.sum(arr1)).tolist()

  
    calculations = {'mean':[Mean_ax1, Mean_ax2, Mean_flat], 
                    'variance':[Var_ax1, Var_ax2, Var_flat], 
                    'standard deviation':[Std_ax1, Std_ax2, Std_flat], 
                    'max':[Max_ax1, Max_ax2, Max_flat], 
                    'min':[Min_ax1, Min_ax2, Min_flat], 
                    'sum':[Sum_ax1, Sum_ax2, Sum_flat]
                 }

    

  else:
    raise ValueError('List must contain nine numbers ')

  return calculations



    

  
