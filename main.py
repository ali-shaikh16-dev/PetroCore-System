from fastapi import FastAPI
from Router.login_api import router as auth_router
from Router.fuel_api import router as fuel_router
from Router.sale_api import router as sale_router
from Router.user_api import router as user_router
from Router.detail_api import router as detail_router
from Router.start_api import router as start_router


#* Building
app = FastAPI()

#* TABLE CREATION CODE 
app.include_router(start_router)


#* ROOM 1 WORK login and signup
app.include_router(auth_router , prefix="/auth" , tags=["Auth Opretion - Signup-(Admin) & Login-(Open free)"])


#* ROOM 2 WORK User CRUD operations
app.include_router(user_router , prefix="/user" , tags=["Users Opretion - Admin & Owner"])


#* ROOM 3 WORK Fuel CRUD operations
app.include_router(fuel_router , prefix="/fuel" , tags=["Fuel Opretion - Admin & Owner"])


#* ROOM 4 WORK sale logic-based
app.include_router(sale_router , prefix="/sale" , tags=["Sale Opretion - (SaleCheck-Admin) & Sale-Worker"])


#* ROOM 5 WORK Profile
app.include_router(detail_router, prefix="/details" , tags=["Worker Details - Admin & Owner"])

