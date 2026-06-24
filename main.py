import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  # pyplot mantiene estado global de la figura.
# plt.subplots() devuelve (fig, ax). Se grafica sobre ax y se muestra con st.pyplot(fig).

def main():

    data = pd.read_csv("GoogleApps.csv")

    """1. Mostrar el DataFrame completo de forma interactiva"""
    st.markdown("<h3 style='color:#E63946;'>DataFrame interactivo</h3>", unsafe_allow_html=True)
    st.dataframe(data)

    """2. Mostrar las primeras filas como tabla estatica"""
    st.markdown("<h3 style='color:#457B9D;'>DataFrame estatico (head)</h3>", unsafe_allow_html=True)
    st.table(data.head(10))

    """3. Grafico de barras: cantidad de apps por categoria"""
    # value_counts() cuenta frecuencias y .plot.bar() las grafica
    st.markdown("<h3 style='color:#2A9D8F;'>Apps por categoria</h3>", unsafe_allow_html=True)
    fig, ax = plt.subplots()
    data["Category"].value_counts().plot.bar(ax=ax)
    st.pyplot(fig)

    """4. Histograma: distribucion de la columna Rating"""
    # .plot.hist() agrupa los valores en bins para ver la frecuencia
    st.markdown("<h3 style='color:#E76F51;'>Distribucion de Rating</h3>", unsafe_allow_html=True)
    fig, ax = plt.subplots()
    data["Rating"].plot.hist(bins=20, ax=ax)
    st.pyplot(fig)

    """5. Boxplot: comparar distribuciones de Rating segun Type (Free/Paid)"""
    # boxplot muestra mediana, cuartiles y outliers por grupo
    st.markdown("<h3 style='color:#8338EC;'>Rating por tipo (boxplot)</h3>", unsafe_allow_html=True)
    fig, ax = plt.subplots()
    data.boxplot(column="Rating", by="Type", ax=ax)
    st.pyplot(fig)

    """6. Scatter plot: relacion entre Size y Rating"""
    # .plot.scatter() muestra la correlacion entre dos variables numericas
    st.markdown("<h3 style='color:#FFBE0B;'>Relacion Size vs Rating</h3>", unsafe_allow_html=True)
    fig, ax = plt.subplots()
    data.plot.scatter(x="Size", y="Rating", alpha=0.5, ax=ax)
    st.pyplot(fig)

    """7. Grafico de torta: proporcion de cada Content Rating"""
    # value_counts().plot.pie() con autopct para porcentajes
    st.markdown("<h3 style='color:#FB5607;'>Proporcion de Content Rating</h3>", unsafe_allow_html=True)
    fig, ax = plt.subplots()
    data["Content Rating"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
    st.pyplot(fig)

    """8. Grafico de lineas: Rating promedio por categoria (ordenado)"""
    # groupby().mean() agrupa y promedia, sort_values() ordena ascendente
    st.markdown("<h3 style='color:#3A86FF;'>Rating promedio por categoria</h3>", unsafe_allow_html=True)
    fig, ax = plt.subplots()
    data.groupby("Category")["Rating"].mean().sort_values().plot.line(ax=ax)
    st.pyplot(fig)

    """9. Heatmap: tabla dinamica (pivot table) de Reviews promedio"""
    # pivot_table cruza dos categorias con un agregado; imshow lo colorea
    st.markdown("<h3 style='color:#9C89B8;'>Reviews promedio (pivot table heatmap)</h3>", unsafe_allow_html=True)
    pivot = data.pivot_table(index="Content Rating", columns="Category",
                             values="Reviews", aggfunc="mean")
    fig, ax = plt.subplots(figsize=(10, 6))
    im = ax.imshow(pivot.values, cmap="YlOrRd", aspect="auto")
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels(pivot.columns, rotation=90)
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)
    st.pyplot(fig)

    """10. Barras horizontales: promedio de Installs por tipo"""
    # groupby().mean() y .barh() para barras horizontales
    st.markdown("<h3 style='color:#06D6A0;'>Installs promedio por tipo</h3>", unsafe_allow_html=True)
    fig, ax = plt.subplots()
    data.groupby("Type")["Installs"].mean().plot.barh(ax=ax)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
