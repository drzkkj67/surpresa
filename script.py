import streamlit as st
from PIL import Image
import os
from datetime import datetime
import random

# Configuração da página (Título e Layout)
st.set_page_config(page_title="Nosso Espaço Amoroso ❤️", page_icon="💝", layout="centered")

# --- ESTILO SUPER ENFEITADO E PERSONALIZADO (TUDO BRANCO + DETALHES EM ROSA/PRETO) ---
st.markdown("""
    <style>
    /* Força o fundo de todas as áreas a ficar 100% branco */
    .stApp, .main, .stTabs, [data-baseweb="tab-list"], .stTab { 
        background-color: #ffffff !important; 
    }

    /* Fontes e Títulos Principais */
    h1 { color: #e91e63; text-align: center; font-family: 'Helvetica', sans-serif; font-weight: bold; margin-bottom: 5px; }
    h2 { color: #e91e63; font-family: 'Helvetica', sans-serif; text-align: center; }

    /* Títulos das seções internas em PRETO */
    h3, h4 { color: #000000 !important; font-family: 'Helvetica', sans-serif; text-align: center; font-weight: bold; }

    /* Texto padrão do site */
    p { color: #4a4a4a; font-size: 18px; text-align: center; }

    /* Design das Abas */
    .stTabs [data-baseweb="tab"] { 
        font-size: 18px; 
        font-weight: bold; 
        color: #c2185b !important;
        padding: 10px 20px;
    }

    /* Fotos com cantos arredondados */
    img {
        border-radius: 16px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
    }

    /* Caixa de Carta/Mensagem Fofa */
    .carta-romantica {
        background-color: #fff5f7;
        border: 1px solid #f8bbd0;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0px 6px 15px rgba(233, 30, 99, 0.05);
        margin-top: 15px;
        margin-bottom: 25px;
    }

    /* Caixa estilo cupom de amor */
    .cupom-gerado {
        background-color: #e91e63;
        border: 2px dashed #ffffff;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 15px;
    }

    /* Interações: Fundo Rosa com Texto 100% Branco */
    div[data-testid="stNotification"] {
        background-color: #e91e63 !important;
        border: none !important;
        border-radius: 12px !important;
    }
    div[data-testid="stNotification"] p {
        color: #ffffff !important;
        font-weight: bold !important;
        font-size: 16px !important;
        text-align: left !important;
    }
    div[data-testid="stNotification"] svg {
        fill: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO DO SITE ---
st.markdown("<h1>Nossa História de Amor ✨</h1>", unsafe_allow_html=True)

# Contador automático de dias
data_inicio = datetime(2024, 6, 12)
dias_juntos = (datetime.now() - data_inicio).days
st.write(f"💖 Juntos há **{dias_juntos} dias** criando o nosso próprio universo! 💖")

st.write("---")

# --- CRIANDO AS ABAS ---
aba1, aba2, aba3 = st.tabs(["💌 Uma Mensagem", "✨ Coisas Nossas", "🖼️ Álbum de Fotos"])

# --- ABA 1: UMA MENSAGEM PRA VOCÊ ---
with aba1:
    st.markdown("### Para a pessoa mais especial do mundo... 📜")

    # SUA CARTA OFICIAL PERSONALIZADA COLOCADA AQUI:
    st.markdown("""
    <div class="carta-romantica">
        <p style='text-align: justify; font-style: italic; color: #c2185b; margin: 0; font-weight: 500;'>
        "Gatinha, muito obrigado por mudar minha vida desde o dia que você voltou para mim. 
        No começo foi um pouquinho difícil, porém mesmo assim eu não desisti de você porque você 
        sabe que sempre fui louco por você. Então quero agradecer por simplesmente me transformar 
        em um homem de verdade e, obviamente, em um homem de Deus.<br><br>
        Sei que tem muitos traumas, porém quero ser o homem que vai te ajudar a curar você de todos 
        os seus traumas com minha forma de amar, te trazendo conforto. Te adoro muito e quero te 
        agradecer por tudo que já fez por mim.<br><br>
        Fiz essa mini surpresa, não é nada demais, porém foi feita com bastante amor. Que nós dois 
        sejamos muito felizes e que conquistemos muitas coisas juntas, e obviamente que Deus esteja 
        no nosso centro, porque sem Ele não somos nada.<br><br>
        Mas é isso, princesa, nada que você já não tenha ouvido antes, mas só quero te dizer que 
        sempre vou estar aqui para tudo que precisar. Você é incrível e muito especial para mim.<br><br>
        Te adoro muito, minha garota! ❤️"
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write(" ")

    st.markdown("#### ✨ Uma perguntinha rápida:")
    st.write("O quanto você me ama hoje?")

    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1:
        opcao1 = st.button("Daqui até a Lua 🌙", use_container_width=True)
    with col_btn2:
        opcao2 = st.button("Muuuito mais! 🚀", use_container_width=True)
    with col_btn3:
        opcao3 = st.button("Não dá pra medir! ♾️", use_container_width=True)

    if opcao1:
        st.success("Eu também te amo daqui até a lua... ida e volta! 🥰")
    elif opcao2:
        st.success("Segura esse amor então, porque o meu por você voa ainda mais alto! 🚀")
    elif opcao3:
        st.success("O universo é pequeno perto do tamanho do que eu sinto por você! ❤️")

    st.write("---")

    # ---------------------------------------------
    # JOGUINHO DO BOTÃO FUJÃO
    # ---------------------------------------------
    st.markdown("#### 💘 Responda com sinceridade:")
    st.write("Você gosta de mim?")

    st.components.v1.html("""
    <div style="display: flex; justify-content: center; align-items: center; gap: 40px; height: 100px; font-family: 'Helvetica', sans-serif;">
        <button id="btnSim" style="padding: 12px 30px; font-size: 18px; font-weight: bold; background-color: #28a745; color: white; border: none; border-radius: 8px; cursor: pointer;">SIM! 😍</button>
        <button id="btnNao" style="padding: 12px 30px; font-size: 18px; font-weight: bold; background-color: #dc3545; color: white; border: none; border-radius: 8px; position: relative; cursor: pointer; transition: all 0.1s ease;">NÃO 😢</button>
    </div>

    <div id="mensagemSucesso" style="display: none; text-align: center; color: #e91e63; font-size: 20px; font-weight: bold; margin-top: 10px;">
        Sabia! vc e incrivel te adoro muitão! 🥰❤️
    </div>

    <script>
        const btnNao = document.getElementById('btnNao');
        const btnSim = document.getElementById('btnSim');
        const mensagem = document.getElementById('mensagemSucesso');

        function desviar() {
            const larguraJanela = 200;
            const alturaJanela = 50;
            const xAleatorio = Math.floor(Math.random() * larguraJanela) - (larguraJanela / 2);
            const yAleatorio = Math.floor(Math.random() * alturaJanela) - (alturaJanela / 2);
            btnNao.style.transform = `translate(${xAleatorio}px, ${yAleatorio}px)`;
        }

        btnNao.addEventListener('mouseover', desviar);
        btnNao.addEventListener('touchstart', (e) => {
            e.preventDefault();
            desviar();
        });

        btnSim.addEventListener('click', () => {
            mensagem.style.display = 'block';
            btnNao.style.display = 'none';
            btnSim.style.display = 'none';
        });
    </script>
    """, height=150)

    st.write("---")

    if st.button("Clique aqui para abrir um segredo de nós dois 🤫", use_container_width=True):
        st.balloons()
        st.success("Você é, sem dúvidas, o meu melhor momento todos os dias! ❤️")
        st.snow()

# --- ABA 2: COISAS NOSSAS ---
with aba3:
    pass

with aba2:
    st.markdown("### 🎟️ Seus Cupons de Amor")
    st.write("Clique para gerar o seu cupom. Tire um print e me cobre quando quiser!")

    col_c1, col_c2, col_c3 = st.columns(3)
    with col_c1:
        c1 = st.button("Cupom Massagem 💆‍♀️", use_container_width=True)
    with col_c2:
        c2 = st.button("Cupom Jantar 🍕", use_container_width=True)
    with col_c3:
        c3 = st.button("Cupom Cinema 🎬", use_container_width=True)

    if c1:
        st.markdown('<div class="cupom-gerado"><h4 style="color:white !important; margin:0;">VALE 1 MASSAGEM CAPRICHADA</h4><p style="color:white; font-size:14px; margin:5px 0 0 0;">Válido para quando você estiver cansada. Reclamação zero garantida!</p></div>', unsafe_allow_html=True)
    elif c2:
        st.markdown('<div class="cupom-gerado"><h4 style="color:white !important; margin:0;">VALE 1 JANTAR POR MINHA CONTA</h4><p style="color:white; font-size:14px; margin:5px 0 0 0;">Eu cozinho ou eu pago o delivery da sua comida favorita. Você escolhe!</p></div>', unsafe_allow_html=True)
    elif c3:
        st.markdown('<div class="cupom-gerado"><h4 style="color:white !important; margin:0;">VALE 1 CINEMA (VOCÊ ESCOLHE)</h4><p style="color:white; font-size:14px; margin:5px 0 0 0;">Direito a escolher o filme e o combo de pipoca sem eu dar nenhum piu.</p></div>', unsafe_allow_html=True)

    st.write("---")

    st.markdown("### 🧠 Jogo: O quanto você me conhece?")
    st.write("Responda à pergunta abaixo:")

    pergunta = st.radio(
        "Qual é o meu programa favorito para fazer junto com você?",
        ["Ir a festas barulhentas", "Ficar de bobeira comendo e assistindo algo", "Fazer caminhadas longas no sol"],
        index=None,
        label_visibility="collapsed"
    )

    if pergunta == "Ficar de bobeira comendo e assistindo algo":
        st.balloons()
        st.success("Acertou em cheio! Estar bem grudadinho com você e comendo algo gostoso é a melhor coisa do mundo! 🍿❤️")
    elif pergunta is not None:
        st.error("Errou feio, errou feio! ❌ Como punição vai ter que me dar 10 beijos agora mesmo!")

    st.write("---")

    st.markdown("###
