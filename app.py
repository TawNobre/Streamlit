import streamlit as st

st.title('Minha Página')
st.header('Primeira Página')
st.subheader('Este é um subheader')
st.text('Aqui serve para adicionar texto')
st.markdown('_______')
st.markdown('> Aqui para citação')
st.markdown('**Negrito** e *Itálico*')
st.caption('Aqui tem uma legenda')
st.latex('x=(283+14)/(10^2)')

json = {
    'Nome': 'João',
    'Idade': '80'
}

st.json(json)
codigo = '''
def funcao():
    return false
'''

st.code(codigo, language='python')