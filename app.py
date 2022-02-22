import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt


st.title("Streamlit quick start")

st.header("Write and Magic")

"hello world"

st.write("hello CSE 5544")

st.header("Text elements")

st.subheader("This is a subheader")

st.text("This is a text")

#markdown grammar https://www.markdownguide.org/
st.subheader("markdown")
st.markdown("# H1")
st.markdown("## H2")
st.markdown("### H3")

st.subheader("latext")
st.latex("\sum_{0}^{n-1}i")

st.subheader("bootstrap alerts")
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")

st.header("Display data")

df = pd.DataFrame({
  'c1': [1, 2, 3, 4],
  'c2': [10, 20, 30, 40]
})

df

st.subheader("Load your data from url")

data = pd.read_csv("https://web.cse.ohio-state.edu/~li.8950/data/ClimateData.csv")
data

st.header("Chart elements")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.subheader("draw chart using matplotlib")

countries = data['Country\year']
chart_data = data.iloc[:,2:]
chart_data = chart_data.apply(pd.to_numeric, errors='coerce')
country_stats = pd.DataFrame({'mean': chart_data.mean(axis=1),
                       'std': chart_data.std(axis=1)})

#render results
fig, ax = plt.subplots(figsize=(14, 6), dpi = 50)
ax.bar(countries, country_stats['mean'], yerr=country_stats['std'], capsize = 3)
ax.set_axisbelow(True)  #ensure the grid is under the graph elements
ax.margins(x=0.01) #set up the margin of graph
ax.grid(alpha = 0.3) #show the grid line
ax.set_xlabel('country')
ax.set_ylabel('emissions')
ax.set_title('The mean and std of emissions of countries')
xaxis = plt.xticks(rotation=90, ha='center', fontsize=8)
yaxis = plt.yticks(fontsize=8)

st.pyplot(fig)

st.subheader("draw chart using altair")

chart_data = data.drop(columns=['Non-OECD Economies'])
chart_data = pd.melt(chart_data, id_vars=['Country\year'], var_name='year')
chart_data['value'] = chart_data['value'].apply(pd.to_numeric, errors='coerce')
chart_data.rename(columns={"Country\year": "country", "value":"emission"}, inplace = True)
chart_data

#render using altair
heatmap = alt.Chart(chart_data).mark_rect().encode(
    x=alt.X('country:N', title = 'country'),
    y=alt.Y('year:O', title = 'year'),
    color='emission:Q',
    tooltip=['country', 'year', 'emission']
)

st.altair_chart(heatmap, use_container_width=True)

st.header("button")
#create a button
st.button("Click me for no reason")
 
# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome To CSE5544")

    
st.header("checkbox")
agree = st.checkbox('I agree')

if agree:
    st.write('Great!')


st.header("radio")
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")

st.header("selectbox")
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)

st.header("slider")
x = st.slider('x')  
st.write(x, 'squared is', x * x)


#create an interactive chart
st.header("an interactive chart")
countries = chart_data['country']
option = st.selectbox('select one country',countries)
filter_data = chart_data[chart_data['country'] == option]


bar_chart = alt.Chart(filter_data).mark_bar().encode(
    x='year',
    y='emission'
).properties(
    title=option
)

st.altair_chart(bar_chart, use_container_width=True)