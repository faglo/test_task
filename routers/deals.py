from fastapi import APIRouter, UploadFile, Depends
from app import csv_to_json
from db.engine import get_db
from sqlalchemy.orm import Session
from sqlalchemy import exists
from db.models import User

router = APIRouter(
    prefix="/deals",
    tags=["deals"],
)

# Converts SQLAlchemy object to dict
def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = getattr(row, column.name)

    return d

@router.post("/")
async def upload_deals(deals: UploadFile, db: Session = Depends(get_db)):
    if deals.filename.split(".")[-1] != "csv":
        return {
            "status": "error",
            "desc": "Invalid file extension",
        }
    
    try:
        deals_json = csv_to_json.parse(deals.file.read().decode("utf-8"))
        for deal in deals_json:

            if db.query(exists().where(User.name == deal['customer'])).one()[0]:
                user = db.query(User).filter(User.name == deal['customer']).first()
                
                # Add gem in user gem list if not exists
                if not db.query(exists().where(User.name == deal['customer'], User.gems.contains([deal['item']]))).one()[0]:
                    user.gems = [*user.gems, deal['item']]
                
                user.spent_money += int(deal['total'])
                
            else:
                prepared = User(
                    name=deal['customer'],
                    spent_money=int(deal['total']),
                    gems=[deal['item']],
                )
                db.add(prepared)
            db.commit()
    except Exception as e:
        return {
            "status": "error",
            "desc": str(e.with_traceback(e.__traceback__)),
        }
    return {"status": "ok"}


@router.get("/")
async def get_top_deals(db: Session = Depends(get_db)):
    top_spend = db.query(User).order_by(User.spent_money.desc()).limit(5).all()
    gem_data = dict()
    result_data = []

    # Count all gems
    for user in top_spend:
        for gem in list(user.gems):
            try:
                gem_data[gem] += 1
            except KeyError:
                gem_data.update({gem: 1})

    # Select needed gems
    for user in top_spend:
        gems = []
        user = row2dict(user)
        for gem in user['gems']:
            if gem_data[gem] >= 2:
                gems.append(gem)
        
        user['gems'] = gems
        result_data.append(user)

    return {"response": result_data}
