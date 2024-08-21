import streamlit as st
from PIL import Image
from package import module


# レシピページ
st.set_page_config(layout="wide")                          # ワイドモード
st.image(Image.open("img/sub.png"), use_column_width=True) # サブビジュアル
module.header("レシピ")                                     # ヘッダー

# 保持変数 初期化
if "can_move" not in st.session_state: st.session_state.can_move = False # ページ遷移フラグ

# レシピ一覧
module.recipe_display(3,2)

# ページ遷移（サイドバー → レシピ詳細ページ）
if st.session_state.can_move: st.switch_page("pages/recipe_detail.py")