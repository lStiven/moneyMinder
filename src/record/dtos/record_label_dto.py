from dataclasses import dataclass

from src.base.models import BaseDtoModel
from src.record.models import RecordLabel
from src.record.schemas.record_label_schema import RecordLabelSchema


@dataclass
class RecordLabelDto(BaseDtoModel):
    record_id: int
    label_id: int

    @classmethod
    def from_schema(cls, schema: RecordLabelSchema):
        return cls(
            id=None,
            record_id=schema.record_id,
            label_id=schema.label_id,
            is_active=None,
            created_at=None,
            updated_at=None,
            created_by=None,
            updated_by=None,
        )

    @classmethod
    def from_model(cls, model: RecordLabel):
        return cls(
            id=model.id,
            record_id=model.record_id,
            label_id=model.label_id,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by,
            updated_by=model.updated_by,
        )

    def to_model(self) -> RecordLabel:
        return RecordLabel(
            id=self.id,
            record_id=self.record_id,
            label_id=self.label_id,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
            created_by=self.created_by,
            updated_by=self.updated_by,
        )

    def to_dict(self):
        return self.__dict__
