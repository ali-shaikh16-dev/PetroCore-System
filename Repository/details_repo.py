from sqlalchemy.orm import Session
from Model.detail_table import Profile
from Schemas.details_schm import ProfileCreate, ProfileUpdate


#* =========================
# Create Profile
#* =========================

def create_profile(db: Session, profile_data: ProfileCreate):
    new_profile = Profile(**profile_data.model_dump())

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return new_profile


#* =========================
# Get All Profiles
#* =========================

def fetch_all_profiles(db):
    return db.query(Profile).all()


#* =========================
# Get Profile By ID
#* =========================


def get_profile_by_id(db: Session, profile_id: int):
    return db.query(Profile).filter(Profile.id == profile_id).first()



#* =========================
# Update Profile (PATCH)
#* =========================

def update_profile(db: Session, profile_id: int, profile_data: ProfileUpdate):
    
    profile = db.query(Profile).filter(Profile.id == profile_id).first()

    if not profile:
        return None

    #* Sirf wahi fields aayengi jo user ne bheji hain
    update_data = profile_data.model_dump(exclude_unset=True)

    #* Dynamic update
    for key, value in update_data.items():
        setattr(profile, key, value)

    db.commit()
    db.refresh(profile)

    return profile


#* =========================
# Delete Profile
#* =========================

def delete_profile(db: Session, profile_id: int):
    profile = db.query(Profile).filter(Profile.id == profile_id).first()

    if not profile:
        return None

    db.delete(profile)
    db.commit()

    return profile