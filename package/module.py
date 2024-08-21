import streamlit as st

# 自作モジュール

# データベース
# レシピデータ
recipe = [
    {"id":101,
     "name":"サラダそうめん",
     "info":"野菜もたっぷり食べられるさっぱりそうめん！",
     "img":"https://www.kyounoryouri.jp/upfile/r/new_xl_1529308734_3360.jpg",
     "ingredients":["そうめん", "きゅうり", "ミニトマト", "ツナ缶", "めんつゆ", "こしょう"], 
     "process":"1.そうめんを茹でて、水で占める。\n\n2.きゅうりは千切りにする。...",
     "evaluation":4.2
    },
    {"id":102,
     "name":"フルーツかんざらし",
     "info":"甘いみつにかんざらしとフルーツがマッチ！",
     "img":"https://www.mod.go.jp/msdf/kanmeshi/menu/sw/018/img/index.jpg",
     "ingredients":["かんざらし", "パイン", "ゼリー", "みかん", "マンゴー"], 
     "process":"1.鍋に砂糖、塩、水を入れ...\n\n2.ボウルに白玉粉を入れ...",
     "evaluation":5
    },
    {"id":103,
     "name":"具だくさん具雑煮",
     "info":"栄養満点のあったか具雑煮！",
     "img":"https://video.kurashiru.com/production/videos/e0c55b95-9b4e-48a9-9c2b-6660644cb404/compressed_thumbnail_square_large.jpg?1720889263",
     "ingredients":["丸もち", "鶏もも", "かまぼこ", "ちくわ", "豆腐", "里芋"], 
     "process":"1.ボウルに豆腐を入れ...\n\n2.里芋は皮をむき...",
     "evaluation":3.8
    },
    {"id":104,
     "name":"サラダそうめん",
     "info":"野菜もたっぷり食べられるさっぱりそうめん！",
     "img":"https://www.kyounoryouri.jp/upfile/r/new_xl_1529308734_3360.jpg",
     "ingredients":["そうめん", "きゅうり", "ミニトマト", "ツナ缶", "めんつゆ", "こしょう"], 
     "process":"1.そうめんを茹でて、水で占める。\n\n2.きゅうりは千切りにする。...",
     "evaluation":4.2
    },
    {"id":105,
     "name":"フルーツかんざらし",
     "info":"甘いみつにかんざらしとフルーツがマッチ！",
     "img":"https://www.mod.go.jp/msdf/kanmeshi/menu/sw/018/img/index.jpg",
     "ingredients":["かんざらし", "パイン", "ゼリー", "みかん", "マンゴー"], 
     "process":"1.鍋に砂糖、塩、水を入れ...\n\n2.ボウルに白玉粉を入れ...",
     "evaluation":5
    },
    {"id":106,
     "name":"具だくさん具雑煮",
     "info":"栄養満点のあったか具雑煮！",
     "img":"https://video.kurashiru.com/production/videos/e0c55b95-9b4e-48a9-9c2b-6660644cb404/compressed_thumbnail_square_large.jpg?1720889263",
     "ingredients":["丸もち", "鶏もも", "かまぼこ", "ちくわ", "豆腐", "里芋"], 
     "process":"1.ボウルに豆腐を入れ...\n\n2.里芋は皮をむき...",
     "evaluation":3.8
    }
]
# 商品データ
product = [
    {"id":1,
     "name":"手延べ島原素麺",
     "info":"島原の湧水で作られたおいしいそうめんです。",
     "price":500,
     "img":"https://cdn.askul.co.jp/img/product/3L1/NX28904_3L1.jpg",
     "recipe":[recipe[0], recipe[1], recipe[2], recipe[3], recipe[4], recipe[5]]
    },
    {"id":2,
     "name":"かんざらし",
     "info":"島原で長く愛されているスイーツのひとつ。甘い蜜が最高です。",
     "price":300,
     "img":"https://img21.shop-pro.jp/PA01476/611/product/167953410.jpg?cmsp_timestamp=20220427141625",
     "recipe":[recipe[0], recipe[1], recipe[2], recipe[3], recipe[4], recipe[5]]
    },
    {"id":3,
     "name":"具雑煮",
     "info":"島原に昔から伝わる伝統的な郷土料理がお家で食べられます。",
     "price":1000,
     "img":"https://p1-3c615a9b.imageflux.jp/w=1200,h=1200,a=0,u=0,ir=auto/uploads/product_image/image/725206/image.jpg?1617703227",
     "recipe":[recipe[0], recipe[1], recipe[2], recipe[3], recipe[4], recipe[5]]
    },
    {"id":4,
     "name":"手延べ島原素麺",
     "info":"島原の湧水で作られたおいしいそうめんです。",
     "price":500,
     "img":"https://cdn.askul.co.jp/img/product/3L1/NX28904_3L1.jpg",
     "recipe":[recipe[0], recipe[1], recipe[2], recipe[3], recipe[4], recipe[5]]
    },
    {"id":5,
     "name":"かんざらし",
     "info":"島原で長く愛されているスイーツのひとつ。甘い蜜が最高です。",
     "price":300,
     "img":"https://img21.shop-pro.jp/PA01476/611/product/167953410.jpg?cmsp_timestamp=20220427141625",
     "recipe":[recipe[0], recipe[1], recipe[2], recipe[3], recipe[4], recipe[5]]
    },
    {"id":6,
     "name":"具雑煮",
     "info":"島原に昔から伝わる伝統的な郷土料理がお家で食べられます。",
     "price":1000,
     "img":"https://p1-3c615a9b.imageflux.jp/w=1200,h=1200,a=0,u=0,ir=auto/uploads/product_image/image/725206/image.jpg?1617703227",
     "recipe":[recipe[0], recipe[1], recipe[2], recipe[3], recipe[4], recipe[5]]
    }
]

