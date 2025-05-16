
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

st.set_page_config(page_title="GENEWISE Pedigree Builder", layout="wide")

st.title("🧬 GENEWISE Pedigree Chart Builder")

st.markdown("Enter family data below and generate a pedigree chart.")

# Input table
default_data = pd.DataFrame({
    'Name': ['Grandfather', 'Grandmother', 'Father', 'Mother', 'Proband', 'Sibling'],
    'Relationship': ['Paternal Grandfather', 'Paternal Grandmother', 'Father', 'Mother', 'Self', 'Sibling'],
    'Sex': ['M', 'F', 'M', 'F', 'F', 'M'],
    'Affected': [False, False, False, False, True, False],
    'X': [1, 3, 2, 5, 3.5, 2],
    'Y': [3, 3, 2, 2, 1, 1]
})

df = st.data_editor(default_data, num_rows="dynamic", use_container_width=True)

# Button to generate chart
if st.button("Generate Pedigree Chart"):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 4)
    ax.axis('off')

    for _, row in df.iterrows():
        name, relationship, sex, affected, x, y = row
        color = 'black' if affected else 'white'
        edgecolor = 'black'
        if sex == 'M':
            shape = plt.Rectangle((x-0.2, y-0.2), 0.4, 0.4, edgecolor=edgecolor, facecolor=color, fill=True)
        else:
            shape = plt.Circle((x, y), 0.2, edgecolor=edgecolor, facecolor=color, fill=True)
        ax.add_patch(shape)
        ax.text(x, y-0.35, name, ha='center', fontsize=8)
        if relationship == "Self":
            ax.annotate("→", (x+0.3, y), fontsize=12, ha='left')

    st.pyplot(fig)
    st.success("Pedigree chart generated!")
