# Shopping Cart
from sqlmodel import Session, select, create_engine
from ikea_models import Mattress, BedFrame, Chair

# 建立資料庫對接
engine = create_engine("sqlite:///ikea.db", echo=False)

# 設定支持的產品類別
product_classes = [Mattress, BedFrame, Chair]

def find_product(product_id):
    for cls in product_classes:
        with Session(engine) as session:
            product = session.exec(select(cls).where(cls.product_id == product_id)).first()
            if product:
                return product, cls
    return None, None

def process_purchase(purchase_list: list[tuple[str, int]]):
    total = 0.0
    purchase_summary = []
    session = Session(engine)
    try:
        # 驗證所有產品是否存在與庫存足夠
        for product_id, qty in purchase_list:
            product, cls = find_product(product_id)
            if not product:
                raise ValueError(f"❌ 輸入的產品ID： {product_id} 找不到對應的產品。")
            if product.stock < qty:
                raise ValueError(f"❌ 產品ID： {product_id} 產品名稱：{product.name} 因存貨不足，目前庫存：{product.stock}")

        # 全部產品驗證通過後，開始扣庫存與統計
        for product_id, qty in purchase_list:
            product, cls = find_product(product_id)
            product.stock -= qty
            session.add(product)
            subtotal = product.price * qty
            total += subtotal
            purchase_summary.append((product.name, qty, product.price, subtotal))

        session.commit()
        print("\n✅ 訂單已成功處理，以下是訂單明細：\n")
        for name, qty, unit_price, subtotal in purchase_summary:
            print(f"產品ID ： {product.id} 產品名稱 ： {name} × {qty} 件，每件 HKD ${unit_price} ，小計：HKD ${subtotal:.2f} ")
        print(f"\n💰 訂單總金額：HKD ${total:.2f} ")
    except ValueError as ve:
        session.rollback()
        print(f"\n⚠️ 錯誤：{ve}\n❌ 訂單未處理，請檢查後再重新輸入。")
    finally:
        session.close()

# 📝 使用說明
if __name__ == "__main__":
    print("📥 請輸入要購買的商品資料（格式：產品ID 數量， 購買單件例子：903.195.12 2    購買多件例子：BF101 1 CH105 3 BF103 18）")
    user_input = input("➡ 請輸入商品ID與數量：\n").strip()
    items = user_input.split()

    if len(items) % 2 != 0:
        print("❌ 輸入格式錯誤，請確認每個 產品ID 後跟著一個正數數量")
    else:
        try:
            purchase_data = [(items[i], int(items[i+1])) for i in range(0, len(items), 2)]
            process_purchase(purchase_data)
        except Exception as e:
            print("❌ 錯誤：", e)
            
