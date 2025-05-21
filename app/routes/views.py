from flask import Blueprint, jsonify
import requests
from flask import render_template

crypto = Blueprint('crypto', __name__)

@crypto.route('/crypto')
def get_crypto_data():
    # cryptocurrencies = [
    #     "FLOWUSDT", "CRVUSDT", "GALAUSDT", "SANDUSDT", "MANAUSDT", "SXPUSDT", "SNXUSDT",
    #     "RVNUSDT", "DOTUSDT", "LUNCUSDT", "ATOMUSDT", "ADAUSDT", "DOGEUSDT", "SHIBUSDT",
    #     "ASTRUSDT", "DYDXUSDT", "LINKUSDT", "GMXUSDT", "POLUSDT", "OPUSDT", "1MBABYDOGEUSDT",
    #     "FETUSDT", "BNBUSDT", "FDUSDUSDT", "USDCUSDT", "USDTBRL", "TRXUSDT", "THEUSDT",
    #     "SOLUSDT", "CAKEUSDT"
    # ]
    quantities = {
        "DOGEUSDT": {"qnt": 365.87, "avg_cost": 0.104, "max_historica": 0.73, "spent": 38.05},
        "ADAUSDT": {"qnt": 173.93, "avg_cost": 0.350, "max_historica": 3.09, "spent": 60.88},
        "SHIBUSDT": {"qnt": 5597719.49, "avg_cost": 0.000014, "max_historica": 0.000086, "spent": 78.37},
        "GALAUSDT": {"qnt": 4505.34, "avg_cost": 0.018, "max_historica": 0.82, "spent": 80.65},
        "MANAUSDT": {"qnt": 73.91, "avg_cost": 0.274, "max_historica": 5.85, "spent": 20.24},
        "DOTUSDT": {"qnt": 11.98, "avg_cost": 3.970, "max_historica": 54.98, "spent": 47.56},
        "SANDUSDT": {"qnt": 80.89, "avg_cost": 0.249, "max_historica": 8.4, "spent": 20.17},
        "LUNCUSDT": {"qnt": 192170.24, "avg_cost": 0.000081, "max_historica": 0.0009, "spent": 15.50},
        "DYDXUSDT": {"qnt": 28.36, "avg_cost": 0.960, "max_historica": 4.52, "spent": 27.23},
        "SXPUSDT": {"qnt": 153.00, "avg_cost": 0.280, "max_historica": 5.79, "spent": 42.84},
        "FLOWUSDT": {"qnt": 137.44, "avg_cost": 0.518, "max_historica": 42.4, "spent": 71.19},
        "ATOMUSDT": {"qnt": 4.22, "avg_cost": 4.787, "max_historica": 44.45, "spent": 20.20},
        "CRVUSDT": {"qnt": 330.00, "avg_cost": 0.272, "max_historica": 15.37, "spent": 89.80},
        "RVNUSDT": {"qnt": 2002.25, "avg_cost": 0.017, "max_historica": 0.29, "spent": 34.44},
        "LINKUSDT": {"qnt": 2.19, "avg_cost": 11.680, "max_historica": 52.7, "spent": 25.58},
        "OPUSDT": {"qnt": 13.76, "avg_cost": 1.453, "max_historica": 4.84, "spent": 20.00},
        "SNXUSDT": {"qnt": 14.58, "avg_cost": 1.400, "max_historica": 28.53, "spent": 20.41},
        "POLUSDT": {"qnt": 287.16, "avg_cost": 0.350, "max_historica": 1.29, "spent": 100.51},
        "GMXUSDT": {"qnt": 4.19, "avg_cost": 24.64, "max_historica": 91.07, "spent": 103.24},
        "1MBABYDOGEUSDT": {"qnt": 22008.36, "avg_cost": 0.0023, "max_historica": 0.0063, "spent": 50.62},
        "BNBUSDT": {"qnt": 0.0048, "avg_cost": 625.00, "max_historica": 720, "spent": 3.00},
        "ASTRUSDT": {"qnt": 1925.69, "avg_cost": 0.065, "max_historica": 0.42, "spent": 126.05},
        "FETUSDT": {"qnt": 23.51, "avg_cost": 1.56, "max_historica": 3.45, "spent": 36.61},
        "FDUSDUSDT": {"qnt": 1.14, "avg_cost": 1.00, "max_historica": 1, "spent": 1.14},
        "USDCUSDT": {"qnt": 0.00, "avg_cost": 0.000, "max_historica": 1, "spent": 0.00},
        "TRXUSDT": {"qnt": 23.66, "avg_cost": 0.060, "max_historica": 0.23, "spent": 1.42},
        "THEUSDT": {"qnt": 31.70, "avg_cost": 1.798, "max_historica": 4.03, "spent": 57.00},
        "SOLUSDT": {"qnt": 0.02355, "avg_cost": 223.779, "max_historica": 263.21, "spent": 5.27},
        "CAKEUSDT": {"qnt": 36.88, "avg_cost": 2.03, "max_historica": 43.96, "spent": 74.86}
    }
    
    cryptocurrencies = list(quantities.keys())
    crypto_data = []
    for symbol in cryptocurrencies:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            name = data.get("symbol", "N/A").replace("USDT", "")
            price = data.get("price", "N/A")
            qnt = quantities.get(symbol, {}).get("qnt", 0)
            avg_cost = quantities.get(symbol, {}).get("avg_cost", 0)
            max_historica = quantities.get(symbol, {}).get("max_historica", 0)
            spent = quantities.get(symbol, {}).get("spent", 0)
            lucro = (float(price) * float(qnt)) - float(spent)
            percentual = ((float(price) - float(avg_cost)) / float(avg_cost)) * 100 if avg_cost > 0 else 0
            crypto_data.append({"name": name, "price": price, "qnt": qnt, "avg_cost": avg_cost,
                                "max_historica": max_historica, "spent": spent, "lucro": lucro, 
                                "percentual": percentual})
            
            crypto_data.sort(key=lambda x: float(x["percentual"]), reverse=True)
            
        else:
            crypto_data.append({"name": symbol.replace("USDT", ""), "price": "Error fetching data"})
    return render_template("crypto.html", context={"cryptocurrencies": crypto_data})