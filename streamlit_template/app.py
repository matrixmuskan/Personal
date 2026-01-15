import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Streamlit Demo App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🚀 Streamlit Demo Application")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("Configure your app settings here")
    
    chart_type = st.selectbox(
        "Select Chart Type",
        ["Line Chart", "Bar Chart", "Area Chart"]
    )
    
    num_points = st.slider(
        "Number of Data Points",
        min_value=10,
        max_value=100,
        value=50,
        step=10
    )
    
    show_data = st.checkbox("Show Raw Data", value=False)

# Main content
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Users",
        value="1,234",
        delta="12%"
    )

with col2:
    st.metric(
        label="Revenue",
        value="$56.7K",
        delta="-3%"
    )

with col3:
    st.metric(
        label="Conversion Rate",
        value="23.5%",
        delta="5%"
    )

st.markdown("---")

# Generate sample data
@st.cache_data
def generate_data(n_points):
    """Generate random data for visualization"""
    dates = pd.date_range(start='2024-01-01', periods=n_points, freq='D')
    data = pd.DataFrame({
        'Date': dates,
        'Sales': np.random.randn(n_points).cumsum() + 100,
        'Revenue': np.random.randn(n_points).cumsum() + 200,
        'Customers': np.random.randn(n_points).cumsum() + 150
    })
    return data

# Generate and display data
df = generate_data(num_points)

st.subheader(f"📊 {chart_type} Visualization")

# Display chart based on selection
if chart_type == "Line Chart":
    st.line_chart(df.set_index('Date')[['Sales', 'Revenue', 'Customers']])
elif chart_type == "Bar Chart":
    st.bar_chart(df.set_index('Date')[['Sales', 'Revenue', 'Customers']])
else:
    st.area_chart(df.set_index('Date')[['Sales', 'Revenue', 'Customers']])

# Show raw data if checkbox is selected
if show_data:
    st.subheader("📋 Raw Data")
    st.dataframe(df, use_container_width=True)

# Interactive input section
st.markdown("---")
st.subheader("💬 Interactive Demo")

col_a, col_b = st.columns(2)

with col_a:
    user_name = st.text_input("Enter your name:", placeholder="John Doe")
    user_age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)

with col_b:
    user_email = st.text_input("Enter your email:", placeholder="user@example.com")
    user_color = st.color_picker("Pick a color:", "#00f900")

if st.button("Submit", type="primary"):
    if user_name:
        st.success(f"✅ Hello {user_name}! Your favorite color is {user_color}")
        st.balloons()
    else:
        st.warning("⚠️ Please enter your name")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Built with ❤️ using Streamlit</p>
        <p>Last updated: {}</p>
    </div>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    unsafe_allow_html=True
)

