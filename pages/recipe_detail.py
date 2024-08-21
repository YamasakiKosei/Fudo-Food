import streamlit as st
from PIL import Image
import time
from package import module # 自作モジュールをインポート


# レシピ詳細ページ
st.set_page_config(layout="wide")                          # ワイドモード
st.image(Image.open("img/sub.png"), use_column_width=True) # サブビジュアル
module.header("レシピ")                                     # ヘッダー

try :
    # 戻るボタン
    button_label = "＜　"
    button_label += "レシピ" if st.session_state.had_page == "recipe" else st.session_state.had_data["name"]
    if st.button(button_label):
        if st.session_state.had_page == "product_detail":
            st.session_state.select_data = st.session_state.had_data # had_dataを選択された項目に戻す
            st.session_state.had_data = "エラー"                      # had_dataは削除
        st.switch_page(f'pages/{st.session_state.had_page}.py')      # ページ遷移
    # レシピ詳細
    col1, col2 = st.columns(2)
    with col1:
        st.image(st.session_state.select_data["img"], use_column_width=True) # 画像
    with col2:
        st.subheader(f'**{st.session_state.select_data["name"]}**')          # レシピ名
        st.write(st.session_state.select_data["info"])                       # 説明
    st.divider()
    st.write("**材料（１人分）**")
    st.write("、".join(st.session_state.select_data["ingredients"]))         # 材料
    st.divider()
    st.write("**料理手順**")
    st.write(st.session_state.select_data["process"])
    st.divider()
    st.write("**みんなの評価**")
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
except Exception as e:
    st.warning("**エラー**\n\n申し訳ございません。\n\nブラウザの「ページ更新」や「戻る・進む」を押すとページを表示できません。\n\n5秒後に自動で画面が切り替わります。")
    time.sleep(5)
    st.switch_page("pages/recipe.py")