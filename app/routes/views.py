from flask import Blueprint, jsonify, render_template
import requests

crypto = Blueprint('crypto', __name__)

@crypto.route('/crypto')
def get_crypto_data():
    
    quantities = {
        "DOGEUSDT": {"qnt": 365.87, "value_invest": 0.104, "max_historica": 0.73, "spent": 38.05},
        "ADAUSDT": {"qnt": 173.93, "value_invest": 0.350, "max_historica": 3.09, "spent": 60.88},
        "SHIBUSDT": {"qnt": 5597719.49, "value_invest": 0.000014, "max_historica": 0.000086, "spent": 78.37},
        "GALAUSDT": {"qnt": 4505.34, "value_invest": 0.018, "max_historica": 0.82, "spent": 80.65},
        "MANAUSDT": {"qnt": 73.91, "value_invest": 0.274, "max_historica": 5.85, "spent": 20.24},
        "DOTUSDT": {"qnt": 11.98, "value_invest": 3.970, "max_historica": 54.98, "spent": 47.56},
        "SANDUSDT": {"qnt": 80.89, "value_invest": 0.249, "max_historica": 8.4, "spent": 20.17},
        "LUNCUSDT": {"qnt": 192170.24, "value_invest": 0.000081, "max_historica": 0.0009, "spent": 15.50},
        "DYDXUSDT": {"qnt": 28.36, "value_invest": 0.960, "max_historica": 4.52, "spent": 27.23},
        "SXPUSDT": {"qnt": 153.00, "value_invest": 0.280, "max_historica": 5.79, "spent": 42.84},
        "FLOWUSDT": {"qnt": 137.44, "value_invest": 0.518, "max_historica": 42.4, "spent": 71.19},
        "ATOMUSDT": {"qnt": 4.22, "value_invest": 4.787, "max_historica": 44.45, "spent": 20.20},
        "CRVUSDT": {"qnt": 330.00, "value_invest": 0.272, "max_historica": 15.37, "spent": 89.80},
        "RVNUSDT": {"qnt": 2002.25, "value_invest": 0.017, "max_historica": 0.29, "spent": 34.44},
        "LINKUSDT": {"qnt": 2.19, "value_invest": 11.680, "max_historica": 52.7, "spent": 25.58},
        "OPUSDT": {"qnt": 13.76, "value_invest": 1.453, "max_historica": 4.84, "spent": 20.00},
        "SNXUSDT": {"qnt": 14.58, "value_invest": 1.400, "max_historica": 28.53, "spent": 20.41},
        "POLUSDT": {"qnt": 287.16, "value_invest": 0.350, "max_historica": 1.29, "spent": 100.51},
        "GMXUSDT": {"qnt": 4.19, "value_invest": 24.64, "max_historica": 91.07, "spent": 103.24},
        "1MBABYDOGEUSDT": {"qnt": 22008.36, "value_invest": 0.0023, "max_historica": 0.0063, "spent": 50.62},
        "BNBUSDT": {"qnt": 0.0048, "value_invest": 625.00, "max_historica": 720, "spent": 3.00},
        "ASTRUSDT": {"qnt": 1925.69, "value_invest": 0.065, "max_historica": 0.42, "spent": 126.05},
        "FETUSDT": {"qnt": 23.51, "value_invest": 1.56, "max_historica": 3.45, "spent": 36.61},
        "FDUSDUSDT": {"qnt": 1.14, "value_invest": 1.00, "max_historica": 1, "spent": 1.14},
        "USDCUSDT": {"qnt": 0.00, "value_invest": 0.000, "max_historica": 1, "spent": 0.00},
        "TRXUSDT": {"qnt": 23.66, "value_invest": 0.060, "max_historica": 0.23, "spent": 1.42},
        "THEUSDT": {"qnt": 31.70, "value_invest": 1.798, "max_historica": 4.03, "spent": 57.00},
        "SOLUSDT": {"qnt": 0.02355, "value_invest": 223.779, "max_historica": 263.21, "spent": 5.27},
        "CAKEUSDT": {"qnt": 36.88, "value_invest": 2.03, "max_historica": 43.96, "spent": 74.86},
        "PENDLEUSDT": {"qnt": 27.78, "value_invest": 3.42, "max_historica": 7.50, "spent": 95.00},
        "PHAUSDT": {"qnt": 549, "value_invest": 0.091, "max_historica": 1.39, "spent": 50.00}
    }
    
    cryptocurrencies = list(quantities.keys())
    crypto_data = []
    resultado_total = []
    resultado_total_lucro = 0
    resultado_total_perc = 0
    resultado_ganho = 0
    resultado_ganho_perc = 0
    resultado_perda = 0
    resultado_perda_perc = 0
    resultado_total_atual = 0
    valor_total_investido = 0
    valor_total_atual = 0
    
    for symbol in cryptocurrencies:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            data = response.json()
            name = data.get("symbol", "N/A").replace("USDT", "")
            price = data.get("price", "N/A")
            qnt = quantities.get(symbol, {}).get("qnt", 0)
            value_invest = quantities.get(symbol, {}).get("value_invest", 0)
            max_historica = quantities.get(symbol, {}).get("max_historica", 0)
            spent = quantities.get(symbol, {}).get("spent", 0)
            valor_atual = round(float(price) * float(qnt), 2)
            lucro = round((((float(price) * float(qnt)) - float(spent))), 2)
            percentual = round((((float(price) - float(value_invest)) / float(value_invest)) * 100), 2) if value_invest > 0 else 0
            resultado_total_lucro += lucro
            valor_total_investido += spent
            valor_total_atual += valor_atual
            
            if lucro >= 0:
                resultado_ganho += lucro
                
            else:
                resultado_perda += lucro
                
            
            crypto_data.append({"name": name, "price": price, "qnt": qnt, "value_invest": value_invest,
                                "max_historica": max_historica, "spent": spent,"valor_atual":valor_atual,
                                "lucro": lucro, "percentual": percentual})
            
            crypto_data.sort(key=lambda x: float(x["percentual"]), reverse=True)
            
        else:
            crypto_data.append({"name": symbol.replace("USDT", ""), "price": "Error fetching data"})
            
    resultado_ganho_perc = round((resultado_ganho / valor_total_investido) * 100, 2) if valor_total_investido > 0 else 0
    resultado_perda_perc = round((resultado_perda / valor_total_investido) * 100, 2) if valor_total_investido > 0 else 0
    resultado_total_perc = round((resultado_total_lucro / valor_total_investido) * 100, 2) if valor_total_investido > 0 else 0
    valor_total_investido = round(valor_total_investido, 2)
    valor_total_atual = round(valor_total_atual, 2)
    resultado_ganho = round(resultado_ganho, 2)
    resultado_perda = round(resultado_perda, 2)
    resultado_total_lucro = round(resultado_total_lucro, 2)
    resultado_total.append({"valor_total_investido": valor_total_investido, "valor_total_atual": valor_total_atual,
                            "resultado_ganho": resultado_ganho, "resultado_perda": resultado_perda,
                            "resultado_ganho_perc": resultado_ganho_perc, "resultado_perda_perc": resultado_perda_perc,
                            "resultado_total_lucro": resultado_total_lucro, "resultado_total_perc": resultado_total_perc})
    
    return render_template("crypto.html", context={"cryptocurrencies": crypto_data, "resultado_total": resultado_total})