######################################################### 共通 ##########################################################################
# ヘッダー
def header(header):
    st.text_input(label=" ", placeholder="検索")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("ショッピング", use_container_width=True): st.switch_page("./home.py")
    with col2:
        if st.button("レシピ", use_container_width=True): st.switch_page("pages/recipe.py")
    with col3:
        if st.button("トピック", use_container_width=True): st.switch_page("pages/topic.py")
    st.divider()
    st.header(header)
    st.divider()

# 保持変数 初期化
if "can_move" not in st.session_state: st.session_state.can_move = False                  # ページ遷移フラグ
if "select_data" not in st.session_state: st.session_state.select_data = {"name":"エラー"} # 選択された項目
if "had_data" not in st.session_state: st.session_state.had_data = {"name":"エラー"}       # ページ遷移前に選択されていた項目（「商品一覧→商品詳細→レシピ詳細」の戻るボタンで必要）
if "had_page" not in st.session_state: st.session_state.had_page = "エラー"                # ページ遷移前のページ（「商品詳細→レシピ詳細」 or 「レシピ一覧→レシピ詳細」の区別 戻るボタンで必要）

######################################################### ショッピング ##########################################################################
# サイドバーに表示（商品）
def side_view(num):
    st.session_state.select_data = product[num]
    with st.sidebar:
        st.title(product[num]["name"])     # 商品名
        st.divider()
        st.image(product[num]["img"])      # 画像
        st.subheader(product[num]["name"]) # 商品名
        st.title(f'¥ {product[num]["price"]}')    # 価格
        st.divider()
        st.write("**商品の説明**")
        st.write(product[num]["info"])     # 商品情報
        st.divider()
        st.button("続きを見る", key="can_move", use_container_width=True)

# 商品一覧
def product_display(width, height):
    num = 0
    for col in st.columns(width):
        with col:
            for row in range(height):
                st.image(product[num]["img"], use_column_width=True)
                if st.button(f'{product[num]["name"]}\n\n¥ {product[num]["price"]}', key=product[num]["id"], use_container_width=True) : side_view(num)
                num += 1

######################################################### レシピ ##########################################################################
# サイドバーに表示（レシピ）
def side_view_recipe(num):
    st.session_state.select_data = recipe[num]
    st.session_state.had_page = "recipe"
    with st.sidebar:
        st.title(recipe[num]["name"])                   # レシピ名
        st.divider()
        st.image(recipe[num]["img"])                    # 画像
        st.write(recipe[num]["info"])                   # 説明
        st.divider()
        st.write("**材料（１人分）**")
        st.write("、".join(recipe[num]["ingredients"])) # 材料
        st.divider()
        st.button("続きを見る", key="can_move", use_container_width=True)

# レシピ一覧
def recipe_display(width, height):
    num = 0
    for col in st.columns(width):
        with col:
            for row in range(height):
                st.image(recipe[num]["img"], use_column_width=True)
                if st.button(recipe[num]["name"], key=recipe[num]["id"], use_container_width=True) : side_view_recipe(num)
                num += 1