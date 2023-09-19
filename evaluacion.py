import pandas as pd
import matplotlib.pyplot as plt

# Se solicita que diseñe e implemente un sencillo sistema, basado en POO, mediante el cual pueda
# leer el archivo, crear listas de reproducción compuestas por canciones y calcular la duración de
# dichas listas creadas.

data = pd.read_csv('Spotify2010-2021Top100.csv')

class Cancion:
    def __init__(self, title, artist, top_genre, year_released, dur):
        self.title = title
        self.artist = artist
        self.top_genre = top_genre
        self.year_released = year_released
        self.dur = dur


class Playlist:
    def __init__(self, nombre, campo=None, valor=None):
        if campo is None or valor is None:
            lista = data
        else:
            lista = data[data[campo] == valor]
        self.canciones = lista
        self.nombre = nombre

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion, ignore_index=True)

    def calcular_duracion(self):
        duracion = self.canciones['dur'].sum()
        horas, segundos = divmod(duracion, 3600)
        minutos, segundos = divmod(segundos, 60)
        return horas, minutos, segundos

    def ordenar_por_titulo(self):
        lista = self.canciones.sort_values(by='title')
        return lista

    def ordenar_por_artista(self):
        lista = self.canciones.sort_values(by='artist')
        return lista

    def cantidad_de_canciones(self):
        cantidad = self.canciones.shape[0]
        return cantidad


playlist = Playlist('Indie', 'top genre', 'indie rock')
print(playlist.canciones)

horas, minutos, segundos = playlist.calcular_duracion()

print(f'La playlist dura {horas}:{minutos}:{segundos}')

# 1- Implementar el código necesario para poder mostrar la lista de reproducción
# ordenada por título de las canciones.

lista_ordenada_por_titulo = playlist.ordenar_por_titulo()

print('Lista ordenada por título:')
print(lista_ordenada_por_titulo)

# 2-Implementar el código necesario para poder mostrar la lista de reproducción ordenada por artistas.

lista_ordenada_por_artista = playlist.ordenar_por_artista()

print('Lista ordenada por artista:')
print(lista_ordenada_por_artista)

# Mostrar la cantidad de canciones de las listas de reproducción creadas.

cantidad = playlist.cantidad_de_canciones()

print(f'La playlist {playlist.nombre} tiene {cantidad} canciones')

# 4- ¿Permite el diseño implementar una lista de reproducción basada en
# un artista en lugar de un género musical?

playlist_nueva = Playlist('Aloe Blacc', 'artist', 'Aloe Blacc')

print(playlist_nueva.canciones)

# 5- ¿Permite el diseño implementar listas de reproducción genéricas?

playlist_generica = Playlist('generica')

print(playlist_generica.canciones)


# ACTIVIDAD 2

# 1.	¿Cuántas canciones responden al género “hip hop”?

playlist_hiphop = Playlist('HipHop', 'top genre', 'hip hop')
cantidad_hiphop = playlist_hiphop.cantidad_de_canciones()
print(cantidad_hiphop)

# 2.	¿Cuál es el género que más aparece en el archivo?

genero_mas_comun = playlist_generica.canciones['top genre'].mode()[0]
print(genero_mas_comun)

#3.	¿Cuál es la canción que tiene mayor duración? ¿Y la canción de menor duración?
dur_max = playlist_generica.canciones['dur'].max()
cancion_max = playlist_generica.canciones[playlist_generica.canciones['dur'] == dur_max]['title']
print(cancion_max)

dur_min = playlist_generica.canciones['dur'].min()
cancion_min = playlist_generica.canciones[playlist_generica.canciones['dur'] == dur_min]['title']
print(cancion_min)

# 4.	¿Cuál es el artista que más aparece en el archivo?
artista_mas_comun = playlist_generica.canciones['artist'].mode()[0]
print(artista_mas_comun)

#5.	¿Cuántas canciones son interpretadas por “Imagine Dragons”?
playlist_imdr = Playlist('imdr','artist','Imagine Dragons')
cantidad_imdr = playlist_imdr.cantidad_de_canciones()
print(cantidad_imdr)