@crypto.route('/crypto/precos')
def get_crypto_prices():
    quantities = {
        "DOGEUSDT": {"qnt": 365.87, "value_invest": 0.104, "max_historica": 0.73, "spent": 38.05},
        "ADAUSDT": {"qnt": 173.93, "value_invest": 0.350, "max_historica": 3.09, "spent": 60.88},
        "SHIBUSDT": {"qnt": 5597719.49, "value_invest": 0.000014, "max_historica": 0.000086, "spent": 78.37},
        "GALAUSDT": {"qnt": 4505.34, "value_invest": 0.018, "max_historica": 0.82, "spent": 80.65},
        "MANAUSDT": {"qnt": 73.91, "value_invest": 0.274, "max_historica": 5.85, "spent": 20.24},
        "DOTUSDT": {"qnt": 11.98, "value_invest": 3.970, "max_historica": 54.98, "spent": 47.56},
        "SANDUSDT": {"qnt": 80.89, "value_invest": 0.249, "max_historica": 8.4, "spent": 20.17},
        "LUNCUSDT": {"qnt": 192170.24, "value_invest": 0.000081, "max_historica": 0.0009, "spent": 15.50},
        "DYDXUSDT": {"qnt": 28.36, "value_invest": 0.960, "max_historica": 4.52, "spent": 27.23},
        "SXPUSDT": {"qnt": 153.00, "value_invest": 0.280, "max_historica": 5.79, "spent": 42.84},
        "FLOWUSDT": {"qnt": 137.44, "value_invest": 0.518, "max_historica": 42.4, "spent": 71.19},
        "ATOMUSDT": {"qnt": 4.22, "value_invest": 4.787, "max_historica": 44.45, "spent": 20.20},
        "CRVUSDT": {"qnt": 330.00, "value_invest": 0.272, "max_historica": 15.37, "spent": 89.80},
        "RVNUSDT": {"qnt": 2002.25, "value_invest": 0.017, "max_historica": 0.29, "spent": 34.44},
        "LINKUSDT": {"qnt": 2.19, "value_invest": 11.680, "max_historica": 52.7, "spent": 25.58},
        "OPUSDT": {"qnt": 13.76, "value_invest": 1.453, "max_historica": 4.84, "spent": 20.00},
        "SNXUSDT": {"qnt": 14.58, "value_invest": 1.400, "max_historica": 28.53, "spent": 20.41},
        "POLUSDT": {"qnt": 287.16, "value_invest": 0.350, "max_historica": 1.29, "spent": 100.51},
        "GMXUSDT": {"qnt": 4.19, "value_invest": 24.64, "max_historica": 91.07, "spent": 103.24},
        "1MBABYDOGEUSDT": {"qnt": 22008.36, "value_invest": 0.0023, "max_historica": 0.0063, "spent": 50.62},
        "BNBUSDT": {"qnt": 0.0048, "value_invest": 625.00, "max_historica": 720, "spent": 3.00},
        "ASTRUSDT": {"qnt": 1925.69, "value_invest": 0.065, "max_historica": 0.42, "spent": 126.05},
        "FETUSDT": {"qnt": 23.51, "value_invest": 1.56, "max_historica": 3.45, "spent": 36.61},
        "FDUSDUSDT": {"qnt": 1.14, "value_invest": 1.00, "max_historica": 1, "spent": 1.14},
        "USDCUSDT": {"qnt": 0.00, "value_invest": 0.000, "max_historica": 1, "spent": 0.00},
        "TRXUSDT": {"qnt": 23.66, "value_invest": 0.060, "max_historica": 0.23, "spent": 1.42},
        "THEUSDT": {"qnt": 31.70, "value_invest": 1.798, "max_historica": 4.03, "spent": 57.00},
        "SOLUSDT": {"qnt": 0.02355, "value_invest": 223.779, "max_historica": 263.21, "spent": 5.27},
        "CAKEUSDT": {"qnt": 36.88, "value_invest": 2.03, "max_historica": 43.96, "spent": 74.86},
        "PENDLEUSDT": {"qnt": 27.78, "value_invest": 3.42, "max_historica": 7.50, "spent": 95.00},
        "PHAUSDT": {"qnt": 549, "value_invest": 0.091, "max_historica": 1.39, "spent": 50.00}
    }
    cryptocurrencies = list(quantities.keys())
    prices = []
    for symbol in cryptocurrencies:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            data = response.json()
            name = data.get("symbol", "N/A").replace("USDT", "")
            price = data.get("price", "N/A")
            prices.append({"name": name, "price": price})
        else:
            prices.append({"name": symbol.replace("USDT", ""), "price": None})
    return jsonify(prices)

