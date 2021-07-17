import numpy as np

def valuation(lp, t, c, d, cp, na):

  lps = np.zeros(t+1)
  lps[0] = lp
  v = 0

  for i in range(1, t+1):
    lps[i] = lps[i-1]+lps[i-1]*(c/100)

  for j in range(1, t+1):
    v += lps[j]/(1+d/100)**(j)

  valor = v + (lps[t]*(1+cp/100)/(d/100-cp/100))/(1+d/100)**t
  valor_acao = valor/na

  print(f'Valor da firma: R${valor: .3f}\n')
  print(f'Valor por ação: R${valor_acao: .2f}')