# All decimal 3 places
import math

# Function to compute mean
def mean(first_list):
    # mean Logic
    sum=summation(first_list) 
    if sum==0:return 0
    else :
        return round(sum/len(first_list),3)


# Function to compute median. You cant use Python functions
def median(first_list):
    if len(first_list)==0:return 0
    else :
        arr=sorting(first_list)
        if arr==0:return 0
        else :
            if(len(arr)%2==1):return round(arr[len(arr)//2],3)
            else :
                n=len(arr)
                ans=(arr[n//2]+arr[(n-1)//2])/2
                return round(ans,3)


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    if len(first_list)==0:return 0

    for i in first_list:
        if not isinstance(i,(int,float)):
            return 0
    else:
        mean_of_list=mean(first_list)
        sum_of_sqaure=0
        for i in first_list:
            sum_of_sqaure+=((i-mean_of_list)**2)
        return round(math.sqrt(sum_of_sqaure/len(first_list)),3)


# Function to compute variance. You cant use Python functions
def variance(first_list):
    if len(first_list)==0:return 0

    for i in first_list:
        if not isinstance(i,(int,float)):
            return 0
    else:
        mean_of_list=mean(first_list)
        sum_of_sqaure=0
        for i in first_list:
            sum_of_sqaure+=((i-mean_of_list)**2)
        return round(sum_of_sqaure/len(first_list),3)


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    if(len(first_list) != len(second_list)):return 0
    elif len(first_list)==0:return 0
    else :
        sum=0
        for x,y in zip(first_list,second_list):
            if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
                return 0
            sum+=(x-y)**2

        return round(math.sqrt(sum/len(first_list)),3)


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    if(len(first_list) != len(second_list)):return 0
    elif len(first_list)==0:return 0
    else :
        sum=0
        for x,y in zip(first_list,second_list):
            if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
                return 0
            sum+=(x-y)**2

        return round((sum/len(first_list)),3)


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    if(len(first_list) != len(second_list)):return 0
    elif len(first_list)==0:return 0
    else :
        sum=0
        for x,y in zip(first_list,second_list):
            if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
                return 0
            sum+=abs(x-y)

        return round(sum/len(first_list),3)


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):

    if(len(first_list) != len(second_list)):return 0
    elif len(first_list)==0:return 0
    else :
        sum_upper=0
        sum_lower=0
        mean_x=mean(first_list)
        for x,y in zip(first_list,second_list):
            if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
                return 0
            sum_upper+=(x-y)**2
            sum_lower+=(x-mean_x)**2

        try :
            return round(1-(sum_upper/sum_lower),3)
        except:
            return 0


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    if len(first_list)==0:return 0

    for i in first_list:
        if not isinstance(i,(int,float)):
            return 0
    else :
        mean_x=mean(first_list)
        sd=standard_deviation(first_list)
        ans=0
        try :
            for i in first_list:
                ans+=((i-mean_x)/sd)**3
            return round(ans/len(first_list),3)
        except:
            return 0
    
def sorting(first_list):
    for i in first_list:
        if not isinstance(i,(int,float)):
            return 0
    else:
        arr=first_list.copy()
        n = len(arr) 
        for i in range(n): 
            swapped = False
            for j in range(0, n-i-1): 
                if arr[j] > arr[j+1] : 
                    arr[j], arr[j+1] = arr[j+1], arr[j] 
                    swapped = True
            if swapped == False: 
                break
        return arr


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    for i in first_list:
        if not isinstance(i,(int,float)):
            return 0
    else:
        summation_value=0
        for i in first_list:
            summation_value+=i
    return summation_value
