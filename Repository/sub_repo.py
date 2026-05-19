from sqlalchemy.orm import Session
from Model.sub_table import Subscription
from Schemas.sub_schm import SubscriptionCreate

def create_subscription(db: Session , subrip: SubscriptionCreate):
    create_sub = Subscription(**subrip.model_dump())
    
    db.add(create_sub)
    db.commit()
    db.refresh(create_sub) 
    return create_sub

def get_subscription_by_user_id(db: Session , user_id: int):
    return db.query(Subscription).filter(Subscription.user_id == user_id).all()


def update_subscription_status(db: Session , subscription_id: int , new_status: str):
    subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if subscription:
        subscription.status = new_status
        db.commit()
        db.refresh(subscription)
        return {"message": "Subscription status updated successfully" , "subscription": subscription}
    return {"error": "Subscription not found"}

