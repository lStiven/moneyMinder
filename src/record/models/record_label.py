from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.base.models import BaseModel
from src.record.constants import RECORD_LABEL_TABLE_NAME


class RecordLabel(BaseModel):
    __tablename__ = RECORD_LABEL_TABLE_NAME

    record_id: Mapped[int] = mapped_column(ForeignKey("record.id"))
    label_id: Mapped[int] = mapped_column(ForeignKey("label.id"))
    record: Mapped["Record"] = relationship("Record", lazy="selectin")
    label: Mapped["Label"] = relationship("Label", lazy="selectin")
