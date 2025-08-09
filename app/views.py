import requests
import time
from decimal import Decimal

walletBinance = {
    "DOGEUSDT": {"qnt": 365.87, "middlePrice": 0.104, "maxHistoric": 0.73, "investValue": 38.05},
    "ADAUSDT": {"qnt": 173.93, "middlePrice": 0.350, "maxHistoric": 3.09, "investValue": 60.88},
    "SHIBUSDT": {"qnt": 5597719.49, "middlePrice": 0.000014, "maxHistoric": 0.000086, "investValue": 78.37},
    "GALAUSDT": {"qnt": 4505.34, "middlePrice": 0.018, "maxHistoric": 0.82, "investValue": 80.65},
    "MANAUSDT": {"qnt": 73.91, "middlePrice": 0.274, "maxHistoric": 5.85, "investValue": 20.24},
    "DOTUSDT": {"qnt": 13.2, "middlePrice": 3.980, "maxHistoric": 54.98, "investValue": 51.98},
    "SANDUSDT": {"qnt": 80.89, "middlePrice": 0.249, "maxHistoric": 8.4, "investValue": 20.17},
    "LUNCUSDT": {"qnt": 192170.24, "middlePrice": 0.000081, "maxHistoric": 0.0009, "investValue": 15.50},
    "DYDXUSDT": {"qnt": 28.36, "middlePrice": 0.960, "maxHistoric": 4.52, "investValue": 27.23},
    "SXPUSDT": {"qnt": 153.00, "middlePrice": 0.280, "maxHistoric": 5.79, "investValue": 42.84},
    "FLOWUSDT": {"qnt": 137.44, "middlePrice": 0.518, "maxHistoric": 42.4, "investValue": 71.19},
    "ATOMUSDT": {"qnt": 4.22, "middlePrice": 4.787, "maxHistoric": 44.45, "investValue": 20.20},
    "CRVUSDT": {"qnt": 330.00, "middlePrice": 0.272, "maxHistoric": 15.37, "investValue": 89.80},
    "RVNUSDT": {"qnt": 2002.25, "middlePrice": 0.01720, "maxHistoric": 0.29, "investValue": 34.44},
    "LINKUSDT": {"qnt": 2.19, "middlePrice": 11.680, "maxHistoric": 52.7, "investValue": 25.58},
    "OPUSDT": {"qnt": 13.76, "middlePrice": 1.453, "maxHistoric": 4.84, "investValue": 20.00},
    "SNXUSDT": {"qnt": 14.58, "middlePrice": 1.400, "maxHistoric": 28.53, "investValue": 20.41},
    "POLUSDT": {"qnt": 287.16, "middlePrice": 0.350, "maxHistoric": 1.29, "investValue": 100.51},
    "GMXUSDT": {"qnt": 4.19, "middlePrice": 24.64, "maxHistoric": 91.07, "investValue": 103.24},
    "1MBABYDOGEUSDT": {"qnt": 22008.36, "middlePrice": 0.0000000023, "maxHistoric": 0.0000000063, "investValue": 50.62},
    "BNBUSDT": {"qnt": 0.0067, "middlePrice": 620.00, "maxHistoric": 720, "investValue": 4.19},
    "ASTRUSDT": {"qnt": 1925.69, "middlePrice": 0.065, "maxHistoric": 0.42, "investValue": 126.05},
    "FETUSDT": {"qnt": 23.51, "middlePrice": 1.56, "maxHistoric": 3.45, "investValue": 36.61},
    "FDUSDUSDT": {"qnt": 1003.658, "middlePrice": 1.00, "maxHistoric": 1, "investValue": 1003.658},
    "USDCUSDT": {"qnt": 0.00, "middlePrice": 0.000, "maxHistoric": 1, "investValue": 0.00},
    "TRXUSDT": {"qnt": 23.66, "middlePrice": 0.060, "maxHistoric": 0.23, "investValue": 1.42},
    "THEUSDT": {"qnt": 31.70, "middlePrice": 1.798, "maxHistoric": 4.03, "investValue": 57.00},
    "SOLUSDT": {"qnt": 0.02355, "middlePrice": 223.779, "maxHistoric": 263.21, "investValue": 5.27},
    "CAKEUSDT": {"qnt": 36.88, "middlePrice": 2.03, "maxHistoric": 43.96, "investValue": 74.86},
    "PENDLEUSDT": {"qnt": 27.78, "middlePrice": 3.42, "maxHistoric": 7.50, "investValue": 95.00},
    "PHAUSDT": {"qnt": 549, "middlePrice": 0.091, "maxHistoric": 1.39, "investValue": 50.00},
    "SUSDT": {"qnt": 812.68, "middlePrice": 0.3072, "maxHistoric": 1.03, "investValue": 249.99},    
}

walletCoingeko = {
    "everdome": {"qnt": 193818.00, "middlePrice": 0.00026, "maxHistoric": 0.094, "investValue": 50.00},
    "metahero": {"qnt": 24319.50, "middlePrice": 0.0020, "maxHistoric": 0.25, "investValue": 48.54},
    "bloktopia": {"qnt": 53113.29, "middlePrice": 0.00094, "maxHistoric": 0.13, "investValue": 50.00},
    "aerodrome-finance": {"qnt": 175.95, "middlePrice": 0.68, "maxHistoric": 2.31, "investValue": 119.17},
    "ai-agent-layer": {"qnt": 3036.18, "middlePrice": 0.022, "maxHistoric": 0.14, "investValue": 66.79},
    "nosana": {"qnt": 12.57, "middlePrice": 4.013, "maxHistoric": 7.83, "investValue": 50.44},
    "zircuit": {"qnt": 526.94, "middlePrice": 0.067, "maxHistoric": 0.097, "investValue": 35.49},
    "lto-network": {"qnt": 274.00, "middlePrice": 0.186, "maxHistoric": 0.90, "investValue": 50.93},    
}

