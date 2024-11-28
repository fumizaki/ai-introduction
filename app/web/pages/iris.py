import streamlit as st

from components.iris.table.dataframe import render_dataframe

def render_page() -> None:
    st.title("Iris")
    
    tab1, tab2, tab3 = st.tabs(["Table", "Plot", "Summary"])
    
    with tab1:
        render_dataframe()
        
    with tab2:
        st.write("Plot")
        
    with tab3:
        st.write("Summary")
    
    
if __name__ == "__main__":
    render_page()