import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Restaurant Order Analytics",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* ---------------------------------------------------------
   MAIN APP BACKGROUND
--------------------------------------------------------- */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(255, 213, 170, 0.45),
            transparent 32%
        ),
        radial-gradient(
            circle at 90% 90%,
            rgba(255, 230, 195, 0.55),
            transparent 32%
        ),
        linear-gradient(
            135deg,
            #fffaf5 0%,
            #fff4e9 50%,
            #fffaf5 100%
        );
}


/* ---------------------------------------------------------
   MAIN CONTAINER
--------------------------------------------------------- */

.block-container {
    max-width: 1150px;
    padding-top: 45px;
    padding-bottom: 35px;
}


/* ---------------------------------------------------------
   PROJECT TITLE
--------------------------------------------------------- */

.project-title {
    text-align: center;
    font-size: 40px;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 10px;
    color: #2b2118;
}


/* ---------------------------------------------------------
   PROJECT DESCRIPTION
--------------------------------------------------------- */

.project-description {
    text-align: center;
    font-size: 17px;
    color: #6f6258;
    margin-bottom: 25px;
}


/* ---------------------------------------------------------
   SECTION LABEL
--------------------------------------------------------- */

.section-label {
    text-align: center;
    font-size: 15px;
    font-weight: 600;
    color: #8a6a52;
    letter-spacing: 0.5px;
    margin-top: 10px;
    margin-bottom: 18px;
}


/* ---------------------------------------------------------
   ALGORITHM CARDS
--------------------------------------------------------- */

.algorithm-card {
    background: rgba(255, 255, 255, 0.94);
    border-radius: 20px;
    padding: 28px 24px 22px 24px;
    text-align: center;
    min-height: 175px;

    box-shadow:
        0 8px 25px rgba(75, 45, 20, 0.08);

    border: 1px solid rgba(220, 195, 170, 0.55);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}


/* ---------------------------------------------------------
   ALGORITHM ICON
--------------------------------------------------------- */

.algorithm-icon {
    font-size: 43px;
    margin-bottom: 5px;
}


/* ---------------------------------------------------------
   ALGORITHM TITLE
--------------------------------------------------------- */

.algorithm-title {
    font-size: 25px;
    font-weight: 750;
    color: #2f241c;
    margin-top: 5px;
}


/* ---------------------------------------------------------
   ALGORITHM DESCRIPTION
--------------------------------------------------------- */

.algorithm-description {
    font-size: 15px;
    color: #74665b;
    margin-top: 8px;
    line-height: 1.5;
}


/* ---------------------------------------------------------
   SMALL ALGORITHM BUTTONS
--------------------------------------------------------- */

.stButton {
    display: flex;
    justify-content: center;
    margin-top: 15px;
}

.stButton > button {
    width: 72%;
    height: 45px;

    border-radius: 11px;

    background: #C65D2E;
    color: #FFFFFF;

    border: 1px solid #B84F23;

    font-size: 15px;
    font-weight: 650;

    box-shadow:
        0 4px 10px rgba(150, 65, 30, 0.20);

    transition:
        background 0.2s ease,
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

.stButton > button:hover {
    background: #A94C25;
    color: #FFFFFF;

    border-color: #A94C25;

    transform: translateY(-2px);

    box-shadow:
        0 6px 15px rgba(150, 65, 30, 0.28);
}


/* ---------------------------------------------------------
   RESULT HEADING
--------------------------------------------------------- */

.result-heading {
    font-size: 29px;
    font-weight: 800;
    color: #2f241c;
    margin-top: 12px;
    margin-bottom: 8px;
}


/* ---------------------------------------------------------
   RESULT DESCRIPTION
--------------------------------------------------------- */

.result-description {
    color: #6f6258;
    font-size: 16px;
    margin-bottom: 20px;
}


/* ---------------------------------------------------------
   METRIC CARDS
--------------------------------------------------------- */

[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.94);

    padding: 18px;

    border-radius: 15px;

    border: 1px solid rgba(220, 195, 170, 0.5);

    box-shadow:
        0 4px 15px rgba(75, 45, 20, 0.06);
}


