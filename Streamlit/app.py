import streamlit as st
import requests
import pandas as pd

data = pd.read_csv("../data/Cleaned_Data.csv")
locations = sorted(data["Location"].unique())
status = sorted(data["Status"].unique())
ownership = sorted(data["Ownership"].unique())
payment_methods = sorted(data["Payment"].unique())

st.set_page_config(
    page_title="Real Estate AI",
    page_icon="🏠",
    layout="wide"
)
st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #2E86C1;
    text-align: center;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 15px;
}

.section-title {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="main-title">🏠 Price prediction for Apartments in 5th Settlement, New Cairo</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Predict apartment prices instantly using Machine Learning</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🏠 Property Info</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (sqm)", value=100.0)
    bedrooms = st.number_input("Bedrooms", value=3)

with col2:
    bathrooms = st.number_input("Bathrooms", value=2)
    location = st.selectbox("Location", locations)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🧾 Transaction</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    payment = st.selectbox("Payment", payment_methods)
    ownership = st.selectbox("Ownership", ownership)

with col2:
    status = st.selectbox("Status", status)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">⚙️ Amenities</div>', unsafe_allow_html=True)

def toggle(label):
    return int(st.toggle(label))

col1, col2, col3 = st.columns(3)

with col1:
    pool = toggle("Pool")
    garden = toggle("Private Garden")
    security = toggle("Security")

with col2:
    electricity = toggle("Electricity Meter")
    water = toggle("Water Meter")
    gas = toggle("Natural Gas")

with col3:
    parking = toggle("Covered Parking")
    landline = toggle("Landline")
    balcony = toggle("Balcony")

st.markdown('</div>', unsafe_allow_html=True)


if st.button('Predict Price'):
    data = {
        "Area": area,
        "Payment": payment,
        "Ownership": ownership,
        "Status": status,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Location": location,
        "Pool": pool,
        "Electricity_Meter": electricity,
        "Water_Meter": water,
        "Natural_Gas": gas,
        "PrivateGarden": garden,
        "Landline": landline,
        "Covered_Parking": parking,
        "Security": security,
        "Balcony": balcony
    }
    url = "http://127.0.0.1:8000/predict"
    try:
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            prediction = response.json()["predicted_price"]
            st.success(f"Predicted Price: {prediction:,.2f}")
        else:
            st.error(f"Error: {response.text}")

    except Exception as e:
        st.error(f"API connection error: {e}")


