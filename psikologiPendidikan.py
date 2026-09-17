import streamlit as st

st.set_page_config(layout="wide")

if "kumpulan" not in st.session_state:
    st.session_state['kumpulan']={'judul':True,'rps':False, 'pertemuan1':False}


#=======================

def kover():
    tulisan_html='''
    <iframe src='https://martin-bernard26.github.io/psikologiPendidikan/kover.html' style='width:100%; height:1500px'></iframe>
    '''
    st.components.v1.html(tulisan_html,height=1500)

def pengenalan():
    tulisan_html='''
    <iframe src='https://drive.google.com/file/d/11cCKrfs-47xbsa4To_MDZgFoLDPPYlfG/preview' style='width:100%; height:1000px'></iframe>
    '''
    st.components.v1.html(tulisan_html,height=1000)

def materi1():
    menu = st.tabs(['Ruang Lingkup Psikologi','Referensi'])
    with menu[0]:
        tulisan_html='''
    <iframe src='https://martin-bernard26.github.io/psikologiPendidikan/psikologi1.html' style='width:100%; height:1500px'></iframe>
    '''
        st.components.v1.html(tulisan_html,height=1500)
    with menu[1]:
        with st.expander("Prof. Dr. Nur Hidayah, M.Pd"):
            tulisan_html='''
            <iframe src='https://drive.google.com/file/d/1xSe8O_174dpM_qRaYDeS91lrfyd_ZqSn/preview' style='width:100%; height:1500px'></iframe>
            '''
            st.components.v1.html(tulisan_html,height=1500)
        with st.expander("Dr. Eko Harianto, S.Sos.I., M.Si."):
            tulisan_html='''
            <iframe src='https://drive.google.com/file/d/1CH17k1Oo95275fS6FqN9P0INMK37EbdF/preview' style='width:100%; height:1500px'></iframe>
            '''
            st.components.v1.html(tulisan_html,height=1500)
        with st.expander("Dr. Pupu Saeful Rahmat, M.Pd"):
            tulisan_html='''
            <iframe src='https://drive.google.com/file/d/1LzKOYs34M2v-1NSVBgqXY8cws3atK3Sa/preview' style='width:100%; height:1500px'></iframe>
            '''
            st.components.v1.html(tulisan_html,height=1500)


#=======================

if st.session_state['kumpulan']['judul']:
    kover()
if st.session_state['kumpulan']['rps']:
    pengenalan()
if st.session_state['kumpulan']['pertemuan1']:
    materi1()

#=========================

if st.sidebar.button("Bagian Depan"):
    st.session_state['kumpulan']={'judul':True,'rps':False, 'pertemuan1':False}
    st.rerun()

if st.sidebar.button("Rencana Pembelajaran Semester"):
    st.session_state['kumpulan']={'judul':False,'rps':True, 'pertemuan1':False}
    st.rerun()

if st.sidebar.button("Pertemuan 1"):
    st.session_state['kumpulan']={'judul':False,'rps':False, 'pertemuan1':True}
    st.rerun()
    
    

