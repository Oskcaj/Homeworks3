# read_database.py 自我查看產品資料
from sqlmodel import Session, select, create_engine
from ikea_models import Mattress, BedFrame, Chair

sqlite_file_name = "ikea.db"
engine = create_engine(f"sqlite:///{sqlite_file_name}", echo=False)   #避免直接用 MAIN. 應該讀返DB

with Session(engine) as session:
    print("🔹 所有床褥（Mattress）:")
    mattresses = session.exec(select(Mattress)).all()
    for item in mattresses:
        print(f"{item.product_id} - {item.name} - HKD ${item.price} - 現在存貨{item.stock}")

with Session(engine) as session:
    bedframes = session.exec(select(BedFrame)).all()
    print("🔹 所有床架（BedFrame）完整資料：\n")
    for b in bedframes:
        print(b)

    print("\n🔹 所有椅子（Chair）:")
    chairs = session.exec(select(Chair)).all()
    for item in chairs:
        print(f"{item.product_id} - {item.name} - HKD{item.price} - {item.category} - {item.chair_type} - 運用尺寸{item.package_dimension} - 現在存貨 {item.stock}")
