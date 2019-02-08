import matplotlib as mpl
from random import randint
mpl.use('Agg')
import matplotlib.pyplot as plt
import timeit

def desenhaGrafico(x,y, yl = "Saídas",xl = "Entradas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(yl+'_graph.png')
 
def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def geraListaOrd(tam):
  lista = []
  for i in range(tam):
    lista.append(i)
  return lista

def geraListaInv(tam):
  lista = []
  for i in range(tam):
    lista.append(tam-i)
  return lista

def buble(xb):
  count = 0
  while xb > 1:
    xb = xb-1
    for a in range(xb):
      if (lis[a] > lis[a+1]):
        aux = lis[a]
        lis[a] = lis[a+1]
        lis[a+1] = aux
      count=count+1
  return count

x = [1000, 2000, 4000, 6000]
y = []
z = []
for i in range(len(x)):
  lis = geraLista(x[i])
  y.append(buble(x[i]))
  z.append(timeit.timeit('buble({})'.format(x[i]),setup="from __main__ import buble",number=1))

desenhaGrafico(x,y, "nops_Ale")
desenhaGrafico(x,z, "Tempo_Ale")
y = []
z = []

for i in range(len(x)):
  lis = geraListaOrd(x[i])
  y.append(buble(x[i]))
  z.append(timeit.timeit('buble({})'.format(x[i]),setup="from __main__ import buble",number=1))

desenhaGrafico(x,y, "nops_ord")
desenhaGrafico(x,z, "Tempo_ord")
y = []
z = []

for i in range(len(x)):
  lis = geraListaInv(x[i])
  y.append(buble(x[i]))
  z.append(timeit.timeit('buble({})'.format(x[i]),setup="from __main__ import buble",number=1))

desenhaGrafico(x,y, "nops_inv")
desenhaGrafico(x,z, "Tempo_inv")