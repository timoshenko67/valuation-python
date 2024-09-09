# Valuation com Python

Valuation é uma forma de se estimar o valor de uma empresa. Existem muitos métodos para se fazer essa estimativa, porém, o mais utilizado é o Fluxo de Caixa Descontado, também conhecido como DCF (Discounted Cash Flow).

A equação utilizada neste método é a que segue:
$$
Valor = (\sum_{t = 1}^n \frac{FCCF_t}{(1+d)^t}) + \frac{Valor\ terminal}{(1+d)^n}
$$
Onde 
$$
Valor\ terminal = \frac{FCFF_n(1+g)}{(d-g)}
$$

    FCFF = Fluxo de Caixa Futuro da Firma
    n = número de anos futuros
    d = taxa de Desconto
    g = Taxa de Crescimento na Perpetuidade 

Warren Buffett utiliza o Lucro do Proprietário para fazer seus valuations. Seu cálculo é feito da seguinte maneira:
$$
Lucro\ do\ Proprietário(LP) = Lucro\ Líquido + Depreciação\ e\ Amortização +exaustão - CAPEX
$$
Caso você prefira utilizar o LP, assim como Buffett, basta substituir o FCFF na equação.

Aqui você encontrará um arquivo em Python com uma função que calcula o valor de uma empresa, a partir de premissas determinas pelo usuário. Se atente ao determinar essas premissas, pois, caso elas estejam muito além da realidade, o cálculo do valor intrínseco da empresa será prejudicado.

> É melhor estar aproximadamente certo do que precisamente errado.
