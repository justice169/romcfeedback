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
        st.metric("Total Votes", "259", "+18")
    with col3:
        st.metric("Avg Votes", "37", "+2.5")

# Simplified HTML content with correct data
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
                <span style="font-size: 2em; font-weight: bold; color: #3498db; display: block;">259</span>
                <span style="color: #bdc3c7; font-size: 0.9em;">Total Votes</span>
            </span>
            <span style="display: inline-block; margin: 0 20px; text-align: center;">
                <span style="font-size: 2em; font-weight: bold; color: #3498db; display: block;">37</span>
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
                <div style="flex-grow: 1;"><strong>havoc2k7#0</strong></div>
                <div style="background: #27ae60; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 35</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>Stubborn Devs - Listen to Community</strong><br>
                "Please listen to your community. Why keep adding useless buffs when every jobclass has already told you what their problems are? Either lower the meta class damage formula or add restrictions like longer cooldowns on their OP skills."
            </div>
            <div style="display: inline-block; background: #e67e22; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">CLASS BALANCE</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/29/2025 1:31 PM</div>
        </div>
        
        <div style="background: linear-gradient(145deg, #34495e, #2c3e50); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid #27ae60;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background: #27ae60; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">4</div>
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
                <div style="background: #f39c12; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">5</div>
                <div style="flex-grow: 1;"><strong>vexxx5502#0</strong></div>
                <div style="background: #f39c12; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 30</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>Fix Abyss MVP/Mini Grind</strong><br>
                "Yes you did make 3K purification faster but not MVP and Mini. That thing takes HOURS of AFK farming to finish. This game is starting to feel like a second job."
            </div>
            <div style="display: inline-block; background: #9b59b6; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">GAMEPLAY</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/29/2025 3:23 PM</div>
        </div>
        
        <div style="background: linear-gradient(145deg, #34495e, #2c3e50); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid #f39c12;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background: #f39c12; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">5</div>
                <div style="flex-grow: 1;"><strong>rue.a_#0</strong></div>
                <div style="background: #f39c12; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 30</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>Bring Back Chaotic Spacetime Instance</strong><br>
                It's fun and has great rewards! Community misses this content.
            </div>
            <div style="display: inline-block; background: #f39c12; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">CONTENT</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/25/2025 5:48 AM</div>
        </div>
        
        <div style="background: linear-gradient(145deg, #34495e, #2c3e50); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid #f39c12;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background: #f39c12; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">7</div>
                <div style="flex-grow: 1;"><strong>setsuna7182#0</strong></div>
                <div style="background: #f39c12; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 27</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>Reduce Grind & Balance Classes</strong><br>
                "Stop turning this game into grindy AF like ROMEL! THIS IS ROMC!! Reduce abyssal lake farming time, give more purification points. LET US SWEEP ON THOSE MVP/Minis too!"
            </div>
            <div style="display: inline-block; background: #e67e22; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">CLASS BALANCE</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/29/2025 6:14 AM</div>
        </div>
        
        <div style="background: linear-gradient(145deg, #34495e, #2c3e50); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid #f39c12;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background: #f39c12; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">8</div>
                <div style="flex-grow: 1;"><strong>extr3meguy#0</strong></div>
                <div style="background: #f39c12; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 26</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>GVG Targeting Options</strong><br>
                During GVG when targeting, give us option aside from "attack all" and "emperium". Give us option to target "Players" specifically - when we select attack all it attacks the emperium too.
            </div>
            <div style="display: inline-block; background: #1abc9c; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">UI/UX</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/25/2025 3:27 PM</div>
        </div>
        
        <div style="background: linear-gradient(145deg, #34495e, #2c3e50); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid #f39c12;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background: #f39c12; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">9</div>
                <div style="flex-grow: 1;"><strong>loki8238#0</strong></div>
                <div style="background: #f39c12; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 25</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>Make All Master Skills Spammable</strong><br>
                Like spiritual combo and insta slash! Improve skill accessibility for all classes.
            </div>
            <div style="display: inline-block; background: #e67e22; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">CLASS BALANCE</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/30/2025 2:00 PM</div>
        </div>
        
        <div style="background: linear-gradient(145deg, #34495e, #2c3e50); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid #95a5a6;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background: #95a5a6; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">10</div>
                <div style="flex-grow: 1;"><strong>extr3meguy#0</strong></div>
                <div style="background: #95a5a6; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 12</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>Make Lunch Box Feature</strong><br>
                Make a lunch box so we can utilize eating the gourmet. Where we can select 6 foods. So when we refood we just have to eat once at the camp.
            </div>
            <div style="display: inline-block; background: #9b59b6; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">GAMEPLAY</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/24/2025 11:48 PM</div>
        </div>
        
        <div style="background: linear-gradient(145deg, #34495e, #2c3e50); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid #95a5a6;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background: #95a5a6; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">11</div>
                <div style="flex-grow: 1;"><strong>stardar123#0</strong></div>
                <div style="background: #95a5a6; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 5</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>Give More Debt to Devs</strong><br>
                "Give more debt so devs be happy and go to afterlife literally"
            </div>
            <div style="display: inline-block; background: #95a5a6; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">MISC</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/29/2025 3:24 PM</div>
        </div>px; font-weight: bold;">✅ 27</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>Reduce Grind & Balance Classes</strong><br>
                "Stop turning this game into grindy AF like ROMEL! THIS IS ROMC!! Reduce abyssal lake farming time, give more purification points. LET US SWEEP ON THOSE MVP/Minis too!"
            </div>
            <div style="display: inline-block; background: #e67e22; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">CLASS BALANCE</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/29/2025 6:14 AM</div>
        </div>
        
        <div style="background: linear-gradient(145deg, #34495e, #2c3e50); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid #27ae60;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background: #f39c12; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">6</div>
                <div style="flex-grow: 1;"><strong>extr3meguy#0</strong></div>
                <div style="background: #f39c12; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 26</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>GVG Targeting Options</strong><br>
                During GVG when targeting, give us option aside from "attack all" and "emperium". Give us option to target "Players" specifically - when we select attack all it attacks the emperium too.
            </div>
            <div style="display: inline-block; background: #1abc9c; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">UI/UX</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/25/2025 3:27 PM</div>
        </div>
        
        <div style="background: linear-gradient(145deg, #34495e, #2c3e50); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid #27ae60;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background: #f39c12; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; font-weight: bold; margin-right: 15px;">7</div>
                <div style="flex-grow: 1;"><strong>loki8238#0</strong></div>
                <div style="background: #f39c12; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold;">✅ 25</div>
            </div>
            <div style="color: #ecf0f1; line-height: 1.6; margin-bottom: 10px;">
                <strong>Make All Master Skills Spammable</strong><br>
                Like spiritual combo and insta slash! Improve skill accessibility for all classes.
            </div>
            <div style="display: inline-block; background: #e67e22; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-top: 8px;">CLASS BALANCE</div>
            <div style="color: #95a5a6; font-size: 0.9em; margin-top: 10px;">📅 08/30/2025 2:00 PM</div>
        </div>
    </div>
    """

# Display content
st.markdown("---")
components.html(get_simplified_html(), height=1200, scrolling=True)