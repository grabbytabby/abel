import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="ABEL", page_icon="🏢", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .main {
        background: #ffffff;
        padding: 3rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        background-color: #f0f2f6;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Name', 'Profession', 'Company', 'Email', 'Phone', 'Rating'])

# Sidebar navigation
st.sidebar.image("https://placehold.co/200x100?text=ABEL+Logo", width=200)
st.sidebar.title("Main Menu")
selected = st.sidebar.radio("", ["Dashboard", "Add Entry", "Database", "Analytics", "ABEL D&B Direct for Finance", "Strategy & Advisory"])

# Main content
st.title("ABEL")
st.subheader("For Modern Agents, Brokers, Escrow, Lenders")

if selected == "Dashboard":
    st.header("Dashboard")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Entries", len(st.session_state.data))
    with col2:
        st.metric("Average Rating", f"{st.session_state.data['Rating'].mean():.2f}" if len(st.session_state.data) > 0 else "N/A")
    with col3:
        st.metric("Top Profession", st.session_state.data['Profession'].mode().values[0] if not st.session_state.data.empty else "N/A")
    
    st.subheader("Recent Entries")
    st.dataframe(st.session_state.data.tail(5))

if selected == "Add Entry":
    st.header("Add New Entry")
    with st.form("new_entry", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name")
            profession = st.selectbox("Profession", ["Agent", "Broker", "Escrow Officer", "Lender"])
            company = st.text_input("Company")
        with col2:
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            rating = st.slider("Rating", 1, 5, 3)
        
        submitted = st.form_submit_button("Add Entry")
        if submitted:
            new_entry = pd.DataFrame({
                'Name': [name], 'Profession': [profession], 'Company': [company],
                'Email': [email], 'Phone': [phone], 'Rating': [rating]
            })
            st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)
            st.success("Entry added successfully!")

if selected == "Database":
    st.header("Database")
    st.dataframe(st.session_state.data)
    
    if not st.session_state.data.empty:
        csv = st.session_state.data.to_csv(index=False)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name="abel_database.csv",
            mime="text/csv",
        )

if selected == "Analytics":
    st.header("Analytics")
    if not st.session_state.data.empty:
        fig1 = px.pie(st.session_state.data, names='Profession', title='Distribution of Professions')
        st.plotly_chart(fig1)
        
        fig2 = px.histogram(st.session_state.data, x='Rating', title='Distribution of Ratings')
        st.plotly_chart(fig2)
    else:
        st.info("No data available for analytics. Please add some entries.")

if selected == "ABEL D&B Direct for Finance":
    st.header("ABEL D&B Direct for Finance")
    st.subheader("The only payments platform designed for money movement at scale.")

    st.write("""
    ABEL D&B Direct for Finance provides real-time access to ABEL's industry-leading data and analytical insights, 
    seamlessly integrated into your applications and workflows. Leverage our powerful API to make faster, 
    more informed financial decisions and drive growth for your business.
    """)

    st.button("Get Started")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Strategic Expertise for Faster Outcomes")
        st.write("Implementation & Optimization:")
        st.write("• Optimize fund flows for revenue, efficiency, and customer experience")
        st.write("• Design tailored chart of accounts for ledgering systems")
        st.write("• Automate reconciliation and refine rules over time")

        st.subheader("Managed Services & Support")
        st.write("• Premium support for customers with stringent needs")
        st.write("• Retained solutions architecture")
        st.write("• Custom integrations with internal IT systems, banks, card processors, and ERPs")

    with col2:
        st.subheader("Key Features")
        st.write("1. Easy API Integration")
        st.write("2. Real-time Data Access")
        st.write("3. AI-Powered Insights")

        st.subheader("Benefits")
        st.write("• Streamline credit decisioning processes")
        st.write("• Enhance risk management capabilities")
        st.write("• Improve operational efficiency")
        st.write("• Make data-driven financial decisions")
        st.write("• Stay compliant with regulatory requirements")

    with st.form("contact_form"):
        st.subheader("Ready to get started?")
        name = st.text_input("Name")
        email = st.text_input("Email")
        company = st.text_input("Company")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thank you for your interest. We'll be in touch soon!")

if selected == "Strategy & Advisory":
    st.header("Strategy & Advisory Services")
    st.subheader("Expert guidance for optimizing your financial operations")

    st.write("""
    Our Strategy & Advisory services leverage deep industry expertise to help you 
    optimize your financial processes and plan for future growth.
    """)

    st.image("https://placehold.co/600x300?text=Strategy+&+Advisory", use_column_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Key Services")
        st.write("• Discover gains in automating real-time payments, ledgering, and reconciliation")
        st.write("• Leverage unparalleled expertise when roadmapping future needs")
        st.write("• Optimize fund flows for revenue, efficiency, and customer experience")
        st.write("• Design tailored chart of accounts for ledgering systems")

    with col2:
        st.subheader("Benefits")
        st.write("• Streamline financial operations")
        st.write("• Reduce costs and increase efficiency")
        st.write("• Stay ahead of industry trends")
        st.write("• Make data-driven strategic decisions")
        st.write("• Prepare for future growth and challenges")

    st.subheader("Our Approach")
    st.write("""
    1. **Assessment**: We begin by thoroughly analyzing your current financial processes and systems.
    2. **Strategy Development**: Our experts work with you to create a tailored strategy that aligns with your business goals.
    3. **Implementation Planning**: We provide a detailed roadmap for implementing recommended changes and improvements.
    4. **Ongoing Support**: Our team offers continuous guidance and support as you execute your strategic plan.
    """)

    with st.form("consultation_form"):
        st.subheader("Request a Consultation")
        name = st.text_input("Name")
        email = st.text_input("Email")
        company = st.text_input("Company")
        specific_needs = st.text_area("Please describe your specific needs or challenges")
        submitted = st.form_submit_button("Submit Request")
        if submitted:
            st.success("Thank you for your interest in our Strategy & Advisory services. We'll be in touch soon to schedule your consultation.")

# Footer
st.markdown("---")
st.markdown("© 2024 ABEL. All rights reserved.")