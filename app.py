import streamlit as st
from PIL import Image
import random

def main():
    st.title("İHA Uçuş Uygulaması")

    # Logolar
    try:
        teknofest_img = Image.open("teknofest_logo.png")
        st.image(teknofest_img, width=150)
    except Exception as e:
        st.write("teknofest_logo.png yüklenemedi:", e)

    try:
        sag_img = Image.open("sag_kose_resmi.png")
        st.image(sag_img, width=150)
    except Exception as e:
        st.write("sag_kose_resmi.png yüklenemedi:", e)

    # Kullanıcı adı ve şifre kontrolü (basit)
    username = st.text_input("Kullanıcı Adı")
    password = st.text_input("Şifre", type="password")
    if st.button("Giriş Yap"):
        if username == "AltNom2025" and password == "AltNom2025":
            st.success("Giriş Başarılı!")

            # Yakıt seviyesi
            fuel_level = st.progress(75)
            altitude = st.metric("İrtifa (m)", 320)
            coordinates = st.text("Koordinatlar: 41.12167° N, 29.02936° E")

            # Simülasyon güncellemesi
            for i in range(75, 0, -1):
                fuel_level.progress(i)
                altitude.metric(f"İrtifa (m)", random.randint(310, 330))
                lat = round(39.9200 + random.uniform(-0.001, 0.001), 6)
                lon = round(32.8540 + random.uniform(-0.001, 0.001), 6)
                coordinates.text(f"Koordinatlar: {lat}° N, {lon}° E")
                st.sleep(0.5)

        else:
            st.error("Hatalı Giriş")

if __name__ == "__main__":
    main()
