import pulp
import pandas as pd
import streamlit as st
from service.project_member_assignment import AssignmentUsecase

def render_page() -> None:
    st.title("Project Member Assignment")
    usecase = AssignmentUsecase()
    result = usecase.exec()

    # # DataFrame に変換
    df = pd.DataFrame(result)

    # # Streamlitで表示
    st.title("プロジェクトメンバーの最適アサイン")
    st.dataframe(df)

    
if __name__ == "__main__":
    render_page()