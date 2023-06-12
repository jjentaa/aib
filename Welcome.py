import streamlit as st

st.set_page_config(page_title="Manga Recommendation",page_icon="📚")
st.title("Manga Recommendation 📚")

st.header("How to!")
st.markdown('''1. ตอนนี้เราอยู่ที่หน้า Welcome ทางซ้ายมือจะมีแถบกดให้เลือกหน้า
2. เริ่มต้น เราสามารถเลือกที่จะลอง model ได้ 2 ตัวค่ะ คือ eng model ที่รองรับภาษาอังกฤษเท่านั้น และ multi model ที่รองรับภาษาอื่นๆ
3. พอกดเข้าไปแต่ละหน้าแล้วเนี่ย สามารถใส่ requirement สำหรับมังงะที่ตามหาได้เลย แล้วกด enter
4. ถ้าไม่รู้จะเริ่มยังไงดี เรามีตัวอย่างทั้งหมด 3 query ให้ในแต่ละหน้า สามารถกดปุ่มได้เลยค่ะ
5. รอซักพักนึง จะมีชื่อมังงะ กับรูปประกอบที่เราแนะนำให้ค่ะ
6. พอเล่นจนพอใช้แล้วเนี่ย ช่วยกดไปที่หน้า give-feedback กรอก feedback เล็กๆน้อยๆทิ้งไว้ให้เราหน่อยนะคะ เราจะได้เอาไปปรับปรุงต่อ''')

st.markdown('''ปล. หน้า multi model เข้าไปอาจจะใช้เวลารอนานระดับนึงเพื่อเริ่มใช้งาน ไม่ต้องห่วงนะคะ เว็บไม่ได้ค้าง
ถ้าใครอยากรู้รายละเอียด link ของบทความจะอยู่ด้านล่างค่ะ และก็เราทิ้งช่องทางการติดต่อเราไว้ด้วย เผื่อใครสงสัยอะไร ทักมาคุยกันได้เลยค่ะ''')



st.subheader("Contact me!")
url_blog = "https://medium.com/@madness_/manga-recommendation-️-a8147d933c51 "
st.markdown("My blog : [medium.com/@madness_/manga-recommendation](%s)" % url_blog)

url_code = "https://github.com/jjentaa/manga-recommendation/"
st.markdown("My code : [jjentaa/manga-recommendation/](%s)" % url_code)

st.markdown("My discord : NongJane#8452" )
