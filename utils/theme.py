import streamlit as st

def apply_premium_theme():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
        
        /* Global Typography */
        html, body, [class*="css"]  {
            font-family: 'Outfit', sans-serif !important;
        }
        
        /* Background Gradient */
        .stApp {
            background: linear-gradient(135deg, #020617 0%, #0f172a 100%);
            background-attachment: fixed;
        }
        
        /* Sidebar Glassmorphism */
        [data-testid="stSidebar"] {
            background: rgba(15, 23, 42, 0.4) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        /* Containers, Metrics, Dataframes */
        [data-testid="stMetric"], .stDataFrame, .stPlotlyChart {
            background: rgba(30, 41, 59, 0.3) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 20px !important;
            padding: 20px !important;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1) !important;
            transition: all 0.3s ease !important;
        }
        
        [data-testid="stMetric"]:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 40px rgba(59, 130, 246, 0.2) !important;
            border: 1px solid rgba(59, 130, 246, 0.3) !important;
        }
        
        /* Metric Values Text Gradient */
        [data-testid="stMetricValue"] {
            background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700 !important;
            font-size: 2.2rem !important;
        }

        /* Buttons Styling */
        .stButton>button {
            background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.6rem 2rem !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3) !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(99, 102, 241, 0.5) !important;
            filter: brightness(1.1);
        }

        /* Input Fields */
        .stTextInput>div>div>input, .stSelectbox>div>div>select, .stDateInput>div>div>input {
            background: rgba(15, 23, 42, 0.5) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 12px !important;
            color: #f8fafc !important;
            transition: all 0.3s ease;
        }
        
        .stTextInput>div>div>input:focus, .stSelectbox>div>div>select:focus {
            border: 1px solid #3b82f6 !important;
            box-shadow: 0 0 15px rgba(59, 130, 246, 0.2) !important;
        }
        
        /* Headings Gradient */
        h1, h2, h3 {
            background: linear-gradient(to right, #60a5fa, #a855f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800 !important;
            letter-spacing: -0.5px;
            margin-bottom: 1.5rem !important;
        }

        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
            background-color: transparent;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: transparent;
            border-radius: 4px 4px 0px 0px;
            gap: 1px;
            padding-top: 10px;
            padding-bottom: 10px;
        }
        
        .stTabs [aria-selected="true"] {
            background: rgba(59, 130, 246, 0.1) !important;
            border-bottom: 2px solid #3b82f6 !important;
            border-radius: 8px 8px 0 0 !important;
        }

        /* Divider */
        hr {
            border-color: rgba(255, 255, 255, 0.1) !important;
        }
        
        /* Toast messages */
        [data-testid="stToast"] {
            background: rgba(30, 41, 59, 0.9) !important;
            backdrop-filter: blur(10px) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 12px !important;
        }
        </style>
    """, unsafe_allow_html=True)
