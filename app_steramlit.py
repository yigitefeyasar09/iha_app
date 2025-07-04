import streamlit as st

st.title("İHA Uçuş Uygulaması - Web Versiyon")

username = st.text_input("Kullanıcı Adı")
password = st.text_input("Şifre", type="password")

if st.button("Giriş Yap"):
    if username == "AltNom2025" and password == "AltNom2025":
        st.success("Giriş başarılı! Ana uygulama gösteriliyor...")
        # Buraya ana uygulamanın web versiyonunu ekle
        st.write("Burada uçuş verileri ve kontroller olacak.")
    else:
        st.error("Hatalı giriş!")
