# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]
data = pd.read_csv(path, sep=',')

#Code starts here
data_sample = data.sample(n=sample_size, random_state = 0)

sample_mean = data_sample['installment'].mean()

sample_std = data_sample['installment'].std()

margin_of_error = z_critical * (sample_std / math.sqrt(sample_size))

confidence_interval = [round(sample_mean - margin_of_error, 2),round(sample_mean + margin_of_error, 2)]

true_mean = data['installment'].mean()

print(true_mean)
print(confidence_interval)






# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig, axes = plt.subplots(3,1) 

for i in range(0, len(sample_size)):
    m =[]
    for j in range(0, 1000):
        m.append(data['installment'].sample(n= sample_size[i]).mean())
    mean_series = pd.Series(m)
    mean_series.hist(ax = axes[i])


# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
lis = data['int.rate'].tolist()
ll = [float(l[:-1])/100 for l in lis] 


data['int.rate'] = pd.Series(ll)

z_statistic, p_value = ztest(data[data['purpose']=='small_business']['int.rate'], value = data['int.rate'].mean(), alternative = 'larger')

z_statistic = round(z_statistic,2)
#print(z_statistic)
#print(p_value)


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here

z_statistic, p_value = ztest(data[data['paid.back.loan']=='No']['installment'], data[data['paid.back.loan']=='Yes']['installment'] )

z_statistic = round(z_statistic,2)


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here

yes = data[data['paid.back.loan'] == 'Yes']['purpose'].value_counts()

no = data[data['paid.back.loan'] == 'No']['purpose'].value_counts()
#print(yes)
#print(yes.transpose())
observed = pd.concat([yes.transpose(), no.transpose()], axis = 1, keys = ['Yes', 'No'])

chi2, p, dof, ex = chi2_contingency(observed)

print(critical_value)
print(chi2)
print(p)
print(dof)
print(ex)


