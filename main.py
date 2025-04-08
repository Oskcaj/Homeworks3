from typing import Tuple

class IkeaFurnitures:
    def __init__(self, product_id, name, category, price, package_dimension, weight, stock):
        self.product_id : str = product_id        # IKEA 產品 ID，例如：barcode '123412341234'
        self.name : str = name                    # 名稱：如 "BILLY 書櫃"
        self.category : str = category            # 分類：如 書櫃、床架
        self.price : float = price                # 價錢（HKD）
        self.package_dimension : Tuple[float,float,float] = package_dimension  # 運輸包裝尺寸：如 "80x28x202 cm"
        self.weight : float = weight              # 重量（kg）
        self.stock : int = stock                  # 庫存數量
        self.in_stock: bool = stock > 0           # 庫存是否有貨

    def display_info(self):
        print("📦 產品資料")
        print(f"名稱：{self.name}")
        print(f"產品編號：{self.product_id}")
        print(f"分類：{self.category}")
        print(f"價格：HK${self.price:,.2f}")
        print(f"運輸包裝尺寸：{self.package_dimension}")
        print(f"重量：約 {self.weight} kg")
        print(f"是否有貨：{'有貨' if self.in_stock else '已售罄'}")
        print(f"庫存：{self.stock} 件")

    def is_available(self) -> bool:
        return self.stock > 0

# 床褥 Class

class Mattress(IkeaFurnitures):
    def __init__(self, product_id, name, category, price, package_dimension, weight, stock,
                 width, length, height, material, warranty, firmness, feature):
        super().__init__(product_id, name, category, price, package_dimension, weight, stock)

        self.width : float = width
        self.length : float = length
        self.height : float = height

        self.material : str = material
        self.warranty : int = warranty
        self.firmness : str = firmness

        # 功能只能選擇其中一個
        allowed_features : list[str] = ["彈簧床褥", "床褥墊", "乳膠床褥"]
        if feature not in allowed_features:
            raise ValueError(f"功能錯誤，必須是以下其中之一：{allowed_features}")
        self.feature = feature

    def get_size(self):
        if self.width <= 92:
            return "單人"
        elif self.width <= 135:
            return "雙人"
        elif self.width <= 150:
            return "特大雙人"
        elif self.width >= 151:
            return "特別訂製"
        else :
            return "尺寸錯誤，請重新輸入"

    def __repr__(self) :
        return (f"{self.name} - {self.category} - 運送尺寸{self.package_dimension}CM - {self.feature} - {self.get_size()} - HK${self.price:,.2f}")
    
# 床架 Class

class BedFrame(IkeaFurnitures):
    def __init__(self, product_id, name, category, price, package_dimension, weight, stock,
                 style, color, material, assembly_time):

        super().__init__(product_id, name, category, price, package_dimension, weight, stock)

        # 款式寫死
        allowed_styles = [
            "單人床架 - (適用92x189cm床褥)",                 # 適用 92x189cm 床褥
            "雙人床架 - (適用135x189cm床褥)",                # 適用 135x189cm 床褥
            "特大雙人床架 - (適用150x200cm床褥)",             # 適用 150x200cm 床褥
            "特別訂製雙人床 - (適用151cm或以上特別訂製床褥)",   # 適用 151cm 或以上
            "碌架床 - (適用92x189cm床褥,1或2張床褥)"          # 適用 92x189cm（上下舖）
        ]

        if style not in allowed_styles:
            raise ValueError(f"必須是以下其中之一：{allowed_styles}")
        self.style = style

        self.color : str = color
        self.material : str = material
        self.assembly_time : int = assembly_time  # 單位：分鐘

    # 自動分類組裝難度
    def get_assembly_difficulty(self):
        if self.assembly_time <= 30:
            return "簡單組裝"
        elif self.assembly_time <= 60:
            return "一般組裝，適合有經驗人仕自行安裝"
        else:
            return "組裝困難，建議由專業人仕組裝"

    def __repr__(self):
        return (f"{self.name} - {self.category} - 款式：{self.style} - 顏色：{self.color} - 物料：{self.material} - "
                f"組裝時間估算需 {self.assembly_time} 分鐘，屬（{self.get_assembly_difficulty()}） - HK${self.price:,.2f}")
