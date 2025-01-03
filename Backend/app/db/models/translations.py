import uuid
from sqlalchemy import Column, String, ForeignKey, TIMESTAMP, UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Translation(Base):
    __tablename__ = 'translations'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
    
    text = Column(String, nullable=False)
    translated_text = Column(String, nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship('User', back_populates='translations')