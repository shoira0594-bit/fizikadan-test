import streamlit as st
import os

# Sahifa dizayni va sarlavhasi
st.set_page_config(page_title="Temperatura va issiqlik hodisalari", page_icon="🌡️")
st.title(" Temperatura va issiqlik hodisalari")
st.subheader("9-sinf Fizika: O'quvchilar bilimini tekshirish")

# 10 ta test savollari bazasi
savollar = [
    {
        "id": 1,
        "savol": "Modda zarralarining tartibsiz issiqlik harakati o‘rtacha kinetik energiyasining o‘lchovi nima deyiladi?",
        "variantlar": ["A) issiqlik miqdori", "B) temperatura", "C) ichki energiya", "D) energiya"],
        "togri_javob": "B) temperatura"
    },
    {
        "id": 2,
        "savol": "Xalqaro birliklar sistemasida temperaturaning asosiy birligi qaysi?",
        "variantlar": ["A) Selsiy darajasi", "B) Kelvin", "C) Farengeyt", "D) kaloriya"],
        "togri_javob": "B) Kelvin"
    },
    {
        "id": 3,
        "savol": "Tabiatda uchrashi mumkin bo‘lgan eng past chegara, ya'ni mutloq nol temperatura Selsiy shkalasida nechaga teng?",
        "variantlar": ["A) nol gradus Selsiy", "B) minus yuz gradus Selsiy", "C) minus ikki yuz yetmish uch gradus Selsiy", "D) to'g'ri variant yo'q"],
        "togri_javob": "A) nol gradus Selsiy"
    },
    {
        "id": 4,
        "savol": "Suyuqlikli termometrlarning ishlash prinsipi moddalarning qaysi xossasiga asoslangan?",
        "variantlar": ["A) Issiqlikdan kengayishiga", "B) Kimyoviy reaksiyaga kirishishiga", "C) Massasining ortishiga", "D) Rangining o‘zgarishiga."],
        "togri_javob": "C) Massasining ortishiga"
    },
    {
        "id": 5,
        "savol": "Xonadagi termometr yigirma yetti gradus Selsiy temperaturani ko‘rsatmoqda. Ushbu ko‘rsatkich Kelvin shkalasida nechaga teng bo‘ladi?",
        "variantlar": ["A) ikki yuz qirq olti Kelvin", "B) uch yuz Kelvin", "C) ikki yuz yetmish uch Kelvin", "D) uch yuz yigirma yetti Kelvin."],
        "togri_javob": "A) ikki yuz qirq olti Kelvin"
    },
    {
        "id": 6,
        "savol": "Mutloq nol temperaturada modda zarralarining harakati qanday holatda bo‘ladi?",
        "variantlar": ["A) Tezligi maksimal darajaga yetadi.", "B) Ilgarilanma harakati butunlay to‘xtaydi.", "C) Zarralar parchalana boshlaydi.", "D) Harakat tezligi o‘zgarmay qoladi."],
        "togri_javob": "B) Ilgarilanma harakati butunlay to‘xtaydi."
    },
    {
        "id": 7,
        "savol": "Agar jismning temperaturasi o'n besh gradus Selsiyga ko‘tarilgan bo‘lsa, uning Kelvin shkalasidagi o‘zgarishi, ya'ni delta Te nimaga teng?",
        "variantlar": ["A) o'n besh Kelvin ga ortgan.", "B) ikki yuz sakson sakkiz Kelvin ga ortgan.", "C) o'n besh Kelvin ga kamaygan.", "D) ikki yuz ellik bitta Kelvin ga kamaygan."],
        "togri_javob": "B) ikki yuz sakson sakkiz Kelvin ga ortgan."
    },
    {
        "id": 8,
        "savol": "Normal atmosfera bosimida muzlash va qaynash nuqtalari orasidagi farq Selsiy va Kelvin shkalalarida qanday nisbatda bo‘ladi?",
        "variantlar": ["A) Selsiyda ko‘p, Kelvin hisobida kam.", "B) Kelvinda ko‘p, Selsiy hisobida kam.", "C) Ikkala shkalada ham farq bir xil, ya'ni yuzga teng.", "D) Bu shkalalarni o‘zaro solishtirib bo‘lmaydi."],
        "togri_javob": "A) Selsiyda ko‘p, Kelvin hisobida kam."
    },
    {
        "id": 9,
        "savol": "Termodinamik muvozanatda turgan tizimning hamma qismlarida qaysi kattalik bir xil bo‘ladi?",
        "variantlar": ["A) Bosim.", "B) Temperatura.", "C) Hajm.", "D) Zichlik."],
        "togri_javob": "C) Hajm."
    },
    {
        "id": 10,
        "savol": "Temperatura modda zarrachalarining qaysi harakatini xarakterlaydi?",
        "variantlar": ["A) Zarrachalarning tartibsiz, issiqlik harakati o'rtacha kinetik energiyasini.", "B) Zarrachalarning faqat tartibli harakat tezligini.", "C) Moddaning umumiy potensial energiyasini.", "D) Zarrachalar o'rtasidagi o'zaro ta'sir kuchlarini."],
        "togri_javob": "B) Zarralarning faqat tartibli harakat tezligini."
    }
]

# Tizimga kirish qismi (Faqat Ism va Sinf)
st.sidebar.header("📝 O'quvchi ma'lumotlari")
o_ism = st.sidebar.text_input("Ism va Familiyangiz:")
o_sinf = st.sidebar.text_input("Sinfingiz (Masalan: 9-A):")

if not o_ism or not o_sinf:
    st.warning("👈 Testni boshlash uchun chap tomondagi menyuda Ism va Sinfingizni kiriting!")
else:
    st.success(f"Omad tilaymiz, {o_ism}! Test savollarini tinglang va javoblarni belgilang.")
    
    # Test shakli
    with st.form(key='fizika_sodda_test_form'):
        foydalanuvchi_javoblari = {}
        
        for s in savollar:
            st.subheader(f"{s['id']}-savol:")
            st.write(s['savol'])
            
            audio_path = f"audio_files/savol_{s['id']}.mp3"
            if os.path.exists(audio_path):
                st.audio(audio_path, format='audio/mp3')
            else:
                st.warning(f"⚠️ audio_files papkasida 'savol_{s['id']}.mp3' topilmadi.")
                
            tanlov = st.radio("Javob varianti:", s['variantlar'], key=f"radio_{s['id']}")
            foydalanuvchi_javoblari[s['id']] = tanlov
            st.markdown("---")
            
        submit_button = st.form_submit_button(label="Testni yakunlash va natijani ko'rish")

    # Natija chiqarish
    if submit_button:
        ball = 0
        st.subheader("📊 Imtihon Natijasi:")
        st.write(f"**O'quvchi:** {o_ism}")
        st.write(f"**Sinf:** {o_sinf}")
        
        # Savollarni tekshirish natijasi
        for s in savollar:
            if foydalanuvchi_javoblari[s['id']] == s['togri_javob']:
                ball += 1
                st.write(f"✅ {s['id']}-savol: To'g'ri")
            else:
                st.write(f"❌ {s['id']}-savol: Noto'g'ri (Siz belgiladingiz: {foydalanuvchi_javoblari[s['id']]})")
                
        st.markdown("---")
        st.success(f"### Umumiy natija: Siz 10 ta savoldan {ball} tasiga to'g'ri javob berdingiz! 🎉")
        
        if ball == 10:
            st.balloons()
