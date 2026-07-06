import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Customer demographics 
def plot_customer_demographics(data):

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    sns.countplot(data=data, x="gender", ax=axes[0])

    axes[0].set_title("Customer Distribution by Gender")
    axes[0].set_xlabel("Gender")
    axes[0].set_ylabel("Customers")
    axes[0].bar_label(axes[0].containers[0])

    sns.countplot(data=data, x="country", ax=axes[1])

    axes[1].set_title("Customer Distribution by Country")
    axes[1].set_xlabel("Country")
    axes[1].set_ylabel("Customers")

    axes[1].tick_params(axis="x", rotation=25)
    axes[1].bar_label(axes[1].containers[0])

    plt.tight_layout()
    st.pyplot(fig)

# Customer Behaviour 
def plot_customer_behaviour(data):

    fig, axes = plt.subplots(1, 2, figsize=(14,5))

    sns.countplot(
        data=data,
        x="device",
        ax=axes[0]
    )

    axes[0].set_title("Browsing Device")
    axes[0].bar_label(axes[0].containers[0])

    sns.countplot(
        data=data,
        x="traffic_source",
        ax=axes[1]
    )

    axes[1].set_title("Traffic Source")
    axes[1].tick_params(axis="x", rotation=25)
    axes[1].bar_label(axes[1].containers[0])

    plt.tight_layout()
    st.pyplot(fig)

# Customer Engagement 
def plot_customer_engagement(data):

    fig, axes = plt.subplots(1,3, figsize=(18,5))

    sns.histplot(
        data=data,
        x="session_duration",
        kde=True,
        ax=axes[0]
    )

    axes[0].set_title("Session Duration")

    sns.histplot(
        data=data,
        x="pages_viewed",
        kde=True,
        ax=axes[1]
    )

    axes[1].set_title("Pages Viewed")

    sns.histplot(
        data=data,
        x="previous_orders",
        kde=True,
        ax=axes[2]
    )

    axes[2].set_title("Previous Orders")

    plt.tight_layout()

    st.pyplot(fig)


# Experiment overview 
def plot_experiment_overview(data):

    fig, axes = plt.subplots(1,2, figsize=(14,5))

    sns.boxplot(
        data=data,
        x="experiment_group",
        y="purchase_prob",
        ax=axes[0]
    )

    axes[0].set_title("Purchase Probability by Group")

    sns.barplot(
        data=data,
        x="experiment_group",
        y="purchase_prob",
        estimator="mean",
        errorbar=None,
        ax=axes[1]
    )

    axes[1].set_title("Average Purchase Probability")

    for container in axes[1].containers:
        axes[1].bar_label(container, fmt="%.3f")

    plt.tight_layout()

    st.pyplot(fig)

# Correlation 
def plot_correlation(data):
    fig, ax = plt.subplots(figsize=(8, 6))

    corr = data.select_dtypes(include="number").corr()

    sns.heatmap(
        corr,
        annot=True,
        cmap="Blues",
        fmt=".2f",
        linewidths=.5,
        ax=ax
    )

    ax.set_title("Correlation Between Numerical Features")

    plt.tight_layout()
    st.pyplot(fig)

    
# interactive visualizatoin part 
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
