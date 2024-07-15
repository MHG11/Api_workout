from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from configs.database import get_session
from fastapi import Depends


DatabaseDependencies = Annotated[AsyncSession, Depends(get_session)]