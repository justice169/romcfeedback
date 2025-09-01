import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="ROM Community Suggestions",
    page_icon="🎮",
    layout="wide"
)

# Custom CSS to hide scrollbar and adjust layout
st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
    }
    
    /* Hide the default streamlit scrollbar for embedded content */
    iframe {
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🏆 ROM Community Suggestions Dashboard")

# Sidebar
st.sidebar.markdown("## 📊 Dashboard Options")

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

# Simplified HTML content (without the complex CSS that causes scrolling issues)
def get_simplified_html():
    return """
    <div style="font-family: 'Segoe UI', sans-serif; color: #ecf0f1; background: #2c3e50; padding: 20px; border-radius: 10px; margin: 0;">
        <div style="text-align: center; margin-bottom: 30px; border-bottom: 2px solid #3498db; padding-bottom: 20px;">
            <h1 style="color: #3498db; margin: 0; font-size: 2em;">🏆 TOP COMMUNITY SUGGESTIONS</h1>
            <div style="color: #bdc3c7; font-size: 1.1em; margin-top: 10px;">📅 Week of August 25-31, 2025</div>
        </div>
        
        <div style="background: #34495e; padding: 20px; border-radius: 10px; margin: 20px 0; text-align: center;">
            <span style="display: inline-block; margin: 0 20px; text-align: center;">
                <span style="font-size: 2em; font-weight: bold; color: #3498db; display: block;">7</span>
                <span style="color: #bdc3c7; font-size: 0.9em;">Total Suggestions</span>
            </span>
            <span style="display: inline-block; margin: 0 20px; text-align: center;">
                <span style="font-size: 2em; font-weight: bold; color: #3498db; display: block;">203</span>
                <span style="color: #bdc3c7; font-size: 0.9em;">Total Votes</span>
            </span>
            <span style="display: inline-block; margin: 0 20px; text-align: center;">
                <span style="font-size: 2em; font-weight: bold; color: #3498db; display: block;">29</span>
                <span style="color: #bdc3c7; font-size: 0.9em;">Avg. Votes</span>
            </span>
        </div>
        
        <!-- Top Suggestions -->
        <div style="background: linear-gradient(145deg, #34495e, #2c3e50); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid #27ae60;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background: #27ae60; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">1</div>
                <div style="flex-grow: 1;"><strong>meng2_tetangga#0</strong></div>
                <div style="background: #27ae60; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 41</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>Adjustment on Abyss Lake Daily Purification</strong><br>
                Abyss lake daily 3k purification consumes so much time, on average it's around 1h if crowded. Currently peaks at 3/8 MVP/Mini, but will peak at 5/10 in future expansion - taking 2h to complete. IT'S SUCH A CHORE!
            </div>
            <div style="display: inline-block; background: #9b59b6; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">GAMEPLAY</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/26/2025 12:33 PM</div>
        </div>
        
        <div style="background: linear-gradient(145deg, #34495e, #2c3e50); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid #27ae60;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background: #27ae60; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">2</div>
                <div style="flex-grow: 1;"><strong>escutcheon_51752#0</strong></div>
                <div style="background: #27ae60; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 36</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>Fix Homunculus Issues (Genetics Class)</strong><br>
                Major problems: Slow movement speed, inefficient AI, lack of control over movement/skills/targeting, defensive power doesn't scale. Current "HP doesn't reduce when Hell Tree is active" doesn't address core issues.
            </div>
            <div style="display: inline-block; background: #e67e22; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">CLASS BALANCE</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/28/2025 10:04 PM</div>
        </div>
        
        <div style="background: linear-gradient(145deg, #34495e, #2c3e50); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid #27ae60;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background: #27ae60; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">3</div>
                <div style="flex-grow: 1;"><strong>gegs6597#0</strong></div>
                <div style="background: #27ae60; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 33</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>Instant Daily Purification Progress</strong><br>
                Make daily purification grind/progress to be completed instantly like Camp Sweep. This purification feature is very tiring and unnecessary.
            </div>
            <div style="display: inline-block; background: #9b59b6; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">GAMEPLAY</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/25/2025 2:40 PM</div>
        </div>
        
        <div style="background: linear-gradient(145deg, #34495e, #2c3e50); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid #27ae60;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background: #27ae60; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">4</div>
                <div style="flex-grow: 1;"><strong>rue.a_#0</strong></div>
                <div style="background: #27ae60; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 30</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>Bring Back Chaotic Spacetime Instance</strong><br>
                It's fun and has great rewards! Community misses this content.
            </div>
            <div style="display: inline-block; background: #f39c12; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">CONTENT</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/25/2025 5:48 AM</div>
        </div>
        
        <div style="background: linear-gradient(145deg, #34495e, #2c3e50); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid #27ae60;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background: #27ae60; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">5</div>
                <div style="flex-grow: 1;"><strong>setsuna7182#0</strong></div>
                <div style="background: #27ae60; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 27</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>Reduce Grind & Balance Classes</strong><br>
                "Stop turning this game into grindy AF like ROMEL! THIS IS ROMC!! Reduce abyssal lake farming time, give more purification points. LET US SWEEP ON THOSE MVP/Minis too!"
            </div>
            <div style="display: inline-block; background: #e67e22; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">CLASS BALANCE</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/29/2025 6:14 AM</div>
        </div>
    </div>
    """

# Display content without iframe scrolling issues
st.markdown("---")
components.html(get_simplified_html(), height=1400, scrolling=True)

# Export Options
# st.markdown("---")
# st.subheader("📈 Export Options")

# col1, col2, col3 = st.columns(3)
# with col1:
#     if st.button("📋 Copy Discord Format"):
#         discord_format = """📊 **TOP COMMUNITY SUGGESTIONS - Week Aug 25-31**

# 🥇 **#1 (41 votes)** - Abyss Lake Daily Purification  
# └ Takes 1-2 hours, needs optimization

# 🥈 **#2 (36 votes)** - Fix Homunculus Issues  
# └ AI problems, movement speed, control issues

# 🥉 **#3 (33 votes)** - Instant Purification Progress  
# └ Make it like Camp Sweep

# 🏅 **#4 (30 votes)** - Bring Back Chaotic Spacetime  
# 🏅 **#5 (27 votes)** - Reduce Grind & Balance Classes

# **📈 Total: 203 votes from 7 suggestions**"""
        
#         st.code(discord_format, language="markdown")
#         st.success("Discord format ready to copy!")

# with col2:
#     if st.button("📊 View Raw Data"):
#         st.json({
#             "week": "Aug 25-31, 2025",
#             "total_suggestions": 7,
#             "total_votes": 203,
#             "top_suggestions": [
#                 {"rank": 1, "votes": 41, "title": "Abyss Lake Daily Purification", "category": "Gameplay"},
#                 {"rank": 2, "votes": 36, "title": "Fix Homunculus Issues", "category": "Class Balance"},
#                 {"rank": 3, "votes": 33, "title": "Instant Purification Progress", "category": "Gameplay"},
#                 {"rank": 4, "votes": 30, "title": "Bring Back Chaotic Spacetime", "category": "Content"},
#                 {"rank": 5, "votes": 27, "title": "Reduce Grind & Balance Classes", "category": "Class Balance"}
#             ]
#         })

# with col3:
#     st.info("💡 **Dev Team Action Items:**\n- Prioritize Abyss Lake optimization\n- Address Homunculus AI issues\n- Consider instant purification feature")