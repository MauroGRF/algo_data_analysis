import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  # pyplot mantiene estado global de la figura.
# plt.subplots() devuelve (fig, ax). Se grafica sobre ax y se muestra con st.pyplot(fig).

def main():

    data = pd.read_csv("GoogleApps.csv")

    """1. Mostrar el DataFrame completo de forma interactiva"""
    st.subheader("DataFrame interactivo")
    st.dataframe(data)

    """2. Mostrar las primeras filas como tabla estatica"""
    st.subheader("DataFrame estatico (head)")
    st.table(data.head(10))

    """3. Grafico de barras: cantidad de apps por categoria"""
    # value_counts() cuenta frecuencias y .plot.bar() las grafica
    st.subheader("Apps por categoria")
    fig, ax = plt.subplots()
    data["Category"].value_counts().plot.bar(ax=ax)
    st.pyplot(fig)

    """4. Histograma: distribucion de la columna Rating"""
    # .plot.hist() agrupa los valores en bins para ver la frecuencia
    st.subheader("Distribucion de Rating")
    fig, ax = plt.subplots()
    data["Rating"].plot.hist(bins=20, ax=ax)
    st.pyplot(fig)

    """5. Boxplot: comparar distribuciones de Rating segun Type (Free/Paid)"""
    # boxplot muestra mediana, cuartiles y outliers por grupo
    st.subheader("Rating por tipo (boxplot)")
    fig, ax = plt.subplots()
    data.boxplot(column="Rating", by="Type", ax=ax)
    st.pyplot(fig)

    """6. Scatter plot: relacion entre Size y Rating"""
    # .plot.scatter() muestra la correlacion entre dos variables numericas
    st.subheader("Relacion Size vs Rating")
    fig, ax = plt.subplots()
    data.plot.scatter(x="Size", y="Rating", alpha=0.5, ax=ax)
    st.pyplot(fig)

    """7. Grafico de torta: proporcion de cada Content Rating"""
    # value_counts().plot.pie() con autopct para porcentajes
    st.subheader("Proporcion de Content Rating")
    fig, ax = plt.subplots()
    data["Content Rating"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
    st.pyplot(fig)

    """8. Grafico de lineas: Rating promedio por categoria (ordenado)"""
    # groupby().mean() agrupa y promedia, sort_values() ordena ascendente
    st.subheader("Rating promedio por categoria")
    fig, ax = plt.subplots()
    data.groupby("Category")["Rating"].mean().sort_values().plot.line(ax=ax)
    st.pyplot(fig)

    """9. Heatmap: tabla dinamica (pivot table) de Reviews promedio"""
    # pivot_table cruza dos categorias con un agregado; imshow lo colorea
    st.subheader("Reviews promedio (pivot table heatmap)")
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
    st.subheader("Installs promedio por tipo")
    fig, ax = plt.subplots()
    data.groupby("Type")["Installs"].mean().plot.barh(ax=ax)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