# 椅 Class

class Chair(IkeaFurnitures):
    def __init__(self, product_id, name, category, price, package_dimension, weight, stock,
                 chair_type, backrest_height, armrest, surface_type, material,
                 has_wheels, need_assembly, color, has_headrest, adjustable_height):

        super().__init__(product_id, name, category, price, package_dimension, weight, stock)

        allowed_types = ["辦公椅", "電腦椅", "電競椅", "餐椅", "摺椅"]
        if chair_type not in allowed_types:
            raise ValueError(f"必須是：{allowed_types}")
        self.chair_type = chair_type

        self.backrest_height : str = backrest_height       # "高椅背" / "低椅背"
        self.armrest : str = armrest                       # "連扶手" / "不連扶手"
        self.surface_type : str = surface_type             # "真皮" / "仿皮" / "無外皮"
        self.material : str = material                     # 物料（文字）
        self.has_wheels : bool = has_wheels                 # bool
        self.need_assembly : bool = need_assembly           # bool
        self.color : str = color                           # 顏色
        self.has_headrest : bool = has_headrest             # bool
        self.adjustable_height : bool = adjustable_height   # bool

    def __repr__(self):
        return (f"{self.name} - {self.chair_type} - {self.backrest_height} - {self.armrest} - 表面：{self.surface_type}｜"
                f"物料：{self.material} - 顏色：{self.color} - 滾輪：{'有' if self.has_wheels else '無'} -"
                f"裝嵌：{'需要裝嵌' if self.need_assembly else '免裝嵌'} - 頭枕：{'有' if self.has_headrest else '無'} - "
                f"升降：{'可調節升降' if self.adjustable_height else '固定'} - HK${self.price:,.2f}")
m1 = Mattress(
    product_id="903.195.12",
    name="HAUGSVÄR",
    category="床褥",
    price=348.59,
    package_dimension=(150, 80, 24),
    weight=24.8,
    stock=17,
    width=150,
    length=200,
    height=20,
    material="spring",
    warranty=12,
    firmness="firm",
    feature="彈簧床褥"
)

m2 = Mattress(
    product_id="903.829.49",
    name="HYLLESTAD",
    category="床褥",
    price=576.1,
    package_dimension=(148, 80, 21),
    weight=29.9,
    stock=9,
    width=90,
    length=200,
    height=19,
    material="spring",
    warranty=8,
    firmness="medium",
    feature="彈簧床褥"
)

m3 = Mattress(
    product_id="903.882.62",
    name="HOVAG",
    category="床褥",
    price=356.88,
    package_dimension=(142, 80, 21),
    weight=29.0,
    stock=1,
    width=150,
    length=200,
    height=22,
    material="foam",
    warranty=12,
    firmness="medium",
    feature="彈簧床褥"
)

m4 = Mattress(
    product_id="903.814.95",
    name="MORGEDAL",
    category="床褥",
    price=561.37,
    package_dimension=(145, 80, 23),
    weight=25.4,
    stock=7,
    width=90,
    length=200,
    height=21,
    material="foam",
    warranty=9,
    firmness="firm",
    feature="彈簧床褥"
)

m5 = Mattress(
    product_id="903.353.15",
    name="MALFORS",
    category="床褥",
    price=485.04,
    package_dimension=(152, 80, 23),
    weight=24.6,
    stock=2,
    width=150,
    length=200,
    height=23,
    material="spring",
    warranty=5,
    firmness="medium firm",
    feature="彈簧床褥"
)

