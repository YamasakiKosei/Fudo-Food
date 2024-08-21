import streamlit as st
from PIL import Image
import time
from package import module # 自作モジュールをインポート


# 商品詳細ページ
st.set_page_config(layout="wide")                          # ワイドモード
st.image(Image.open("img/sub.png"), use_column_width=True) # サブビジュアル
module.header("ショッピング")                               # ヘッダー

# 戻るボタン
if st.button("＜　ホーム"): st.switch_page("./home.py")

try:
    # 商品詳細
    col1, col2 = st.columns(2)
    with col1:
        st.image(st.session_state.select_data["img"], use_column_width=True) # 画像
    with col2:
        st.subheader(f'**{st.session_state.select_data["name"]}**')          # 商品名
        st.title(f'¥ {st.session_state.select_data["price"]}')               # 価格
        if st.button("購入手続きへ", use_container_width=True): st.switch_page("pages/purchase.py")
        st.divider()
        st.write("**商品の説明**")
        st.write(st.session_state.select_data["info"])                       # 商品情報
    st.divider()

    # 関連レシピ
    st.subheader("関連レシピ")
    for col, data in zip(st.columns(5), st.session_state.select_data["recipe"]):
        with col:
                st.image(data["img"], use_column_width=True) # 画像
                # ページ遷移（レシピ詳細ページ）
                if st.button(data["name"], key=data["id"], use_container_width=True):
                    st.session_state.had_data = st.session_state.select_data # 選択された商品をhad_dataに保存
                    st.session_state.select_data = data                      # 選択された項目をレシピに変更
                    st.session_state.had_page = "product_detail"             # 遷移前のページは商品詳細ページ
                    st.switch_page("pages/recipe_detail.py")
except Exception as e:
    st.warning("**エラー**\n\n申し訳ございません。\n\nブラウザの「ページ更新」や「戻る・進む」を押すとページを表示できません。\n\n5秒後に自動で画面が切り替わります。")
    time.sleep(5)
    st.switch_page("./home.py")
            