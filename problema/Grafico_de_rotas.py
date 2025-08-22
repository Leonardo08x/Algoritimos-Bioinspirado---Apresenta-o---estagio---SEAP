import plotly.graph_objects as go
def rotas_converter(rotas,coords):
    cidades_rota = [c for c in rotas] 
    coordsx = [(coords[c][0], coords[c][1],c) for c in range(len(coords))]
    coord_rota = []
    for i in cidades_rota:
        for j in coordsx:
            if i == j[2]:
                coord_rota.append((i, j[0], j[1]))
    return coord_rota
def grafico_de_rotas(rotas_geral, rotas_ga, rotas_aco, rotas_gwo):
    #pontos
    city_points = go.Scatter(x=[c[0] for c in rotas_geral], y=[c[1] for c in rotas_geral], mode='markers+text', name='Cidades',
    text=[f"Cidade {i}" for i in range(len(rotas_geral))],
    textposition='top center',)

    #rotas
    rota_aco = go.Scatter(x=[c[1] for c in rotas_aco], y=[c[2] for c in rotas_aco], mode='lines',
    line=dict(color='red', width=2),
    name=f'Tour-aco:{[c[0] for c in rotas_aco]}')
    rota_ga = go.Scatter(x=[c[1] for c in rotas_ga], y=[c[2] for c in rotas_ga], mode='lines',
    line=dict(color='green', width=2),
    name=f'Tour-ga:{[c[0] for c in rotas_ga]}')
    rota_gwo = go.Scatter(x=[c[1] for c in rotas_gwo], y=[c[2] for c in rotas_gwo], mode='lines',
    line=dict(color='blue', width=2),
    name=f'Tour-gwo:{[c[0] for c in rotas_gwo]}')

    # Criar figura e adicionar traces
    fig = go.Figure()
    fig.add_trace(city_points)
    fig.add_trace(rota_aco)
    fig.add_trace(rota_ga)
    fig.add_trace(rota_gwo)
  
    fig.update_layout(
        title="TSP: Comparativo de Rotas (ACO, GA, GWO)",
        xaxis_title="Coordenada X",
        yaxis_title="Coordenada Y",
        legend_title="Legenda",
        hovermode="closest"
    )
    return fig.show()