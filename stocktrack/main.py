from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


DATABASE_URL = "sqlite:///./stocks.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class StockPrice(Base):
    __tablename__ = "stock_prices"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)


MOCK_STOCKS = {
    "AAPL": lambda: round(random.uniform(150, 200), 2),
    "GOOGL": lambda: round(random.uniform(2700, 3000), 2),
    "AMZN": lambda: round(random.uniform(3100, 3500), 2),
    "MSFT": lambda: round(random.uniform(290, 350), 2),
    "TSLA": lambda: round(random.uniform(600, 800), 2),
    "NFLX": lambda: round(random.uniform(450, 550), 2),
    "META": lambda: round(random.uniform(250, 300), 2),
    "NVDA": lambda: round(random.uniform(500, 700), 2),
    "INTC": lambda: round(random.uniform(30, 50), 2),
    "AMD": lambda: round(random.uniform(70, 120), 2),
}

class StockRequest(BaseModel):
    symbol: str

@app.post("/fetch_price/")
def fetch_stock_price(stock: StockRequest):
    symbol = stock.symbol.upper()
    if symbol not in MOCK_STOCKS:
        raise HTTPException(status_code=404, detail="Stock symbol not found")
    
    price = MOCK_STOCKS[symbol]()
    db = SessionLocal()
    new_stock = StockPrice(symbol=symbol, price=price)
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    db.close()
    return {"symbol": symbol, "price": price}

@app.get("/historical_prices/{symbol}")
def get_historical_prices(symbol: str):
    db = SessionLocal()
    prices = db.query(StockPrice).filter(StockPrice.symbol == symbol.upper()).order_by(StockPrice.timestamp.desc()).limit(5).all()
    db.close()
    return [{"id": p.id, "symbol": p.symbol, "price": p.price, "timestamp": p.timestamp} for p in prices]
