from problema.Grafico_de_rotas import rotas_converter
import matplotlib.pyplot as plt
import os
import imageio
def static_graph(len_distancia,lista_cidades, gen, coords):
    print(f"Geração: {gen} - Distância: {len_distancia}, Cidades: {lista_cidades}")
    rotas = rotas_converter(lista_cidades,coords)
    cidadesx, cidadesy = [c[0] for c in coords], [c[1] for c in coords]
    plt.figure(figsize=(12, 6)) 
    plt.clf()
    plt.scatter(cidadesx, cidadesy, color='blue')
    for i, (x, y) in enumerate(coords):
        plt.text(x, y, f'Cidade - {i} ', fontsize=9, ha='right')
    rotax, rotay = [rotas[i][1] for i in range(len(rotas))], [rotas[i][2] for i in range(len(rotas))]
    plt.plot(rotax, rotay, color='red', linestyle='-', linewidth=0.5, marker='o', markersize=5)
    plt.title(f'AG - Geração: {gen} - Distância: {len_distancia}')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.pause(0.1)
    plt.savefig(rf'banco_de_imagens/geracao_{gen}.png')
def del_pngs():
    folder = 'banco_de_imagens'
    for filename in os.listdir(folder):
        if filename.endswith('.png'):
            file_path = os.path.join(folder, filename)
            os.remove(file_path)
    print("Todos os arquivos .png foram deletados.")

def gif_maker():
    images = []
    folder = 'banco_de_imagens'
    file_names = sorted((fn for fn in os.listdir(folder) if fn.endswith('.png')),
                        key=lambda x: int(x.split('_')[1].split('.')[0]))
    for filename in file_names:
        file_path = os.path.join(folder, filename)
        images.append(imageio.imread(file_path))
    gif_path = os.path.join(folder, 'evolucao_ag.gif')
    imageio.mimsave(gif_path, images, fps=0.4)
    print(f"GIF salvo em: {gif_path}")
    del_pngs()