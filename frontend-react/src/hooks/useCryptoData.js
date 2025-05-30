import { useState, useEffect } from "react";

export function useCryptoData() {
  const [cryptos, setCryptos] = useState([]);
  const [result_total, setResultTotal] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchData = async () => {
    try {
      const res = await fetch("http://localhost:5001/crypto/precos");
      const data = await res.json();
      setCryptos(data.cryptos.map((crypto, idx) => ({ id: idx, ...crypto })));
      setResultTotal(data.result_total);
      setLoading(false);
    } catch (e) {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 5000);
    return () => clearInterval(interval);
  }, []);

  return { cryptos, result_total, loading };
}