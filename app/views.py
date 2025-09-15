import requests
import time
from decimal import Decimal

walletBinance = {
    "LINKUSDT": {"qnt": 39.56, "middlePrice": 25.27, "maxHistoric": 50.00, "investValue": 999.00},
    "POLUSDT": {"qnt": 3483.88, "middlePrice": 0.286, "maxHistoric": 2.5, "investValue": 999.00},
    "ASTRUSDT": {"qnt": 800.69, "middlePrice": 0.065, "maxHistoric": 0.42, "investValue": 52.04},
    "SOLUSDT": {"qnt": 0.02355, "middlePrice": 223.779, "maxHistoric": 263.21, "investValue": 5.27},
    "PENDLEUSDT": {"qnt": 106.43, "middlePrice": 5.21, "maxHistoric": 7.50, "investValue": 554.50},
    "SUIUSDT": {"qnt": 261.57, "middlePrice": 3.81, "maxHistoric": 10.00, "investValue": 996.58},
    "AAVEUSDT": {"qnt": 3.12, "middlePrice": 320.19, "maxHistoric": 600.00, "investValue": 999.00},
    "WLDUSDT": {"qnt": 609.74, "middlePrice": 1.64, "maxHistoric": 11.00, "investValue": 999.00},
    "ONDOUSDT": {"qnt": 849.95, "middlePrice": 1.1, "maxHistoric": 5.07, "investValue": 934.94},
    "ENAUSDT": {"qnt": 1302.81, "middlePrice": 0.76, "maxHistoric": 5.07, "investValue": 997.30},    
}

walletCoingeko = {
    "nosana": {"qnt": 12.57, "middlePrice": 4.013, "maxHistoric": 7.83, "investValue": 50.44},
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
            #time.sleep(15) # Atraso de 15 segundos para respeitar o limite da API coingeko
                
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
           
            
    