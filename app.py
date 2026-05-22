import streamlit as st
import os

# Sahifa dizayni va sarlavhasi
st.set_page_config(page_title="Temperatura va issiqlik hodisalari", page_icon="🌡️")
st.title("🌡️ Ovozli test: Temperatura va issiqlik hodisalari")
st.subheader("9-sinf Fizika: Molekulyar fizika bo'limi")
st.write("Savollarni eshitish uchun ovoz pleyeridan foydalaning va to'g'ri javobni tanlang.")

# Siz yuborgan 10 ta test savoli va kalit bo'yicha to'g'ri javoblari
savollar = [
    {
        "id": 1,
        "savol": "Modda zarralarining tartibsiz issiqlik harakati o‘rtacha kinetik energiyasining o‘lchovi nima deyiladi?",
        "variantlar": ["A) issiqlik miqdori", "B) temperatura", "C) ichki energiya", "D) energiya"],
        "togri_javob": "B) temperatura"  # Kalit: 1-B
    },
    {
        "id": 2,
        "savol": "Xalqaro birliklar sistemasida temperaturaning asosiy birligi qaysi?",
        "variantlar": ["A) Selsiy darajasi", "B) Kelvin", "C) Farengeyt", "D) kaloriya"],
        "togri_javob": "B) Kelvin"  # Kalit: 2-B
    },
    {
        "id": 3,
        "savol": "Tabiatda uchrashi mumkin bo‘lgan eng past chegara, ya'ni mutloq nol temperatura Selsiy shkalasida nechaga teng?",
        "variantlar": ["A) nol gradus Selsiy", "B) minus yuz gradus Selsiy", "C) minus ikki yuz yetmish uch gradus Selsiy", "D) to'g'ri variant yo'q"],
        "togri_javob": "A) nol gradus Selsiy"  # Kalit: 3-A
    },
    {
        "id": 4,
        "savol": "Suyuqlikli termometrlarning ishlash prinsipi moddalarning qaysi xossasiga asoslangan?",
        "variantlar": ["A) Issiqlikdan kengayishiga", "B) Kimyoviy reaksiyaga kirishishiga", "C) Massasining ortishiga", "D) Rangining o‘zgarishiga."],
        "togri_javob": "C) Massasining ortishiga"  # Kalit: 4-C
    },
    {
        "id": 5,
        "savol": "Xonadagi termometr yigirma yetti gradus Selsiy temperaturani ko‘rsatmoqda. Ushbu ko‘rsatkich Kelvin shkalasida nechaga teng bo‘ladi?",
        "variantlar": ["A) ikki yuz qirq olti Kelvin", "B) uch yuz Kelvin", "C) ikki yuz yetmish uch Kelvin", "D) uch yuz yigirma yetti Kelvin."],
        "togri_javob": "A) ikki yuz qirq olti Kelvin"  # Kalit: 5-A
    },
    {
        "id": 6,
        "savol": "Mutloq nol temperaturada modda zarralarining harakati qanday holatda bo‘ladi?",
        "variantlar": ["A) Tezligi maksimal darajaga yetadi.", "B) Ilgarilanma harakati butunlay to‘xtaydi.", "C) Zarralar parchalana boshlaydi.", "D) Harakat tezligi o‘zgarmay qoladi."],
        "togri_javob": "B) Ilgarilanma harakati butunlay to‘xtaydi."  # Kalit: 6-B
    },
    {
        "id": 7,
        "savol": "Agar jismning temperaturasi o'n besh gradus Selsiyga ko‘tarilgan bo‘lsa, uning Kelvin shkalasidagi o‘zgarishi, ya'ni delta Te nimaga teng?",
        "variantlar": ["A) o'n besh Kelvin ga ortgan.", "B) ikki yuz sakson sakkiz Kelvin ga ortgan.", "C) o'n besh Kelvin ga kamaygan.", "D) ikki yuz ellik bitta Kelvin ga kamaygan."],
        "togri_javob": "B) ikki yuz sakson sakkiz Kelvin ga ortgan."  # Kalit: 7-B
    },
    {
        "id": 8,
        "savol": "Normal atmosfera bosimida muzlash va qaynash nuqtalari orasidagi farq Selsiy va Kelvin shkalalarida qanday nisbatda bo‘ladi?",
        "variantlar": ["A) Selsiyda ko‘p, Kelvin hisobida kam.", "B) Kelvinda ko‘p, Selsiy hisobida kam.", "C) Ikkala shkalada ham farq bir xil, ya'ni yuzga teng.", "D) Bu shkalalarni o‘zaro solishtirib bo‘lmaydi."],
        "togri_javob": "A) Selsiyda ko‘p, Kelvin hisobida kam."  # Kalit: 8-A
    },
    {
        "id": 9,
        "savol": "Termodinamik muvozanatda turgan tizimning hamma qismlarida qaysi kattalik bir xil bo‘ladi?",
        "variantlar": ["A) Bosim.", "B) Temperatura.", "C) Hajm.", "D) Zichlik."],
        "togri_javob": "C) Hajm."  # Kalit: 9-C
    },
    {
        "id": 10,
        "savol": "Temperatura modda zarrachalarining qaysi harakatini xarakterlaydi?",
        "variantlar": ["A) Zarrachalarning tartibsiz, issiqlik harakati o'rtacha kinetik energiyasini.", "B) Zarrachalarning faqat tartibli harakat tezligini.", "C) Moddaning umumiy potensial energiyasini.", "D) Zarrachalar o'rtasidagi o'zaro ta'sir kuchlarini."],
        "togri_javob": "B) Zarrachalarning faqat tartibli harakat tezligini."  # Kalit: 10-B
    }
]

# Test shakli (Forma)
with st.form(key='fizika_final_test_form'):
    foydalanuvchi_javoblari = {}
    
    for s in savollar:
        st.subheader(f"{s['id']}-savol:")
        st.write(s['savol'])
        
        # Audio fayl yo'li (audio_files/savol_1.mp3 va h.k.)
        audio_path = f"audio_files/savol_{s['id']}.mp3"
        
        if os.path.exists(audio_path):
            st.audio(audio_path, format='audio/mp3')
        else:
            st.warning(f"⚠️ audio_files papkasida 'savol_{s['id']}.mp3' fayli hali yuklanmagan.")
            
        # Variantlar radio tugmalari
        tanlov = st.radio("To'g'ri javob variantini tanlang:", s['variantlar'], key=f"radio_{s['id']}")
        foydalanuvchi_javoblari[s['id']] = tanlov
        st.markdown("---")
        
    submit_button = st.form_submit_button(label="Natijalarni tekshirish")

# Natijalarni tekshirish qismi
if submit_button:
    ball = 0
    for s in savollar:
        if foydalanuvchi_javoblari[s['id']] == s['togri_javob']:
            ball += 1
            
    st.success(f"Imtihon yakunlandi! Siz 10 ta savoldan {ball} tasiga to'g'ri javob berdingiz! 🎉")
    
    # Rag'batlantirish
    if ball == 10:
        st.balloons()
        st.success("Ajoyib natija! 100% to'g'ri! 🥇")
    elif ball >= 7:
        st.info("Yaxshi ko'rsatkich, ballingiz yuqori! 👍")
    else:
        st.warning("Mavzuni yana bir bor takrorlashni tavsiya qilamiz. 📖")
