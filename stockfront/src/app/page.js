"use client";
import { useState } from 'react';

export default function Home() {
  const [symbol, setSymbol] = useState('');
  const [latestPrice, setLatestPrice] = useState(null);
  const [historicalPrices, setHistoricalPrices] = useState([]);

  const fetchStockPrice = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/fetch_price/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ symbol }),
      });

      if (response.status === 404) {
        setSymbol("");
        setLatestPrice(null);
        setHistoricalPrices([]);
        alert("No stock with provided symbol found");
        return;
      }

      const data = await response.json();
      setLatestPrice(data);

      const historicalResponse = await fetch(`http://127.0.0.1:8000/historical_prices/${symbol}`);
      const historicalData = await historicalResponse.json();
      setHistoricalPrices(historicalData);

    } catch (error) {
      console.log('Error fetching stock data:', error);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Stock Price Fetcher</h1>
      <input
        type="text"
        placeholder="Enter stock symbol (e.g., AAPL)"
        value={symbol}
        onChange={(e) => setSymbol(e.target.value)}
      />
      <button onClick={fetchStockPrice}>Fetch Price</button>

      {latestPrice !== null && (
        <div>
          <h2>Latest Price: ${latestPrice.price}</h2>
        </div>
      )}

      {historicalPrices.length > 0 && (
        <div>
          <h3>Last 5 Historical Prices:</h3>
          <ul>
            {historicalPrices.map((item) => (
              <li key={item.id}>
                ${item.price} (at {new Date(item.timestamp).toLocaleString()})
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
