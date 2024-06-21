from configuration import gs_credit_nails, st as st, urls
import pandas as pd
import gspread

password = st.secrets["database"]["password"]
st.set_page_config(page_title="Fast Dash", page_icon=":moneybag:", layout="wide")
gc = gspread.service_account_from_dict(gs_credit_nails)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def process_url(incoming):
    left_part = incoming.split("edit?gid")[0]
    table_id = incoming.split("#gid=")[1]
    result = left_part + "export?format=csv&gid=" + table_id
    return result


def read_gsheet_by_url(url):
    try:
        url2 = process_url(url)
        df = pd.read_csv(url2)
        return df
    except Exception as e:
        print(f"Ошибка загрузки данных: {e}")


def is_authenticated():
    return "authenticated" in st.session_state and st.session_state.authenticated


def login():
    with st.form("my_form"):
        st.title("Вход в приложение")
        password_input = st.text_input("Введите пароль", type="password")

        submit = st.form_submit_button("Войти")
        if submit:
            if password_input == password:
                st.success("Успешный вход!")
                st.session_state.authenticated = True
                st.experimental_rerun()
                # После успешного входа скрываем поля ввода и кнопку
                show_main_page()
            else:
                st.error("Неверный пароль")


def show_main_page():
    # Заголовок дашборда
    st.title(" :moneybag: PowerDash")
    st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)
    for worker, objects in urls.items():
        st.write(worker)
        for name, url in objects.items():
            st.write(name)
            st.write(read_gsheet_by_url(url))


if not is_authenticated():
    # Если пользователь еще не авторизован, показываем поля ввода и кнопку для входа
    if "hide_login" not in st.session_state or not st.session_state.hide_login:
        login()
else:
    # Если пользователь уже авторизован, сразу показываем главную страницу
    show_main_page()
