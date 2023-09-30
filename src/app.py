"""
Script to build a streamlit app
"""

import streamlit as st

import pocket_client as pc


def GetPocketData(_p, n_items=10):
    """
    Function to manage data retrievel in a single step
    """
    access_token = p.makeLoginRequest()

    st.text("Access Done!")
    data = p.makeRequest(access_token=access_token, n_items=n_items)
    return data.json()


st.title("Pocket Articles to Obsidian")

data_load_state = st.text("Loading data ...")
p = pc.PocketClient()
data = GetPocketData(p, n_items=10)
data_load_state.text("Done!")
st.write(data)
