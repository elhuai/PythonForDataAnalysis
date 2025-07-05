import matplotlib 
import streamlit as st
import yfinance as yf
import os
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# 页面配置
st.set_page_config(
    page_title="📈 台股分析",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定义 CSS 样式
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #F5F5DC 0%, #F0F8E8 50%, #E8F5E8 100%);
        font-family: 'Noto Sans JP', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #D4A574 0%, #B8860B 100%);
        padding: 2.5rem 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 25px rgba(139, 69, 19, 0.2);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .zen-card {
        background: linear-gradient(145deg, #FFFFFF 0%, #F9F9F9 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin: 1.5rem 0;
        border-left: 4px solid #E8A87C;
        position: relative;
    }
    
    .zen-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #E8A87C, #D4A574);
        border-radius: 15px 15px 0 0;
    }
    
    .metric-box {
        background: linear-gradient(135deg, #F0F8E8 0%, #E8F5E8 100%);
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin: 0.5rem;
        border: 1px solid rgba(232, 168, 124, 0.3);
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .zen-button {
        background: linear-gradient(135deg, #E8A87C 0%, #D4A574 100%);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(232, 168, 124, 0.3);
        font-family: 'Noto Sans JP', sans-serif;
    }
    
    .zen-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(232, 168, 124, 0.4);
    }
    
    .nature-accent {
        color: #8B4513;
        font-weight: 500;
    }
    
    .bamboo-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #E8A87C, transparent);
        margin: 2rem 0;
    }
    
    .stSelectbox > div > div {
        background: linear-gradient(135deg, #FFFFFF 0%, #F9F9F9 100%);
        border-radius: 12px;
        border: 1px solid rgba(232, 168, 124, 0.3);
    }
    
    .stMultiSelect > div > div {
        background: linear-gradient(135deg, #FFFFFF 0%, #F9F9F9 100%);
        border-radius: 12px;
        border: 1px solid rgba(232, 168, 124, 0.3);
    }
    
    .stDateInput > div > div > input {
        background: linear-gradient(135deg, #FFFFFF 0%, #F9F9F9 100%);
        border-radius: 12px;
        border: 1px solid rgba(232, 168, 124, 0.3);
    }
    
    .japanese-title {
        font-family: 'Noto Sans JP', sans-serif;
        font-weight: 300;
        color: #2F2F2F;
        letter-spacing: 0.5px;
    }
    
    .zen-info {
        background: linear-gradient(135deg, #F0F8E8 0%, #E8F5E8 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 3px solid #90EE90;
        margin: 1rem 0;
    }
    
    .seasonal-accent {
        display: inline-block;
        margin: 0 0.5rem;
        font-size: 1.2em;
    }
</style>
""", unsafe_allow_html=True)

def download_tw_stocks():
    stock_list = ['2330.TW', '2303.TW', '2454.TW', '2317.TW']
    today_str = datetime.today().strftime('%Y-%m-%d')
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    for stock in stock_list:
        stock_code = stock.split('.')[0]
        filename = f"{stock_code}_{today_str}.csv"
        filepath = os.path.join(data_dir, filename)
        if os.path.exists(filepath):
            continue
        df = yf.download(
            stock,
            start="2010-01-01",
            end=today_str,
            auto_adjust=False
        )
        df.to_csv(filepath)

def load_adjclose_dataframe():
    code_to_name = {
        '2330': '台積電',
        '2303': '聯電',
        '2454': '聯發科',
        '2317': '鴻海'
    }
    data_dir = 'data'
    series_dict = {}
    for code, name in code_to_name.items():
        files = [f for f in os.listdir(data_dir) if f.startswith(code+'_') and f.endswith('.csv')]
        if not files:
            continue
        files.sort(reverse=True)
        filepath = os.path.join(data_dir, files[0])
        df = pd.read_csv(filepath, index_col=0)
        df.index = pd.to_datetime(df.index, errors='coerce')
        df = df[~df.index.isna()]
        if 'Adj Close' in df.columns:
            series_dict[name] = df['Adj Close']
    result_df = pd.DataFrame(series_dict)
    return result_df

# 初始化 session_state
if 'start_date_selected' not in st.session_state:
    st.session_state.start_date_selected = None
if 'end_date_selected' not in st.session_state:
    st.session_state.end_date_selected = None

st.markdown("""
<div class="main-header">
    <h1>📈 台股歷史股價分析</h1>
    <p>🎯 專業級股票數據視覺化</p>
</div>
""", unsafe_allow_html=True)

with st.spinner('🔄 正在同步最新股票數據...'):
    download_tw_stocks()
with st.spinner('📊 正在處理股價資料...'):
    df = load_adjclose_dataframe()

st.markdown('<div class="stock-card">', unsafe_allow_html=True)
st.markdown("### 🎯 股票選擇")
col1, col2 = st.columns([2, 1])

with col1:
    options = sorted(list(df.columns))
    default = [name for name in options if "台積電" in name]
    selected = st.multiselect(
        "📋 請選擇您要分析的股票（支援多選）",
        options=options,
        default=default,
        help="您可以同時選擇多檔股票進行比較分析"
    )

with col2:
    if selected:
        st.markdown("### 📊 已選股票")
        for stock in selected:
            st.markdown(f"✅ **{stock}**")
    else:
        st.markdown("### ⚠️ 請選擇股票")

st.markdown('</div>', unsafe_allow_html=True)

if not df.empty:
    if not pd.api.types.is_datetime64_any_dtype(df.index):
        df.index = pd.to_datetime(df.index, errors='coerce')
        df = df[~df.index.isna()]

    today = pd.to_datetime('today').date()
    
    # 預設日期區間
    last_7_dates = df.index[-7:]
    start_default = last_7_dates[0].date()
    end_default = last_7_dates[-1].date()

    if st.session_state.start_date_selected is None:
        st.session_state.start_date_selected = start_default
    if st.session_state.end_date_selected is None:
        st.session_state.end_date_selected = end_default

    st.markdown('<div class="stock-card">', unsafe_allow_html=True)
    st.markdown("### ⚡ 快速時間選擇")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button('📅 近一週', help="查看最近 7 天的股價走勢"):
            st.session_state.start_date_selected = max((pd.Timestamp(today) - pd.Timedelta(weeks=1)).date(), df.index[0].date())
            st.session_state.end_date_selected = min(today, df.index[-1].date())
    with col2:
        if st.button('📅 近一月', help="查看最近 30 天的股價走勢"):
            st.session_state.start_date_selected = max((pd.Timestamp(today) - pd.Timedelta(days=30)).date(), df.index[0].date())
            st.session_state.end_date_selected = min(today, df.index[-1].date())
    with col3:
        if st.button('📅 近三月', help="查看最近 3 個月的股價走勢"):
            st.session_state.start_date_selected = max((pd.Timestamp(today) - pd.Timedelta(days=90)).date(), df.index[0].date())
            st.session_state.end_date_selected = min(today, df.index[-1].date())
    with col4:
        if st.button('📅 今年以來', help="查看今年至今的股價走勢"):
            st.session_state.start_date_selected = max(pd.to_datetime(f'{today.year}-01-01').date(), df.index[0].date())
            st.session_state.end_date_selected = min(today, df.index[-1].date())
    with col5:
        if st.button('📅 全部時間', help="查看所有可用數據"):
            st.session_state.start_date_selected = df.index[0].date()
            st.session_state.end_date_selected = df.index[-1].date()

    # 自定义日期选择
    st.markdown("### 📆 自訂日期區間")
    date_col1, date_col2 = st.columns(2)
    
    with date_col1:
        start_date_input = st.date_input(
            "🗓️ 開始日期", 
            value=st.session_state.start_date_selected, 
            min_value=df.index[0].date(), 
            max_value=df.index[-1].date(),
            help="選擇分析的起始日期"
        )
    with date_col2:
        end_date_input = st.date_input(
            "🗓️ 結束日期", 
            value=st.session_state.end_date_selected, 
            min_value=df.index[0].date(), 
            max_value=df.index[-1].date(),
            help="選擇分析的結束日期"
        )

    if start_date_input != st.session_state.start_date_selected:
        st.session_state.start_date_selected = start_date_input
    if end_date_input != st.session_state.end_date_selected:
        st.session_state.end_date_selected = end_date_input

    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.error("⚠️ 資料載入失敗，請檢查網路連線或稍後再試")
    st.session_state.start_date_selected = None
    st.session_state.end_date_selected = None

# 數據展示
if selected and st.session_state.start_date_selected and st.session_state.end_date_selected:
    mask = (df.index.date >= st.session_state.start_date_selected) & (df.index.date <= st.session_state.end_date_selected)
    filtered_df = df.loc[mask, selected]
    filtered_df = filtered_df.apply(pd.to_numeric, errors='coerce')
    filtered_df = filtered_df.dropna(axis=0, how='all').dropna(axis=1, how='all')
    
    if not filtered_df.empty:
        # 總覽統計
        st.markdown('<div class="stock-card">', unsafe_allow_html=True)
        st.markdown("### 📊 投資概覽")
        
        overview_cols = st.columns(len(selected))
        for i, col in enumerate(filtered_df.columns):
            with overview_cols[i]:
                latest_price = filtered_df[col].iloc[-1]
                first_price = filtered_df[col].iloc[0]
                change_pct = ((latest_price - first_price) / first_price) * 100
                
                color = "🟢" if change_pct >= 0 else "🔴"
                st.markdown(f"""
                <div class="metric-container">
                    <h4>{col}</h4>
                    <h3>NT$ {latest_price:,.0f}</h3>
                    <p>{color} {change_pct:+.2f}%</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 图表展示
        for i, col in enumerate(filtered_df.columns):
            st.markdown('<div class="stock-card">', unsafe_allow_html=True)
            chart_data = filtered_df[[col]].round(0)
            st.markdown(f"### 📈 {col} 股價走勢分析")
            
            # 动态调整 y 轴
            min_val = chart_data.min().min()
            max_val = chart_data.max().max()
            margin = (max_val - min_val) * 0.1 if max_val > min_val else 1
            y_min = int(min_val - margin)
            y_max = int(max_val + margin)
            
            # 创建更漂亮的图表
            fig = go.Figure()
            
            # 添加渐变色线条
            colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
            fig.add_trace(go.Scatter(
                x=chart_data.index, 
                y=chart_data[col], 
                mode='lines',
                name=col,
                line=dict(color=colors[i % len(colors)], width=3),
                fill='tonexty' if i > 0 else 'tozeroy',
                fillcolor=f'rgba({int(colors[i % len(colors)][1:3], 16)}, {int(colors[i % len(colors)][3:5], 16)}, {int(colors[i % len(colors)][5:7], 16)}, 0.1)'
            ))
            
            fig.update_layout(
                plot_bgcolor='rgba(255,255,255,0.9)',
                paper_bgcolor='rgba(255,255,255,0.9)',
                yaxis=dict(
                    range=[y_min, y_max], 
                    tickformat=',d',
                    gridcolor='rgba(128,128,128,0.3)'
                ),
                xaxis=dict(
                    title="📅 日期",
                    gridcolor='rgba(128,128,128,0.3)'
                ),
                yaxis_title="💰 收盤價 (NT$)",
                showlegend=False,
                font=dict(size=12),
                margin=dict(t=20, b=20, l=20, r=20),
                hovermode='x unified'
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # 数据表格
        st.markdown('<div class="stock-card">', unsafe_allow_html=True)
        st.markdown("### 📋 詳細數據表")
        st.dataframe(
            filtered_df.round(2).style.background_gradient(cmap='RdYlGn'),
            use_container_width=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        st.warning("⚠️ 所選時間區間內無可用數據，請調整日期範圍")
else:
    st.info("👆 請先選擇股票和日期區間開始分析")

# 页脚
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>📊 台股分析</p>
    <p>💡 數據來源：Yahoo Finance | 僅供參考，投資有風險</p>
</div>
""", unsafe_allow_html=True)
