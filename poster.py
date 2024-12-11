from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🎁 제품 홍보 포스터 생성기")

keyword = st.text_input("키워드를 입력하세요")
if st.button('생성하기'):

    with st.spinner("생성 중입니다."):
        if keyword:
            response = client.chat.completions.create(
                model="gpt-4",
                temperature=0.2,  # 0~1, 창의성 값
                messages=[{
                    "role": "system",
                    "content": "입력 받은 키워드에 대한 150자 이내의 솔깃한 제품 광고 문구를 작성해줘"
                },
                    {
                        "role": "user",
                        "content": keyword,
                    }
                ]
            )

            st.success(response.choices[0].message.content)

    with st.spinner("이미지를 생성 중입니다."):
        if keyword:
            response = client.images.generate(
                model="dall-e-3",
                prompt=keyword,
                n=1,
                size="1024x1024"
            )

            st.image(response.data[0].url)