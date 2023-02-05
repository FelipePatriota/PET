import pandas as pd
from scipy import stats

data2022 = pd.read_csv('licitacoes-2022.csv', sep=',',on_bad_lines='skip', low_memory=False)

data2021 = pd.read_csv('licitacoes-2021.csv', sep=',',on_bad_lines='skip', low_memory=False)


sample1 = data2022[data2022['DESCRICAOOBJETO'] == 'GÊNEROS ALIMENTÍCIOS']['VALORESTIMADO'] 
sample2 = data2021[data2021['DESCRICAOOBJETO'] == 'GÊNEROS ALIMENTÍCIOS']['VALORESTIMADO']
sample1 = pd.to_numeric(sample1, errors='coerce')
sample2 = pd.to_numeric(sample2, errors='coerce')

# teste de hipótese para médiana
mediana2022 = sample1.median()
mediana2021 = sample2.median()
# teste de hipótese para média 
media2022 = sample1.mean()
media2021 = sample2.mean()
# valor Minimo 
minimo2021 = sample1.min()
minimo2021 = sample2.min()
# valor Maximo
maximo2021 = sample1.max()
maximo2021 = sample2.max()
# teste de hipótese para variância
variancia2022 = sample1.var()
variancia2021 = sample2.var()
# teste de hipótese para desvio padrão
desvio2022 = sample1.std()
desvio2021 = sample2.std()


# exibir o resultado
print('Valor mediana 2022 %s' % mediana2022)
print('-------------------------')
print("Valor mediana 2021 %s" % mediana2021)
print('-------------------------')
print("Valor média 2022 %s" % media2022)
print('-------------------------')
print("Valor média 2021 %s" % media2021)
print('-------------------------')
print("Valor mínimo 2022 %s" % minimo2022)
print('-------------------------')
print("Valor mínimo 2021 %s" % minimo2021)
print('-------------------------')
print("Valor máximo 2022 %s" % maximo2022)
print('-------------------------')
print("Valor máximo 2021 %s" % maximo2021)
print('-------------------------')
print("Valor variância 2022 %s" % variancia2022)
print('-------------------------')
print("Valor variância 2021 %s" % variancia2021)
print('-------------------------')
print("Valor desvio padrão 2022 %s" % desvio2022)
print('-------------------------')
print("Valor desvio padrão 2021 %s" % desvio2021)


# # Perform t-test
t_stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=False)

# # Print results
print("t-statistic:", t_stat)
print("p-value:", p_value)
# p-value  0.005


# Interpret results
alpha = 0.05
if p_value > alpha:
    print("Fail to reject the null hypothesis")
else:
    print("Reject the null hypothesis")
