from fastapi import FastAPI
from routes.index import property_

""" Main APP Run """

def create_application() -> FastAPI:
    """Create application object."""
    app = FastAPI()
    app.include_router(property_)
    return app
    
app = create_application()
