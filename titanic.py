import pandas as pd
import streamlit as st

df = pd.read_csv(r'C:\Users\User\Downloads\Titanic Data.csv')

print(df.columns)

df.drop(columns=['PassengerId', 'Cabin'], inplace=True)
print(df.head())

st.title('Titanic Dataset Analysis')
st.write(df.head(10))

dff=df.groupby(['Sex', 'Pclass'])[['Survived']].value_counts().reset_index(name='count')
print(dff)

st.title('Bar on Count of Sex by Passenger Class')
st.bar_chart(dff, x='Pclass', y='count', color='Sex', stack=False, x_label='Passenger Class', y_label='Number of Passengers')

st.title('Bar on Count of Sex by Passenger Survival Status')
st.bar_chart(dff, x='Survived', y='count', color='Sex', stack=False, horizontal=True, x_label='Number of Passengers', y_label='Survived')
