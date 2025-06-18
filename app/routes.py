from flask import jsonify
from .helpers import create_portfolio
from flask import Blueprint
from .views import walletBinance, walletCoingeko 

crypto = Blueprint('crypto', __name__)

cryptoDataCoingeko, resultadoTotalCoingeko = create_portfolio(walletCoingeko, 'coingeko')
         
@crypto.route('/cryptos')
def get_crypto_currentPrices():
    
    # Cria o primeiro portfólios  
    cryptoDataBinance, resultado_total = create_portfolio(walletBinance, 'binance', resultadoTotalCoingeko)
    
    # Concatena as listas
    crypto_data = cryptoDataBinance + cryptoDataCoingeko
    
    return jsonify({
        "cryptos": crypto_data,
        "result_total": resultado_total
    })