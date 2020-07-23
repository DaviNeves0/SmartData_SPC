import pandas as pd
import numpy as np
import datetime
from plotly.offline import iplot
import plotly.graph_objs as go
from plotly.subplots import make_subplots

def highlight_max(s):    
    is_max = s == s.max()
    return ['color: white; background-color: #3749E9' if v else '' for v in is_max]
def highlight_min(s):
    is_max = s == s.min()
    return ['color: white; background-color: #112244' if v else '' for v in is_max]
def destaque(val):
    color = '#F2F200' if val == 'Sim' else ''
    return 'background: {}'.format(color)
def destaque_coluna(val):
    color = '#F2F200' if val == 0 else ''
    return 'background: {}'.format(color)
def validacao (relatorio, pasta, tabela_fnt):
    print ("Analisando tabela de fontes...")
    df = pd.read_excel(tabela_fnt)
    df.DAT_INC_DBO = pd.to_datetime(df.DAT_INC_DBO, format='%Y-%m-%d', errors='coerce')
    dict_tipo = {'ID_STG_FNT_ITT': int, 'NUM_CNPJ': int, 'NUM_CMP_CNPJ': int, 'NOM_COM': str,'NOM_RAZ_SCL': str, 'DAT_INC_DBO': datetime.date}
    dict_analise = {}
    for coluna, tipo in dict_tipo.items():
        dict_analise[coluna] = len([linha for linha in df[coluna]
                                    if (type(linha) == tipo) or (linha == tipo) or (isinstance(linha, tipo))])
    final = [x * 100 / len (df) for x in dict_analise.values()]
    tipo_review = pd.DataFrame({'Porcentagem': final},index=df.columns)
    tipo_review = tipo_review.rename_axis('Colunas', axis='columns')
    data = [go.Bar(y=final,
                   x=df.columns,
                   marker=dict(color='#ad6207')
                  )]
    fig = go.Figure(data=data)
    fig.update_xaxes(showline=True, linewidth=1, linecolor='#717171')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#8686b3')
    fig.update_layout(dict(plot_bgcolor = '#FFFFFF', paper_bgcolor = '#FFFFFF'))
    fig.update_layout(yaxis=dict(ticksuffix = '%'))
    fig.write_html(pasta + "/fonte_dado.html")
    dado_sensivel = ['Encontrado', 'Não Encontrado', 'Não Encontrado', 'Encontrado', 'Encontrado', 'Não Encontrado']
    sensibilidade_review = pd.DataFrame({'Dado Confidencial': dado_sensivel},index=df.columns)
    sensibilidade_review = sensibilidade_review.rename_axis('Colunas', axis='columns')
    visualiza = (sensibilidade_review.style.applymap(destaque))
    write_to_html_file(visualiza, title='', filename=pasta + "/fonte_confidencial.html")
    visualiza
    unico = [len(np.unique(df.ID_STG_FNT_ITT)) * 100 / len (df)]
    ff = df[['NUM_CNPJ', 'NUM_CNPJ', 'NUM_CMP_CNPJ', 'NOM_COM', 'DAT_INC_DBO']]
    for x in ff.columns:
        coluna = df
        coluna = coluna.replace(0,np.nan)
        soma = coluna.groupby(f'{x}').count()
        soma = soma[soma.ID_STG_FNT_ITT == 1]
        soma = soma.ID_STG_FNT_ITT.sum()
        unico.append (soma * 100 / len (coluna[x]))
    unico_review = pd.DataFrame({'Campos Íntegros': unico},index=df.columns)
    unico_review = unico_review.rename_axis('Colunas', axis='columns')
    data = go.Bar(x = unico, 
                  y = df.columns, 
                  orientation = 'h', 
                  marker = {'color' : '#3FBA89'})
    layout = go.Layout(title = '', 
                       yaxis = {'title': ''}, 
                       xaxis = {'title': ''})
    fig = go.Figure(data = data, layout = layout)
    fig.update_yaxes(showline = True, linewidth = 1, linecolor = '#717171')
    fig.update_xaxes(showgrid = True, gridwidth = 1, gridcolor = '#D9D9DE')
    fig.update_layout({'plot_bgcolor': '#FFFFFF', 'paper_bgcolor': '#FFFFFF'})
    fig.update_layout(xaxis=dict(ticksuffix = '%'))
    fig.write_html(pasta + "/fonte_unicos.html")
    df = df.fillna(0)
    df.ID_STG_FNT_ITT = df.ID_STG_FNT_ITT.astype(np.int64)
    df.NUM_CNPJ = df.NUM_CNPJ.astype(np.int64)
    df.NUM_CMP_CNPJ = df.NUM_CMP_CNPJ.astype(np.int64)
    df.NOM_COM = df.NOM_COM.astype (str)
    df.NOM_RAZ_SCL = df.NOM_RAZ_SCL.astype (str)
    coluna_id = len([x for x in df.ID_STG_FNT_ITT if x != 0]) * 100 / len (df.ID_STG_FNT_ITT)
    coluna_num_cnpj = len([x for x in df.NUM_CNPJ if x != 0]) * 100 / len (df.NUM_CNPJ)
    coluna_num_comp = len([x for x in df.NUM_CMP_CNPJ if x != 0]) * 100 / len (df.NUM_CMP_CNPJ)
    coluna_nome_com = len([x for x in df.NOM_COM if x != 0]) * 100 / len (df.NOM_COM)
    coluna_nome_raz = len([x for x in df.NOM_RAZ_SCL if x != 0]) * 100 / len (df.NOM_RAZ_SCL)
    coluna_data_inc = len([x for x in df.DAT_INC_DBO if x != 0]) * 100 / len (df.DAT_INC_DBO)
    campos_validos = [coluna_id, coluna_num_cnpj, coluna_num_comp, coluna_nome_com, coluna_nome_raz, coluna_data_inc]
    preenchimento_labels = ['Fonte', 'CNPJ', 'Complemento do CNPJ', 'Complemento', 'Nome/Razão Social', 'Data de inclusão']
    tabela_review = pd.DataFrame({'Campos que estão válidos': campos_validos},index=preenchimento_labels)
    tabela_review = tabela_review.rename_axis('Colunas', axis='columns')
    data = go.Bar(x = campos_validos, 
                  y = preenchimento_labels, 
                  orientation = 'h', 
                  marker = {'color' : '#860ccc'})
    layout = go.Layout(title = '', 
                       yaxis = {'title': ''}, 
                       xaxis = {'title': ''})
    fig = go.Figure(data = data, layout = layout)
    fig.update_yaxes(showline = True, linewidth = 1, linecolor = '#717171')
    fig.update_xaxes(showgrid = True, gridwidth = 1, gridcolor = '#D9D9DE')
    fig.update_layout({'plot_bgcolor': '#FFFFFF', 'paper_bgcolor': '#FFFFFF'})
    fig.update_layout(xaxis=dict(ticksuffix = '%'))
    fig.write_html(pasta + "/fonte_integridade.html")
    datas_inc = df[df['DAT_INC_DBO'] != 0]
    datas_inc = datas_inc.groupby('DAT_INC_DBO').count()
    datas_inc
    conta = 0
    porcentagem = []
    for x in datas_inc.ID_STG_FNT_ITT:
        conta = x * 100 / len(df)
        porcentagem.append (conta)
    datas_encontradas = pd.DataFrame({'Taxa': porcentagem},index=datas_inc.index)
    datas_encontradas = datas_encontradas.rename_axis('As seguintes datas foram encontradas:', axis='columns')
    datas_encontradas.index.name = None
    visualiza = (datas_encontradas.style.format({'Taxa':"{:.2f}%"}).applymap(destaque_coluna, subset=pd.IndexSlice[:, ['Taxa']]))
    write_to_html_file(visualiza, title='', filename=pasta + "/fonte_datas.html")
    visualiza
    nome_identico = df.groupby('NOM_RAZ_SCL').count().sort_values(by = 'NUM_CNPJ', ascending = False)
    nome_identico = nome_identico[nome_identico['ID_STG_FNT_ITT'] > 1]
    cnpj_nome_identico = [df.NUM_CNPJ[x] for x in range (len (df)) if df.NOM_RAZ_SCL[x] in nome_identico.index]
    cnpj_c_nome_identico = [df.NUM_CMP_CNPJ[x] for x in range (len (df)) if df.NOM_RAZ_SCL[x] in nome_identico.index]
    cnpj_nome_unico = [df.NUM_CNPJ[x] for x in range (len (df)) if df.NOM_RAZ_SCL[x] not in nome_identico.index]
    cnpj_c_nome_unico = [df.NUM_CMP_CNPJ[x] for x in range (len (df)) if df.NOM_RAZ_SCL[x] not in nome_identico.index]
    cnpjList_nome_unico = [str(cnpj_nome_unico[c]) + str(cnpj_c_nome_unico[c]) for c in range (len(cnpj_nome_unico))]
    cnpj_valido_nome_unico = [cnpjList_nome_unico[c] for c in range (len(cnpjList_nome_unico)) if len(cnpjList_nome_unico[c]) == 14]
    cnpj_nao_valido = [cnpjList_nome_unico[c] for c in range (len(cnpjList_nome_unico)) if len(cnpjList_nome_unico[c]) != 14]
    cnpj_mais = [cnpjList_nome_unico[c] for c in range (len(cnpjList_nome_unico)) if len(cnpjList_nome_unico[c]) > 14]
    cnpj_menos = [cnpjList_nome_unico[c] for c in range (len(cnpjList_nome_unico)) if len(cnpjList_nome_unico[c]) < 14]
    cnpjList_nome_identico = [str(cnpj_nome_identico[c]) + str(cnpj_c_nome_identico[c]) for c in range (len(cnpj_nome_identico))]
    cnpj_valido_nome_identico = [cnpjList_nome_identico[c] for c in range (len(cnpjList_nome_identico)) if len(cnpjList_nome_identico[c]) == 14]
    cnpj_nao_valido.extend([(cnpjList_nome_identico[c]) for c in range (len(cnpjList_nome_identico)) if len(cnpjList_nome_identico[c]) != 14])
    cnpj_mais.extend([(cnpjList_nome_identico[c]) for c in range (len(cnpjList_nome_identico)) if len(cnpjList_nome_identico[c]) > 14])
    cnpj_menos.extend([(cnpjList_nome_identico[c]) for c in range (len(cnpjList_nome_identico)) if len(cnpjList_nome_identico[c]) < 14])
    cnpjs_unicos = len(np.unique(cnpj_valido_nome_unico)) + len(np.unique(cnpj_valido_nome_identico))
    cnpjs_identicos = len(cnpj_valido_nome_unico) + len(cnpj_valido_nome_identico) - cnpjs_unicos
    valores_unicos = cnpjs_unicos*100/(len(cnpj_valido_nome_unico) + len(cnpj_valido_nome_identico))
    valores_identicos = 100 - valores_unicos
    labels = ['CNPJs Únicos', 'CNPJs Iguais']
    colors = ['#37e94f', '#0003ad']
    sizes = [valores_unicos, valores_identicos]
    explode = (0, 0.05)
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes)])
    fig.update_traces(marker=dict(colors=colors, line=dict(color='#000000', width=0)))
    fig.update_traces(texttemplate='%{percent:.2%f}')
    fig.write_html(pasta + "/fonte_cnpjs_unicos.html")
    cnpjs_unicos = len(np.unique(cnpj_valido_nome_unico))
    cnpjs_identicos = len(cnpj_valido_nome_unico) - cnpjs_unicos
    conta = cnpjs_unicos
    valores_validos_unicos = (conta*100) / len(df)
    conta = len(cnpj_valido_nome_identico) + cnpjs_identicos
    valores_validos_identicos = (conta*100) / len(df)
    conta = len(cnpj_nao_valido)
    valores_nao_validos = (conta*100) / len(df)
    labels = 'Válidos', 'Invalidados', 'Não válidos'
    colors = ['#66ff66', '#e6e600', '#ff0000']
    sizes = [valores_validos_unicos, valores_validos_identicos, valores_nao_validos]
    explode = (0, 0.05, 0.05)
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes)])
    fig.update_traces(marker=dict(colors=colors, line=dict(color='#000000', width=0)))
    fig.update_traces(texttemplate='%{percent:.2%f}')
    fig.write_html(pasta + "/fonte_cnpjs_validados.html")
    exat_14_char = valores_validos_unicos + valores_validos_identicos
    conta = len(cnpj_mais)
    mais_14_char = (conta*100) / len (df)
    conta = len(cnpj_menos)
    menos_14_char = (conta*100) / len (df)
    labels = '+14 Caracteres', '-14 Caracteres', '14 Caracteres (Correto)'
    colors = ['#e6e600', '#ff0000', '#66ff66']
    sizes = [mais_14_char, menos_14_char, exat_14_char]
    explode = (0.03, 0.03, 0.03)
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes)])
    fig.update_traces(marker=dict(colors=colors, line=dict(color='#000000', width=0)))
    fig.update_traces(texttemplate='%{percent:.2%f}')
    fig.write_html(pasta + "/fonte_cnpj_numeros.html")
    nome_identico = nome_identico.ID_STG_FNT_ITT.sum()*100/len(df)
    nome_unico = 100 - nome_identico
    labels = ['Nomes Únicos', 'Nomes Idênticos']
    colors = ['#66ff66', '#ff0000']
    sizes = [nome_unico, nome_identico]
    explode = (0, 0.05)
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes)])
    fig.update_traces(marker=dict(colors=colors, line=dict(color='#000000', width=0)))
    fig.update_traces(texttemplate='%{percent:.2%f}')
    fig.write_html(pasta + "/fonte_nomes.html")
    media_preenchimento = sum (campos_validos) / df.shape[1]
    media_validacao = valores_validos_unicos
    print(f"Tabela de Fontes analisada com sucesso e validada.!")
