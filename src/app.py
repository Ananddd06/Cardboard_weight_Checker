import streamlit as st
from utils import convert_to_cm, calculate_cardboard_length, calculate_weight
import pandas as pd
import os

EXCEL_FILE = "cardboard_data.xlsx"

def append_to_excel(data, filename=EXCEL_FILE):
    df_new = pd.DataFrame([data])
    if os.path.exists(filename):
        df_existing = pd.read_excel(filename)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new
    df_combined.to_excel(filename, index=False)

def reset_excel(filename=EXCEL_FILE):
    if os.path.exists(filename):
        os.remove(filename)

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
        @media (max-width: 600px) {
            .stColumns {
                flex-direction: row !important;
                gap: 0.25rem !important;
            }
            .stNumberInput, .stSelectbox {
                width: 100% !important;
            }
            .stButton>button {
                width: 100%;
                font-size: 1.1em;
            }
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

        # Length
        col1, col2 = st.columns([3, 1], gap="small")
        with col1:
            length = st.number_input("Length", key="length", format="%.2f")
        with col2:
            length_unit = st.selectbox("Unit", ["cm", "inches", "mm"], key="length_unit")

        # Width
        col3, col4 = st.columns([3, 1], gap="small")
        with col3:
            width = st.number_input("Width", key="width", format="%.2f")
        with col4:
            width_unit = st.selectbox("Unit", ["cm", "inches", "mm"], key="width_unit")

        # Height
        col5, col6 = st.columns([3, 1], gap="small")
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

        if ply == "3PLY":
            extra1 = 3
            extra2 = 6
        else:
            extra1 = 3
            extra2 = 12

        part1 = width_cm + height_cm + extra1
        part2 = (length_cm + width_cm) * 2 + extra2

        cardboard_length = part1 * part2
        weight = calculate_weight(cardboard_length, gsm)

        data = {
            "Length": f"{length:.2f} cm",
            "Width": f"{width:.2f} cm",
            "Height": f"{height:.2f} cm",
            "GSM": gsm,
            "Ply": ply,
            "Cardboard Length (cm)": f"{part1:.2f} cm",
            "Cardboard Breadth (cm)": f"{part2:.2f} cm",
            "Cardboard Size": f"{part1:.2f} cm × {part2:.2f} cm",
            "Total Weight (grams)": f"{weight:.2f} grams"
        }
        append_to_excel(data)

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

    # Show and allow download of the Excel file
    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE)
        st.markdown("### Submission History")
        st.markdown(
            """
            <div style='color:#334155; font-size:1.05em; margin-bottom:1em;'>
                Below is your Excel database. You can store up to <b>500 entries</b> in a single file.<br>
                <ul>
                    <li>To <b>delete</b> a row, enter its row number and click <b>Delete Selected Row</b>.</li>
                    <li>To <b>download</b> the current database, use the <b>Download Current Excel</b> button below the table (right side).</li>
                    <li>To <b>export and reset</b> the database, use the <b>Export & Reset</b> button at the bottom.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<h2 style='text-align:center; color:#2563eb;'>Weight Calculator</h2>", unsafe_allow_html=True)
        st.dataframe(df)

        with open(EXCEL_FILE, "rb") as f:
            st.download_button(
                "Download Current Excel",
                f,
                file_name="cardboard_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )


        # --- Delete Row Feature ---
        st.markdown("#### Delete a Row")
        if not df.empty:
            row_to_delete = st.number_input(
                "Enter the row number to delete (starting from 0):",
                min_value=0, max_value=len(df)-1, step=1, format="%d"
            )
            if st.button("Delete Selected Row"):
                df = df.drop(df.index[row_to_delete]).reset_index(drop=True)
                df.to_excel(EXCEL_FILE, index=False)
                st.success(f"Row {row_to_delete} deleted.")
                st.experimental_rerun()

        # Download Excel file (always as .xlsx)
        # Export & Reset button
        if st.button("Export & Reset"):
            with open(EXCEL_FILE, "rb") as f:
                st.download_button(
                    "Download and Reset",
                    f,
                    file_name="exported_cardboard_data.xlsx",
                    key="export_reset",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            reset_excel()
            st.success("Excel file exported and reset for new batch!")

if __name__ == "__main__":
    main()