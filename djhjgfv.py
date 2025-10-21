import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Генерация текста",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("Генерация текста")
st.markdown(
    """
    Это приложение использует предобученную модель GPT-2 для генерации текста на основе введенной вами подсказки.
    Введите начальный текст, выберите максимальную длину сгенерированного ответа, и модель сгенерирует продолжение!
    """
)
st.markdown("---")
@st.cache_resource
def load_gpt2_pipeline():
    return pipeline("text-generation", model="gpt2")

with st.spinner("Загружаю модель GPT-2..."):
    generator = load_gpt2_pipeline()

st.subheader("Введите начальный текст:")
user_prompt = st.text_area(
    "Введите здесь текст, с которого начнется генерация:",
    "",
    height=150
)

st.subheader("Настройки генерации:")
max_length = st.slider(
    "Максимальная длина генерируемого текста:",
    min_value=30,
    max_value=300,
    value=100,
    step=10
)

if st.button("Сгенерировать текст"):
    if user_prompt:
        with st.spinner("Генерирую текст..."):
            generated_output = generator(user_prompt, max_length=max_length, num_return_sequences=1)

            st.subheader("Сгенерированный текст:")
            st.success(generated_output[0]['generated_text'])
    else:
        st.warning("Введите текст для генерации.")

st.markdown("---")
st.info("Работу выполнили: Ибраева Асем и Киреева Анастасия")