#6.	¿Cuál es el año cuyas canciones tienen la mayor sumatoria de duración? Indicar el valor.
playlist_x_year = playlist_generica.canciones.groupby('year released')['dur'].sum()
year_max = playlist_x_year.idxmax()
print(year_max)

#7.	¿Cuál es el año cuyas canciones tienen la menor sumatoria de duración? Indicar el valor.
year_min = playlist_x_year.min()
horas1, segundos1 = divmod(year_min, 3600)
minutos1, segundos1 = divmod(segundos1, 60)
print(f'La playlist dura {horas1}:{minutos1}:{segundos1}')
#8.	¿Cuál es el género cuyas canciones tienen la mayor sumatoria de duración? Indicar el valor.
playlist_x_genero = playlist_generica.canciones.groupby('top genre')['dur'].sum()
gen_max = playlist_x_genero.idxmax()
print(gen_max)

#9.	¿Cuál es el género cuyas canciones tienen la menor sumatoria de duración? Indicar el valor.
gen_min = playlist_x_genero.idxmin()
print(gen_min)

#10.	¿Cuál es el promedio de duración de las canciones del género con mayor sumatoria de duración de sus canciones?
playlist_prom_max = Playlist('prommax', 'top genre', gen_max)
prom_max = playlist_prom_max.canciones['dur'].mean()
print(prom_max)

#11.	¿Cuál es el año cuyo promedio de duración de canciones es el menor?
playlist_x_year_prom = playlist_generica.canciones.groupby('year released')['dur'].mean()
year_prom_min = playlist_x_year.idxmin()
print(year_prom_min)

#12.	Informar el porcentaje de canciones de cada género que aparecen en la lista.
playlist_x_gen = playlist_generica.canciones['top genre'].value_counts()
porc_x_gen = (playlist_x_gen / len(playlist_generica.canciones['top genre']))*100
print(porc_x_gen)

#13.	Informar los 5 géneros que tienen los mayores porcentajes de aparición en el archivo.
porc_ordenado = porc_x_gen.sort_values(ascending=False)
print(porc_ordenado.head())

#14.	Informar cuáles son todos los géneros en cuyo nombre aparece la palabra “rock” en la lista.
lista_rock = playlist_generica.canciones[playlist_generica.canciones['top genre'].str.contains('rock')]
rock = lista_rock.groupby('top genre')['top genre'].count()
print(rock)

#15.	El archivo contiene registros duplicados (hay temas que aparecen más de una vez). Determine, cuente y muestre los duplicados.
duplicados = playlist_generica.canciones[playlist_generica.canciones.duplicated()]
print(duplicados)
print(duplicados.count())

#ACTIVIDAD 3

#1.	Evolución de la cantidad de canciones del género “dance pop” para cada año.
pl_dancepop = Playlist('dancepop','top genre','dance pop')
pl_dancepop = pl_dancepop.canciones.groupby('year released').count()

plt.plot(pl_dancepop,'-r*')
plt.title("Evolucion dance pop")
plt.xlabel("Año")
plt.ylabel("Cantidad")
plt.show()

#2.	Gráfico de torta representando los porcentajes que ocupan las canciones de los
# géneros informados en el punto 13 de la actividad 2. Tener en cuenta que es necesario recalcular los
# porcentajes teniendo en cuenta sólo las categorías consideradas.
suma = porc_ordenado.head().sum()
porcentaje = (porc_ordenado.head() / suma)*100
fig2, axs = plt.subplots()
plt.title("Porcentaje de géneros")
porcentaje.plot(kind="pie", autopct='%.2f%%', ax=axs)
plt.show()

#3. Gráfico de barras indicando la cantidad de temas de cada género en cuyo nombre aparece la palabra “rock” en la lista.
fig3, ax = plt.subplots()
ax.barh(rock.index, rock.values, color='coral')
ax.set_title("Cantidad de temas de cada género que incluye la palabra 'Rock'")
ax.set_xlabel("Cantidad")
ax.set_ylabel("Genero")
plt.tight_layout()
plt.show()