m6 = Mattress(
    product_id="903.941.38",
    name="MATRAND",
    category="床褥",
    price=453.77,
    package_dimension=(157, 80, 21),
    weight=29.2,
    stock=0,
    width=135,
    length=200,
    height=20,
    material="latex",
    warranty=12,
    firmness="soft",
    feature="彈簧床褥"
)

m7 = Mattress(
    product_id="903.673.76",
    name="MYRBACKA",
    category="床褥",
    price=366.13,
    package_dimension=(149, 80, 23),
    weight=28.2,
    stock=10,
    width=150,
    length=200,
    height=23,
    material="latex",
    warranty=6,
    firmness="medium",
    feature="彈簧床褥"
)

m8 = Mattress(
    product_id="903.858.83",
    name="MINNESUND",
    category="床褥",
    price=1563.7,
    package_dimension=(147, 80, 18),
    weight=25.9,
    stock=3,
    width=135,
    length=200,
    height=20,
    material="spring",
    warranty=14,
    firmness="firm",
    feature="彈簧床褥"
)

m9 = Mattress(
    product_id="903.432.69",
    name="MEISTERVIK",
    category="床褥",
    price=341.02,
    package_dimension=(144, 80, 21),
    weight=22.2,
    stock=20,
    width=90,
    length=200,
    height=18,
    material="foam",
    warranty=11,
    firmness="medium",
    feature="彈簧床褥"
)

m10 = Mattress(
    product_id="903.961.68",
    name="VESTERÖY",
    category="床褥",
    price=389.47,
    package_dimension=(145, 80, 21),
    weight=29.5,
    stock=8,
    width=90,
    length=200,
    height=22,
    material="foam",
    warranty=14,
    firmness="soft",
    feature="彈簧床褥"
)

mattress_list = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

for i, mattress in enumerate(mattress_list, 1):
    print(f"Mattress : {mattress.name} - {mattress.get_size()} - {mattress.feature} - {mattress.material} - {mattress.firmness} - ${mattress.price:,.2f} - 保養{mattress.warranty}月") #總結滙出

bf1 = BedFrame(
    product_id="BF100",
    name="床架系列 A",
    category="床架",
    price=2519.44,
    package_dimension=(149.8, 36.8, 12.5),
    weight=31.9,
    stock=19,
    style="雙人床架 - (適用135x189cm床褥)",
    color="黑色",
    material="膠合板",
    assembly_time=32
)

bf2 = BedFrame(
    product_id="BF101",
    name="床架系列 B",
    category="床架",
    price=2229.75,
    package_dimension=(156.0, 38.8, 18.1),
    weight=43.5,
    stock=10,
    style="雙人床架 - (適用135x189cm床褥)",
    color="淺木色",
    material="鋼架",
    assembly_time=78
)

bf3 = BedFrame(
    product_id="BF102",
    name="床架系列 C",
    category="床架",
    price=1536.96,
    package_dimension=(140.9, 36.9, 23.7),
    weight=41.8,
    stock=7,
    style="雙人床架 - (適用135x189cm床褥)",
    color="深灰色",
    material="MDF纖維板",
    assembly_time=89
)

bf4 = BedFrame(
    product_id="BF103",
    name="床架系列 D",
    category="床架",
    price=2285.3,
    package_dimension=(147.3, 36.5, 23.3),
    weight=39.6,
    stock=3,
    style="特大雙人床架 - (適用150x200cm床褥)",
    color="黑色",
    material="MDF纖維板",
    assembly_time=36
)

bf5 = BedFrame(
    product_id="BF104",
    name="床架系列 E",
    category="床架",
    price=1885.52,
    package_dimension=(140.7, 37.7, 12.5),
    weight=58.6,
    stock=17,
    style="碌架床 - (適用92x189cm床褥,1或2張床褥)",
    color="白色",
    material="膠合板",
    assembly_time=66
)

bf6 = BedFrame(
    product_id="BF105",
    name="床架系列 F",
    category="床架",
    price=2760.42,
    package_dimension=(148.9, 41.4, 22.7),
    weight=30.9,
    stock=9,
    style="雙人床架 - (適用135x189cm床褥)",
    color="白色",
    material="鋼架",
    assembly_time=62
)

