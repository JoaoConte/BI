import matplotlib.pyplot as plt
import numpy as np

votos = np.array([842.201, 488.775, 553.424, 424.307, 272.500, 381.512, 261.386])
candi = ['Candidato A', 'Candidato B', 'Candidato C', 'Candidato D', 'Candidato E',
         'Candidato F', 'Candidato G']

cores=['gold', 'red', 'blue', 'magenta', 'green','lightskyblue', 'yellowgreen']
# o atributo explode indica que fatia do gráfico será destacada. No exemplo abaixo, será a primeira fatia. A quantidade de valores é igual ao número de fatias do gráfico. 
explode = (0.1, 0, 0, 0, 0, 0, 0)  # explode 1st slice

# Atribuindo um título ao gráfico
plt.title('Eleição 2020 - Total de Votos')

plt.pie(votos, explode=explode, labels=candi, colors=cores, autopct='%1.1f%%', shadow=True, startangle=90)

#Adiciona Legenda
plt.legend(candi, bbox_to_anchor=(1.3, 1.3),loc='upper right')

#Centraliza o gráfico
plt.axis('equal')

#Ajusta o espaçamento para evitar o recorte do rótulo
plt.tight_layout()

plt.show()