/* ---------------------------------------------------------
   SUBHEADINGS
--------------------------------------------------------- */

h2, h3 {
    color: #38291f !important;
}


/* ---------------------------------------------------------
   STREAMLIT TEXT VISIBILITY
--------------------------------------------------------- */

[data-testid="stMetric"] * {
    color: #38291f !important;
}

[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    color: #38291f !important;
}


/* ---------------------------------------------------------
   KEY INSIGHT TEXT
--------------------------------------------------------- */

.key-insight {
    color: #4a3528 !important;
}

.key-insight strong {
    color: #2f241c !important;
}


/* ---------------------------------------------------------
   DATAFRAME
--------------------------------------------------------- */

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}


/* ---------------------------------------------------------
   FOOTER
--------------------------------------------------------- */

.footer {
    text-align: center;
    font-size: 13px;
    color: #8a7a6c;
    margin-top: 30px;
    line-height: 1.7;
}


/* ---------------------------------------------------------
   MOBILE RESPONSIVENESS
--------------------------------------------------------- */

@media (max-width: 768px) {

    .project-title {
        font-size: 28px;
        white-space: normal;
    }

    .project-description {
        font-size: 15px;
    }

    .algorithm-card {
        min-height: auto;
        padding: 22px;
    }

    .algorithm-title {
        font-size: 22px;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

kmeans_results = pd.read_csv(
    "data/kmeans_customer_results.csv"
)

cluster_summary = pd.read_csv(
    "data/kmeans_cluster_summary.csv"
)

frequent_itemsets = pd.read_csv(
    "data/apriori_frequent_itemsets.csv"
)

association_rules = pd.read_csv(
    "data/apriori_association_rules.csv"
)


# ============================================================
# PROJECT HEADER
# ============================================================

st.markdown(
    """
    <div class="project-title">
        🍽️ Restaurant Order Analytics & Food Pattern Mining System
    </div>

    <div class="project-description">
        Data-Driven Insights into Customer Behavior and Food Purchasing Patterns
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# ALGORITHM SELECTION
# ============================================================

st.markdown(
    """
    <div class="section-label">
        SELECT AN ALGORITHM TO EXPLORE THE ANALYSIS
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap="large")


# ============================================================
# K-MEANS CARD
# ============================================================

with col1:

    st.markdown(
        """
        <div class="algorithm-card">
            <div class="algorithm-icon">👥</div>
            <div class="algorithm-title">K-Means</div>
            <div class="algorithm-description">
                Groups customers with similar purchasing behavior
                into meaningful segments.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    kmeans_button = st.button(
        "View K-Means Results →",
        key="kmeans",
        width="stretch"
    )


# ============================================================
# APRIORI CARD
# ============================================================

with col2:

    st.markdown(
        """
        <div class="algorithm-card">
            <div class="algorithm-icon">🍔</div>
            <div class="algorithm-title">Apriori</div>
            <div class="algorithm-description">
                Discovers frequently purchased food combinations
                and meaningful association rules.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    apriori_button = st.button(
        "View Apriori Results →",
        key="apriori",
        width="stretch"
    )


# ============================================================
# K-MEANS RESULTS
# ============================================================

if kmeans_button:

    st.divider()

    st.markdown(
        """
        <div class="result-heading">
            👥 K-Means Customer Segmentation
        </div>

        <div class="result-description">
            Customers are grouped according to similarities
            in their purchasing behavior.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="key-insight" style="
            background: rgba(255, 255, 255, 0.85);
            border-left: 5px solid #C65D2E;
            padding: 16px 20px;
            border-radius: 10px;
            margin: 18px 0 25px 0;
            box-shadow: 0 3px 12px rgba(75, 45, 20, 0.06);
        ">
            <strong>💡 Key Insight</strong><br>
            Cluster 0 represents customers with higher average
            order frequency and spending, while Cluster 1 represents
            customers with comparatively lower purchasing activity.
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Number of Clusters",
            kmeans_results["cluster"].nunique()
        )

    with col2:

        st.metric(
            "Customers Segmented",
            len(kmeans_results)
        )

    # --------------------------------------------------------
    # CLUSTER SUMMARY
    # --------------------------------------------------------

    st.subheader("📊 Cluster Summary")

    st.dataframe(
        cluster_summary,
        width="stretch",
        hide_index=True
    )

    # --------------------------------------------------------
    # VISUALIZATION
    # --------------------------------------------------------

    st.subheader("📈 Customer Segmentation")

    plot_data = kmeans_results.copy()

    plot_data["cluster"] = (
        plot_data["cluster"]
        .astype(str)
        .apply(lambda x: f"Cluster {x}")
    )

    fig = px.scatter(
        plot_data,
        x="total_orders",
        y="total_spending",
        color="cluster",

        # Fixed colors for deployment consistency
        color_discrete_sequence=[
            "#C65D2E",
            "#8A6A52"
        ],

        hover_data=[
            "Customer_ID",
            "avg_order_value",
            "total_quantity",
            "avg_rating"
        ],

        labels={
            "total_orders": "Total Orders",
            "total_spending": "Total Spending",
            "cluster": "Customer Cluster"
        },

        title="Customer Segmentation: Orders vs Spending"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(
            color="#3b3028"
        ),
        title_x=0.5
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


# ============================================================
# APRIORI RESULTS
# ============================================================

if apriori_button:

    st.divider()

    st.markdown(
        """
        <div class="result-heading">
            🍔 Apriori Food Pattern Mining
        </div>

        <div class="result-description">
            Frequently purchased food combinations and
            association rules are identified from transaction data.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="key-insight" style="
            background: rgba(255, 255, 255, 0.85);
            border-left: 5px solid #C65D2E;
            padding: 16px 20px;
            border-radius: 10px;
            margin: 18px 0 25px 0;
            box-shadow: 0 3px 12px rgba(75, 45, 20, 0.06);
        ">
            <strong>💡 Key Insight</strong><br>
            The association rules reveal recurring food purchasing
            patterns. Rules with higher lift indicate stronger
            associations between the purchased items.
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Frequent Itemsets",
            len(frequent_itemsets)
        )

    with col2:

        st.metric(
            "Association Rules",
            len(association_rules)
        )

    # --------------------------------------------------------
    # TOP RULES
    # --------------------------------------------------------

    st.subheader("⭐ Top Association Rules")

    display_columns = [
        "antecedents",
        "consequents",
        "support",
        "confidence",
        "lift"
    ]

    available_columns = [
        column
        for column in display_columns
        if column in association_rules.columns
    ]

    top_rules = (
        association_rules[available_columns]
        .sort_values(
            "lift",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        top_rules,
        width="stretch",
        hide_index=True
    )

    # --------------------------------------------------------
    # VISUALIZATION
    # --------------------------------------------------------

    st.subheader("📈 Association Rule Visualization")

    fig = px.scatter(
        association_rules,
        x="support",
        y="confidence",
        size="lift",

        # Fixed color for deployment consistency
        color_discrete_sequence=["#C65D2E"],

        hover_data=[
            "antecedents",
            "consequents",
            "lift"
        ],

        title="Support vs Confidence"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(
            color="#3b3028"
        ),
        title_x=0.5
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    '<div class="footer">'
    'Restaurant Order Analytics & Food Pattern Mining System'
    '<br>'
    'K-Means Customer Segmentation &nbsp; • &nbsp; Apriori Association Mining'
    '</div>',
    unsafe_allow_html=True
)