bf7 = BedFrame(
    product_id="BF106",
    name="床架系列 G",
    category="床架",
    price=2780.65,
    package_dimension=(153.4, 32.1, 14.4),
    weight=55.0,
    stock=10,
    style="雙人床架 - (適用135x189cm床褥)",
    color="淺木色",
    material="鋼架",
    assembly_time=31
)

bf8 = BedFrame(
    product_id="BF107",
    name="床架系列 H",
    category="床架",
    price=2743.87,
    package_dimension=(142.6, 37.1, 12.0),
    weight=59.8,
    stock=5,
    style="特別訂製雙人床 - (適用151cm或以上特別訂製床褥)",
    color="淺木色",
    material="金屬+木板",
    assembly_time=42
)

bf9 = BedFrame(
    product_id="BF108",
    name="床架系列 I",
    category="床架",
    price=1303.32,
    package_dimension=(157.0, 38.7, 24.9),
    weight=41.1,
    stock=0,
    style="雙人床架 - (適用135x189cm床褥)",
    color="白色",
    material="實木",
    assembly_time=84
)

bf10 = BedFrame(
    product_id="BF109",
    name="床架系列 J",
    category="床架",
    price=2579.33,
    package_dimension=(143.9, 33.4, 14.7),
    weight=39.1,
    stock=8,
    style="單人床架 - (適用92x189cm床褥)",
    color="深灰色",
    material="膠合板",
    assembly_time=72
)

bedframe_list = [bf1, bf2, bf3, bf4, bf5, bf6, bf7, bf8, bf9, bf10]

for i, bedFrame in enumerate(bedframe_list, 1):
    print(f"BedFrame : {bedFrame.name} - {bedFrame.category} - {bedFrame.style} - {bedFrame.material} - {bedFrame.color} - ${bedFrame.price:,.2f} ＊組裝時間估計需 {bedFrame.assembly_time} 分鐘，屬於{bedFrame.get_assembly_difficulty()}") #總結滙出

c1 = Chair(
    product_id="CH100",
    name="椅子系列 A",
    category="椅子",
    price=1479.29,
    package_dimension=(64.9, 48.1, 21.5),
    weight=9.6,
    stock=8,
    chair_type="餐椅",
    backrest_height="高椅背",
    armrest="連扶手",
    surface_type="真皮",
    material="塑膠",
    has_wheels=False,
    need_assembly=True,
    color="白色",
    has_headrest=False,
    adjustable_height=False
)

c2 = Chair(
    product_id="CH101",
    name="椅子系列 B",
    category="椅子",
    price=588.56,
    package_dimension=(88.4, 48.9, 24.8),
    weight=16.6,
    stock=19,
    chair_type="電腦椅",
    backrest_height="高椅背",
    armrest="連扶手",
    surface_type="無外皮",
    material="金屬",
    has_wheels=False,
    need_assembly=True,
    color="藍色",
    has_headrest=False,
    adjustable_height=True
)

c3 = Chair(
    product_id="CH102",
    name="椅子系列 C",
    category="椅子",
    price=375.36,
    package_dimension=(74.7, 52.6, 18.1),
    weight=10.4,
    stock=10,
    chair_type="辦公椅",
    backrest_height="低椅背",
    armrest="不連扶手",
    surface_type="仿皮",
    material="鋁合金",
    has_wheels=False,
    need_assembly=True,
    color="灰色",
    has_headrest=False,
    adjustable_height=False
)

c4 = Chair(
    product_id="CH103",
    name="椅子系列 D",
    category="椅子",
    price=1085.37,
    package_dimension=(89.5, 46.7, 17.3),
    weight=12.1,
    stock=15,
    chair_type="辦公椅",
    backrest_height="高椅背",
    armrest="連扶手",
    surface_type="仿皮",
    material="鋼+網布",
    has_wheels=True,
    need_assembly=False,
    color="灰色",
    has_headrest=False,
    adjustable_height=True
)

