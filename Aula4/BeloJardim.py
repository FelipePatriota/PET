import pandas as pd
from scipy import stats

# Read data from CSV file
data2022 = pd.read_csv('licitacoes-2022.csv', sep=',',
                       on_bad_lines='skip', low_memory=False)

data2021 = pd.read_csv('licitacoes-2021.csv', sep=',',
                       on_bad_lines='skip', low_memory=False)

print(data2021)
print(data2022)

data2022.dropna(subset=['VALORESTIMADO'], inplace=True)
data2021.dropna(subset=['VALORESTIMADO'], inplace=True)

media2022 = data2022['VALORESTIMADO'].mean()
media2021 = data2021['VALORESTIMADO'].mean()

print(media2022)
print(media2021)

t_stat, p_value = stats.ttest_ind(
    data2022['VALORESTIMADO'], data2021['VALORESTIMADO'], equal_var=False)

# # Print results
print("t-statistic:", t_stat)
print("p-value:", p_value)
# p-value de 0.05