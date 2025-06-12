import streamlit as st
from utils import convert_to_cm, calculate_cardboard_length, calculate_weight

def main():
    st.set_page_config(page_title="Cardboard Weight Calculator", page_icon="📦", layout="centered")
    st.markdown(
        """
        <style>
        .main {background-color: #f8fafc;}
        .stButton>button {
            background-color: #2563eb;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 2em;
            font-size: 1.1em;
        }
        .stNumberInput>div>input {
            background-color: #f1f5f9;
            border-radius: 6px;
            font-size: 1.1em;
        }
        .stSelectbox>div>div {
            background-color: #f1f5f9;
            border-radius: 6px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h1 style='text-align: center; color: #2563eb; margin-bottom:0;'>📦 Cardboard Weight Calculator for 3PLY and 5PLY/7PLY </h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #334155; font-size:1.1em;'>Enter your cardboard dimensions and GSM to calculate the size and weight.</p>", unsafe_allow_html=True)

    with st.form("cardboard_form"):
        st.markdown("#### Enter Dimensions")
        ply = st.selectbox("Select Cardboard Ply", ["3PLY", "5PLY", "7PLY"])

        col1, col2 = st.columns([2, 1])
        with col1:
            length = st.number_input("Length", key="length", format="%.2f")
        with col2:
            length_unit = st.selectbox("Unit", ["cm", "inches", "mm"], key="length_unit")

        col3, col4 = st.columns([2, 1])
        with col3:
            width = st.number_input("Width", key="width", format="%.2f")
        with col4:
            width_unit = st.selectbox("Unit", ["cm", "inches", "mm"], key="width_unit")

        col5, col6 = st.columns([2, 1])
        with col5:
            height = st.number_input("Height", key="height", format="%.2f")
        with col6:
            height_unit = st.selectbox("Unit", ["cm", "inches", "mm"], key="height_unit")

        st.markdown("#### Enter GSM")
        gsm = st.number_input("GSM (grams per square meter)", format="%.2f")

        submitted = st.form_submit_button("Calculate")

    if submitted:
        length_cm = convert_to_cm(length, length_unit)
        width_cm = convert_to_cm(width, width_unit)
        height_cm = convert_to_cm(height, height_unit)

        # Calculate extra based on ply
        if ply == "3PLY":
            extra1 = 3
            extra2 = 6
        else:  # 5PLY or 7PLY
            extra1 = 3
            extra2 = 12

        part1 = width_cm + height_cm + extra1
        part2 = (length_cm + width_cm) * 2 + extra2

        cardboard_length = part1 * part2
        weight = calculate_weight(cardboard_length, gsm)

        st.markdown(
            f"""
            <div style='background-color:#e0e7ff;padding:24px 16px 16px 16px;border-radius:12px;text-align:center;box-shadow:0 2px 8px #c7d2fe;'>
                <h2 style='color:#2563eb;margin-bottom:0.5em;'>Results</h2>
                <p style='color:#334155;font-size:1.1em;margin-bottom:0.5em;'>
                    <b>Cardboard Size:</b> {part1:.2f} cm × {part2:.2f} cm
                </p>
                <p style='color:#334155;font-size:1.1em;'>
                    <b>Total Weight:</b> {weight:.2f} grams
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    main()