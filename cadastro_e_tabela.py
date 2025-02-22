import streamlit as st
import streamlit_authenticator as stauth
from dependencies_final import add_registro, consulta_geral, consulta


db_query = consulta_geral()

registros = {'usernames': {}}
for data in db_query:
    registros['usernames'][data[1]] = {'name' : data[0], 'password' : data[4]}

COOKIE_EXPIRY_DAYS = 30
authenticator = stauth.Authenticate(
    registros,
    'random_cookie_name',
    'random_signature_key',
    COOKIE_EXPIRY_DAYS,

)

def usuario_form():
    with st.form(key="test", clear_on_submit=True):
        nome = st.text_input("Nome", key="nome")
        username = st.text_input("Usuário", key="user")
        email = st.text_input("E-mail", key="email")
        fone = st.text_input("Fone", key="fone")
        password = st.text_input("Password", key="pswrd", type="password")
        confirm_password = st.text_input("Confirm Password", key="confirm_pswrd", type="password")
        submit = st.form_submit_button(
            "Salvar", on_click=confirmation_msg,
        )

def confirmation_msg():
    hashed_password = stauth.Hasher([st.session_state.pswrd]).generate()
    if st.session_state.pswrd != st.session_state.confirm_pswrd:
        st.warning('Senhas não conferem')
        #sleep(3)
    elif consulta(st.session_state.user):
        st.warning('Nome de usuário já existe.')
        #sleep(3)
    else:
        add_registro(st.session_state.nome,st.session_state.user,st.session_state.email,
                     st.session_state.fone,hashed_password[0])
        st.success('Registro efetuado!')
        #sleep(3)


def main():
    st.write("Essa a ficha de controle dos usuários")

    usuario_form()

    # Exibir a tabela de cadastrados
    st.title("Tabela de Cadastrados")
    registros = consulta_geral()
    if registros:
        st.table(registros)
    else:
        st.info("Nenhum cadastro encontrado.")



if __name__ == "__main__":
    main()