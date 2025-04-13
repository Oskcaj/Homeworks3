#這是產品入庫的流程
from sqlmodel import Session, select, create_engine
from ikea_models import Mattress, BedFrame, Chair

# 建立資料庫對接（直接在DATABASE運作)
engine = create_engine("sqlite:///ikea.db")

def update_stock(product_id: str, quantity: int):
    with Session(engine) as session:
        # 建立類別清單
        product_classes = [Mattress, BedFrame, Chair]
        product = None
        product_type = ""

        # 一次搜尋所有類別 (本身分了3個CLASS，現在統一處理)
        for cls in product_classes:
            result = session.exec(select(cls).where(cls.product_id == product_id)).first()
            if result:
                product = result
                product_type = cls.__name__  # 自動讀出類別名稱
                break

        if product:
            product.stock += quantity
            session.add(product)
            session.commit()

            # 類別中文對照
            type_map = {
                "Mattress": "床褥",
                "BedFrame": "床架",
                "Chair": "椅子"
            }

            zh_type = type_map.get(product_type, "未知類別")
            print(f"✅ 已更新 [{zh_type}] {product.name}（ID: {product.product_id}）的庫存為：{product.stock}")
        else:
            print("❌ 找不到對應的產品 ID，請確認輸入是否正確。")

# 📝 使用教學提示
if __name__ == "__main__":
    print("📦 IKEA 入庫系統")
    print("請輸入商品 ID 及要新增的庫存數量")
    print("例如：BF101 5  表示將 BF101 增加 5 件庫存")

    try:
        user_input = input("請輸入格式（商品ID 數量）：").strip().split()
        if len(user_input) != 2:
            raise ValueError("輸入格式錯誤，請輸入：商品ID 數量（例如 BF101 5）")

        product_id = user_input[0]
        quantity = int(user_input[1])

        update_stock(product_id, quantity)

    except Exception as e:
        print(f"⚠️ 錯誤：{e}")
