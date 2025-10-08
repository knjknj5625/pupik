import streamlit as st
import pandas as pd
import numpy as np

st.title("Я долго мучилась и что-то получилоось")

st.image("sobak.jpg", caption="Грустная собака", width=300)

titanic = pd.read_csv('https://huggingface.co/datasets/ankislyakov/titanic/resolve/main/titanic_train.csv', index_col='PassengerId')
st.header("Данные Титаника")
st.write("Первые 5 строк данных:")
st.dataframe(titanic.head())



user_soblez = st.text_input("Введите ваши соболезнования:", " ")
st.write(f"Спасибо за: {user_soblez}!")


def children(data):
    count = {'C': 0, 'Q': 0, 'S': 0}
    max_age = {'C': 0, 'Q': 0, 'S': 0}
    children = 0
    
    for index, row in data.iterrows():
        if pd.notna(row['Age']) and row['Age'] < 18 and row['Survived'] == 0:
            embarked = row['Embarked']
            
            if embarked in count:
                count[embarked] += 1
                children +=1
                
            if embarked in ['C', 'Q', 'S'] and row['Age'] > max_age[embarked]:
                max_age[embarked] = int(row['Age'])
    
    return count, children, max_age  

emb,  children, max_age = children(titanic)

st.header("Анализ детской смертности на Титанике")

st.subheader("Погибло детей по портам посадки")
ports_table = pd.DataFrame({
    'Порт': ['Шебург (C)', 'Квинстоун (Q)', 'Саутгемптон (S)', 'ВСЕГО'],
    'Количество': [emb['C'], emb['Q'], emb['S'], children]
})
st.table(ports_table)

st.subheader("Максимальный возраст погибших детей по портам")
class_table = pd.DataFrame({
    'Порт': ['Шербур (C)', 'Квинстаун (Q)', 'Саутгемптон (S)', 'ВСЕГО'],
    'Возраст:': [
        f"{max_age['C']} лет" if max_age['C'] > 0 else "нет данных",
        f"{max_age['Q']} лет" if max_age['Q'] > 0 else "нет данных", 
        f"{max_age['S']} лет" if max_age['S'] > 0 else "нет данных",
        f"{max(max_age.values())} лет"  
    ]
})
st.table(class_table)

age = st.slider("Возраст ребенка:", min_value=0, max_value=17, value=0)

def colvo(data, select):
    count_port = {'C': 0, 'Q': 0, 'S': 0}
    
    for index, row in data.iterrows():
        if (pd.notna(row['Age']) and 
            int(row['Age']) == select and 
            row['Survived'] == 0 and 
            row['Age'] < 18):
            
            embarked = row['Embarked']
            if embarked in count_port:
                count_port[embarked] += 1
    
    return count_port

age_counts = colvo(titanic, age)
helo = sum(age_counts.values())

st.subheader(f"Количество умерших детей {age} лет по портам посадки")

age_tab = pd.DataFrame({
    'Порт': ['Шербур (C)', 'Квинстаун (Q)', 'Саутгемптон (S)', 'ВСЕГО'],
    'Количество': [
        age_counts['C'],
        age_counts['Q'], 
        age_counts['S'],
        helo
    ]
})

st.table(age_tab)


st.success('Лаба завершена!')