class Cryptocurrency:
    def __init__(self, symbol, qnt, middlePrice, maxHistoric, investValue):
        self.symbol = symbol
        self.qnt = qnt
        self.middlePrice = middlePrice
        self.maxHistoric = maxHistoric
        self.investValue = investValue
        self.currentPrice = 0
        self.currentValue = 0
        self.lucro = 0
        self.percentual = 0
        
                  
    def calculate_values(self):
        if self.symbol == 'FDUSD':
            self.symbol = 'USDT'
            self.currentValue = self.investValue
            self.lucro = 0.0
            self.percentual = 0.0
        else:
            self.currentValue = round(self.currentPrice * self.qnt, 2)
            self.lucro = round((self.currentValue - self.investValue), 2 )
            self.percentual = round((((self.currentPrice - self.middlePrice) / self.middlePrice) * 100), 2) if self.middlePrice > 0 else 0
            
        if self.symbol == "1MBABYDOGE":
            self.symbol = "BABYDOGE"
            self.qnt *= 1000000.00
            self.currentPrice /= 1000000.00
            self.lucro = (self.currentPrice * self.qnt) - self.investValue
            self.percentual = ((self.currentPrice - self.middlePrice) / self.middlePrice) * 100 if self.middlePrice > 0 else 0
            self.currentPrice = Decimal(str(self.currentPrice)).normalize()
            self.middlePrice = Decimal(str(self.middlePrice)).normalize()
            self.maxHistoric = Decimal(str(self.maxHistoric)).normalize()
            self.currentPrice = format(self.currentPrice, '.12f')
            self.middlePrice = format(self.middlePrice, '.10f')
            self.maxHistoric = format(self.maxHistoric, '.10f')
            
    def fetch_price_binance(self):
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={self.symbol}"
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            data = response.json()
            self.symbol = data.get("symbol", "N/A").replace("USDT", "")
            self.currentPrice = float(data.get("price", "N/A"))
            self.calculate_values()
            
            
    def fetch_price_coingeko(self):
        url = f"https://api.coingecko.com/api/v3/coins/{self.symbol}"
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            data = response.json()
            self.symbol = data.get("symbol", {}).upper()
            self.currentPrice = float(data.get("market_data", {}).get("current_price", {}).get("usd", "N/A"))
            self.calculate_values()
            time.sleep(15) # Atraso de 15 segundos para respeitar o limite da API coingeko
                
class CryptoPortfolio:
    def __init__(self):
        
        self.cryptocurrencies = []
        self.resultado_total_lucro = 0
        self.resultado_ganho = 0
        self.resultado_perda = 0
        self.valor_total_investido = 0
        self.valor_total_atual = 0

    def add_cryptocurrency(self, crypto):
        self.cryptocurrencies.append(crypto)
    
    def calculate_totals(self, api):
        for crypto in self.cryptocurrencies:
            
            if api == 'binance':
                crypto.fetch_price_binance()
            else:
                crypto.fetch_price_coingeko()
                
            self.resultado_total_lucro += crypto.lucro
            self.valor_total_investido += crypto.investValue
            self.valor_total_atual += crypto.currentValue
            if crypto.lucro >= 0:
                self.resultado_ganho += crypto.lucro
            else:
                self.resultado_perda += crypto.lucro
    
    def get_results(self, portifolio=None):
        if portifolio is None:
             return {
                "valor_total_investido": round(self.valor_total_investido, 2),
                "valor_total_atual": round(self.valor_total_atual, 2),
                "resultado_ganho": round(self.resultado_ganho, 2),
                "resultado_perda": round(self.resultado_perda, 2),
                "resultado_total_lucro": round(self.resultado_total_lucro, 2),
            }
        else:
            resultado_ganho_perc = round(((self.resultado_ganho + portifolio["resultado_ganho"]) / (self.valor_total_investido + portifolio["valor_total_investido"])) * 100, 2) if (self.valor_total_investido + portifolio["valor_total_investido"]) > 0 else 0
            resultado_perda_perc = round(((self.resultado_perda + portifolio["resultado_perda"] ) / (self.valor_total_investido + portifolio["valor_total_investido"])) * 100, 2) if (self.valor_total_investido + portifolio["valor_total_investido"]) > 0 else 0
            resultado_total_perc = round(((self.resultado_total_lucro + portifolio["resultado_total_lucro"])  / (self.valor_total_investido + portifolio["valor_total_investido"])) * 100, 2) if (self.valor_total_investido + portifolio["valor_total_investido"]) > 0 else 0
            
            return [{
                "valor_total_investido": round((self.valor_total_investido + portifolio["valor_total_investido"]), 2),
                "valor_total_atual": round((self.valor_total_atual + portifolio["valor_total_atual"]), 2),
                "resultado_ganho": round((self.resultado_ganho + portifolio["resultado_ganho"]), 2),
                "resultado_perda": round((self.resultado_perda + portifolio["resultado_perda"]), 2),
                "resultado_ganho_perc": resultado_ganho_perc,
                "resultado_perda_perc": resultado_perda_perc,
                "resultado_total_lucro": round((self.resultado_total_lucro + portifolio["resultado_total_lucro"]), 2),
                "resultado_total_perc": resultado_total_perc
            }]
           
            
    