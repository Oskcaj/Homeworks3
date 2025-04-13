#主類別及子類別
from sqlmodel import SQLModel, Field
from typing import Optional

# 主類別：資料由子類別丞繼。子類別才用TRUE，真正產品資料列表
class IkeaFurnitureBase(SQLModel, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: str
    name: str
    category: str
    price: float
    package_dimension: Optional[str] = Field(default="未提供") #硬顯示出資料，不是數字或變數，及可留空
    length: Optional[float] = Field(default=None) #成品後數值,可留空
    width: Optional[float] = Field(default=None) #成品後數值,可留空
    height: Optional[float] = Field(default=None) #成品後數值,可留空
    weight: Optional[float] = Field(default=None) #成品後數值,可留空
    stock: int

# 子類別 1：床褥
class Mattress(IkeaFurnitureBase, table=True):
    material: str
    warranty: int
    firmness: str
    feature: str

# 子類別 2：床架
class BedFrame(IkeaFurnitureBase, table=True):
    style: str
    color: str
    material: str
    assembly_time: int

# 子類別 3：椅子
class Chair(IkeaFurnitureBase, table=True):
    chair_type: str
    backrest_height: str
    armrest: str
    surface_type: str
    material: str
    has_wheels: bool
    need_assembly: bool
    color: str
    has_headrest: bool
    adjustable_height: bool
