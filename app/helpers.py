from .views import Cryptocurrency, CryptoPortfolio

def create_portfolio(wallet, api, portifolioCoingeko=None):
    portifolio = CryptoPortfolio()
    
    for symbol, data in wallet.items():
        crypto = Cryptocurrency(
            symbol=symbol,
            qnt=data["qnt"],
            middlePrice=data["middlePrice"],
            maxHistoric=data["maxHistoric"],
            investValue=data["investValue"]
        )
        portifolio.add_cryptocurrency(crypto)
  
    portifolio.calculate_totals(api)
    
    crypto_data = sorted([{
        "name": crypto.symbol,
        "currentPrice": crypto.currentPrice,
        "qnt": crypto.qnt,
        "middlePrice": crypto.middlePrice,
        "maxHistoric": crypto.maxHistoric,
        "investValue": crypto.investValue,
        "currentValue": crypto.currentValue,
        "lucro": crypto.lucro,
        "percentual": crypto.percentual
    } for crypto in portifolio.cryptocurrencies], key=lambda x: float(x["percentual"]), reverse=True)
    
    if portifolioCoingeko is None:
        resultado_total = portifolio.get_results()
    else:
        resultado_total = portifolio.get_results(portifolioCoingeko)
    
    return crypto_data, resultado_total
