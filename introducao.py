import streamlit as st


def introducao(selecao, menu):
    if selecao == menu[0]:
        st.markdown('''<h1 style='text-align: center;
                    color: teal;
                    '>Apresentação </h2>''',
                    unsafe_allow_html=True)

        st.markdown('''<div style='text-align: justify;
                    '>Este aplicativo foi desenvolvido pela mestranda <b>Flavya
                    Fernanda França Vilela </b> e pelo professor e orientador
                    <b>Dr. Márcio Ricardo Salla</b>, ambos do Programa de
                    Pós-Graduação em Qualidade Ambiental (PPGMQ),
                    da Universidade Federal de
                    Uberlândia - UFU.  </div>''',
                    unsafe_allow_html=True)
        st.write('')
        st.markdown('''<div style='text-align: justify;
                    '>Este programa é gratuito e tem o intuito de contribuir.
                    Os autores não se responsabilizam por eventuais erros no
                    programa, mas é gratos se forem comunicado de
                    algum.</div>''',
                    unsafe_allow_html=True)
        st.write('')
        st.markdown('''Contatos: flavya2310@gmail.com | marcio.salla@ufu.br
                    ''')

        st.divider()

        st.markdown('<h6 style="text-align: right;">Apoio:</h6>',
                    unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("   ")
            st.image("https://comunica.ufu.br/sites/default/files/imagem/2023-08/anexo_45_anos_ufu-01%5B1%5D.png",
                     width=220)
        with col3:
            st.image("http://www.fapemig.br/media/arquivos/nova_logo_eps.jpg",
                     width=120)
        with col4:
            st.image("http://www.ppgmq.iciag.ufu.br/sites/ppgmq.iciag.ufu.br/files/imagens/logo-ppgmq.png",
                     width=180)
        st.divider()