c5 = Chair(
    product_id="CH104",
    name="椅子系列 E",
    category="椅子",
    price=487.93,
    package_dimension=(63.0, 46.4, 13.5),
    weight=17.2,
    stock=12,
    chair_type="電腦椅",
    backrest_height="低椅背",
    armrest="連扶手",
    surface_type="真皮",
    material="塑膠",
    has_wheels=False,
    need_assembly=True,
    color="黑色",
    has_headrest=False,
    adjustable_height=False
)

c6 = Chair(
    product_id="CH105",
    name="椅子系列 F",
    category="椅子",
    price=604.35,
    package_dimension=(69.7, 58.0, 19.4),
    weight=14.9,
    stock=16,
    chair_type="電競椅",
    backrest_height="低椅背",
    armrest="不連扶手",
    surface_type="無外皮",
    material="鋼+網布",
    has_wheels=True,
    need_assembly=True,
    color="紅色",
    has_headrest=False,
    adjustable_height=False
)

c7 = Chair(
    product_id="CH106",
    name="椅子系列 G",
    category="椅子",
    price=404.75,
    package_dimension=(63.2, 46.6, 22.3),
    weight=13.5,
    stock=7,
    chair_type="餐椅",
    backrest_height="低椅背",
    armrest="連扶手",
    surface_type="真皮",
    material="鋼+網布",
    has_wheels=False,
    need_assembly=False,
    color="黑色",
    has_headrest=False,
    adjustable_height=True
)

c8 = Chair(
    product_id="CH107",
    name="椅子系列 H",
    category="椅子",
    price=425.42,
    package_dimension=(61.1, 52.0, 20.2),
    weight=8.4,
    stock=13,
    chair_type="電腦椅",
    backrest_height="高椅背",
    armrest="不連扶手",
    surface_type="仿皮",
    material="實木",
    has_wheels=True,
    need_assembly=False,
    color="灰色",
    has_headrest=False,
    adjustable_height=True
)

c9 = Chair(
    product_id="CH108",
    name="椅子系列 I",
    category="椅子",
    price=967.39,
    package_dimension=(67.0, 54.4, 24.2),
    weight=7.6,
    stock=5,
    chair_type="電競椅",
    backrest_height="低椅背",
    armrest="連扶手",
    surface_type="仿皮",
    material="塑膠",
    has_wheels=False,
    need_assembly=False,
    color="灰色",
    has_headrest=True,
    adjustable_height=False
)

c10 = Chair(
    product_id="CH109",
    name="椅子系列 J",
    category="椅子",
    price=1082.12,
    package_dimension=(81.1, 56.8, 10.8),
    weight=12.7,
    stock=17,
    chair_type="電腦椅",
    backrest_height="高椅背",
    armrest="不連扶手",
    surface_type="真皮",
    material="鋼+網布",
    has_wheels=True,
    need_assembly=False,
    color="藍色",
    has_headrest=False,
    adjustable_height=False
)

chair_list = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

for i, Chair in enumerate(chair_list, 1):
    print(f"Chair : {Chair.name} - {Chair.category} - {Chair.chair_type} - {Chair.material} - {Chair.color} - ${Chair.price:,.2f} ") #總結滙出

# 模擬加入購物籃的三件傢俬（任選）

item1 = mattress_list[0]   #每一個Class 簡一件
item2 = bedframe_list[8]
item3 = chair_list[9]

# 放入購物籃
shopping_cart = [item1, item2, item3]

# 計算總金額
total = sum(item.price for item in shopping_cart)

print(" ")
print("多謝選購以下物品! ") #只顯示一次的內容
for item in shopping_cart:
    print(f"\n {item.name} {item.category} (ID:{item.product_id}) x1件   HK${item.price:,.2f}")
print(f"\n\n 總共 {len(shopping_cart)}件傢俬，總金額為：HK${total:,.2f}")