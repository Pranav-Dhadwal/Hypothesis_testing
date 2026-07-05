import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar(data, col):
    fig, ax = plt.subplots(figsize=(8,5))

    sns.countplot(data=data, x=col, ax=ax)

    ax.set_title(f"Distribution of {col.replace('_', ' ').title()}")
    ax.set_xlabel(col.replace('_', ' ').title())
    ax.set_ylabel("Count")

    ax.bar_label(ax.containers[0], padding=3)

    plt.xticks(rotation=45)
    plt.tight_layout()
    sns.despine()
    st.pyplot(fig)

def plot_pie(data, col):
    fig, ax = plt.subplots(figsize=(7,7))
    data[col].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    ax.set_title(f"{col.replace('_',' ').title()} Distribution")
    sns.despine()
    st.pyplot(fig)

def plot_histogram(data, col, bins=20):
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(data=data, x=col, bins=bins, kde=True, ax=ax)
    ax.set_title(f"Distribution of {col.replace('_', ' ').title()}")
    ax.set_xlabel(col.replace('_', ' ').title())
    ax.set_ylabel("Frequency")

    plt.tight_layout()
    sns.despine()
    st.pyplot(fig)

def plot_boxplot(data, x, y):
    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(data=data, x=x, y=y, ax=ax)
    plt.xticks(rotation=45)
    ax.set_title(
    f"{y.replace('_',' ').title()} by {x.replace('_',' ').title()}"
    )

    ax.set_xlabel(x.replace('_',' ').title())
    ax.set_ylabel(y.replace('_',' ').title())

    plt.tight_layout()
    sns.despine()
    st.pyplot(fig)

def plot_scatter(data, x, y, hue=None):
    fig, ax = plt.subplots(figsize=(8,5))
    if hue:
        sns.scatterplot(data=data, x=x, y=y, hue=hue, ax=ax)
    else:
        sns.scatterplot(data=data, x=x, y=y, ax=ax)
        ax.set_title(
    f"{y.replace('_',' ').title()} vs {x.replace('_',' ').title()}"
    )

    ax.set_xlabel(x.replace('_',' ').title())
    ax.set_ylabel(y.replace('_',' ').title())

    plt.tight_layout()
    sns.despine()
    st.pyplot(fig)

def plot_line(data, x, y):
    fig, ax = plt.subplots(figsize=(8,5))
    sns.lineplot(data=data, x=x, y=y, ax=ax)
    ax.set_title(
    f"{y.replace('_',' ').title()} over {x.replace('_',' ').title()}"
    )

    ax.set_xlabel(x.replace('_',' ').title())
    ax.set_ylabel(y.replace('_',' ').title())

    plt.tight_layout()
    sns.despine()
    st.pyplot(fig)
