"""
[ streamlit (sidebar) ]

streamlit 사이드바


"""


#####   라이브러리

# 내장
from PIL import Image

# 외부
import streamlit as st



#####   streamlit

### 사이드바
st.sidebar.title("Side Bar")

# 아이디 비밀번호
st.sidebar.header("Text Input")

if 'login_status' not in st.session_state:
    st.session_state['login_status'] = ''

with st.sidebar.form("Login"):
    user_id = st.text_input("User ID", value='streamlit', max_chars=15)
    user_pw = st.text_input("Password", value="1234", type="password")
    submitted = st.form_submit_button("Login")
    if submitted:
        if (user_id == 'streamlit') & (user_pw == '1234'):
            st.write("Login Success")
            st.session_state['login_status'] = 'ok'
        else:
            st.write("Login Fail")
            st.session_state['login_status'] = 'fail'

# 이미지 선택
st.sidebar.header("Select Box")
select_opt = ['진주 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '월하정인']
user_opt = st.sidebar.selectbox("Choose img", select_opt)
st.sidebar.write("Img : ", user_opt)


### 메인 화면
st.title("Streamlit Sidebar")

# 선택한 항목의 인덱스
selected_index = select_opt.index(user_opt)

# 선택한 항목에 맞는 이미지 파일 지정
folder = "0613_AI/data/"
img_files = ["Vermeer.png", "Gogh.png", "Munch.png", "ShinYoonbok.png"]
selected_img = img_files[selected_index]
selected_img_file = Image.open(folder+selected_img)

if st.session_state['login_status'] == 'ok':

    # 선택한 이미지 표시
    st.image(selected_img_file, caption=user_opt)

else:
    st.write("Please log in to view the image.")


