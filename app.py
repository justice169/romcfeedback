import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="ROM Community Suggestions",
    page_icon="🎮",
    layout="wide"
)

# Title
st.title("🏆 ROM Community Suggestions Dashboard")

# Read HTML file
def load_html_file():
    with open('templates/suggestions.html', 'r', encoding='utf-8') as f:
        return f.read()

# Main app
def main():
    st.sidebar.markdown("## 📊 Dashboard Options")
    
    # Sidebar options
    week_option = st.sidebar.selectbox(
        "Select Week:",
        ["Week Aug 25-31, 2025", "Previous Weeks"]
    )
    
    show_stats = st.sidebar.checkbox("Show Statistics", True)
    
    if show_stats:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Suggestions", "7", "+2")
        with col2:
            st.metric("Total Votes", "203", "+15")
        with col3:
            st.metric("Avg Votes", "29", "+3")
    
    # Display HTML
    st.markdown("---")
    html_content = load_html_file()
    components.html(html_content, height=1200, scrolling=True)
    
    # Additional features
    st.markdown("---")
    st.subheader("📈 Export Options")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📋 Copy Discord Format"):
            st.code("""📊 TOP SUGGESTIONS - Week Aug 25-31
🥇 #1 (41 votes) - Abyss Lake Daily Purification
🥈 #2 (36 votes) - Fix Homunculus Issues  
🥉 #3 (33 votes) - Instant Purification Progress""")
    
    with col2:
        if st.button("📊 Download CSV"):
            st.info("CSV download feature coming soon!")
    
    with col3:
        if st.button("📷 Generate Screenshot"):
            st.info("Screenshot feature coming soon!")

if __name__ == "__main__":
    main()