"""Base models for the application with common functionality like timestamps."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TimestampedModel(BaseModel):
    """Base model with timestamp fields for tracking creation and update times."""

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
