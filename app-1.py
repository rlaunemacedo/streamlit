#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 20:27:27 2022

@author: laune
"""

import pandas as pd
import streamlit as st
import plotly.express as px

# Definindo um Data Frame
df = pd.read_csv('covid-variants.csv')

paises = list(df['location'].unique())
variantes = list(df['variant'].unique())

# Tratando os dados da coluna date como um datatime
df['date'] = pd.to_datetime(df['date'],format='%Y-%m-%d')

# Seletores
pais = st.sidebar.selectbox('Escolha o país',['Todos']+paises)
variante = st.sidebar.selectbox('Escolha a variante',['Todas']+variantes)

# Filtra os dados se apenas um pais conforme selecionado
if(pais != 'Todos'):
    st.header('País: '+pais)
    df = df[df['location'] == pais]
else:
    st.header('Mostrando o resultado de todos os países')

# ... além disso, filtra a variante caso seja selecionada uma

if(variante != 'Todas'):
    st.subheader('Mostrando o resultado para a variante: '+variante)
    df = df[df['variant'] == variante]
else:
    st.subheader('Mostrando o resultado de todas as variantes')

dfshow = df.groupby(by = ['date']).sum()

fig = px.line(dfshow,x=dfshow.index,y=dfshow.num_sequences,line_shape="spline")
fig.update_layout(title='Casos diários de covid-19' )
st.plotly_chart(fig,use_container_width=True)
