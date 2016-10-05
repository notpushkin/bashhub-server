import os
from asphalt.core import ContainerComponent, Context
from kyoukai import KyoukaiComponent
from asphalt.sqlalchemy.component import SQLAlchemyComponent

from . import app


class AppContainer(ContainerComponent):
    async def start(self, ctx: Context):
        self.add_component("kyoukai", KyoukaiComponent, app=app,
                           ip=os.getenv("HOST", "127.0.0.1"),
                           port=int(os.getenv("PORT", "2274")))
        self.add_component("sqlalchemy", SQLAlchemyComponent,
                           metadata="bashhub_server.models:Base.metadata",
                           url=os.getenv("DATABASE_URL", "sqlite:///test.db"))

        await super().start(ctx)
