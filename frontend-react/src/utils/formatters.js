/**
 * Formata um valor numérico de acordo com a moeda especificada.
 *
 * @function formatQuantity
 * @param {string} moeda - A moeda utilizada para determinar o formato (ex: "BNB" ou outras).
 * @param {(number|string)} value - O valor numérico a ser formatado.
 * @returns {string} O valor formatado, sem o símbolo "R$". Caso a moeda seja "BNB", utiliza três casas decimais; 
 * para outras moedas, utiliza duas casas decimais.
 */

/**
 * Formata um valor numérico para exibição com símbolo "$ " substituindo "R$".
 *
 * @function formatCurrency
 * @param {string} moeda - A moeda utilizada para determinar o formato (ex: "SHIB", "BABYDOGE", "FDUSD", "USDC", "LUNC", "GALA" ou outras).
 * @param {(number|string)} value - O valor numérico a ser formatado.
 * @returns {string} O valor formatado com o símbolo "$ " no início. Para moedas específicas (ex: SHIB, BABYDOGE, FDUSD, USDC, LUNC, GALA),
 * o número pode ter até 10 casas decimais; para as demais moedas, utiliza duas casas decimais.
 */

/**
 * Formata um valor numérico para representação de lucro, utilizando o símbolo "$ " em vez de "R$".
 *
 * @function formatCurrencyLucro
 * @param {string} moeda - A moeda utilizada para determinar o formato (ex: "FDUSD" ou outras).
 * @param {(number|string)} value - O valor numérico a ser formatado.
 * @returns {string} O valor formatado com o símbolo "$ " no início. Para "FDUSD", utiliza três casas decimais;
 * para as demais, utiliza duas casas decimais.
 */

/**
 * Formata um valor numérico adicionando o símbolo de porcentagem.
 *
 * @function formatPercent
 * @param {(number|string)} value - O valor numérico a ser formatado.
 * @returns {string} O valor formatado com duas casas decimais seguido de " %".
 */

 function formatQuantity(moeda, value)
 {
  const num = Number(value);

  if ( moeda === "BNB" ) {
    return num.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', minimumFractionDigits: 3, maximumFractionDigits: 3 }).replace("R$", "");
  }
  else {
    return num.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', minimumFractionDigits: 2, maximumFractionDigits: 2 }).replace("R$", "");
  }
}

function formatCurrency(moeda, value) {
  const num = Number(value);

  if (
    moeda === "SHIB" ||
    moeda === "BABYDOGE" ||
    moeda === "FDUSD" ||
    moeda === "USDC" ||
    moeda === "LUNC" ||
    moeda === "GALA"
  ) {
    return num.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', minimumFractionDigits: 2, maximumFractionDigits: 10 }).replace("R$", "$ ");
  }
  else {
    return num.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', minimumFractionDigits: 2, maximumFractionDigits: 2 }).replace("R$", "$ ");
  }
}

function formatCurrencyLucro(moeda, value) {
  const num = Number(value);
  if (moeda === "FDUSD") {
    return num.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', minimumFractionDigits: 3, maximumFractionDigits: 3 }).replace("R$", "$ ");
  }
  else{
    return num.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', minimumFractionDigits: 2, maximumFractionDigits: 2 }).replace("R$", "$ ");
  }
}

function formatPercent(value) {
  return Number(value).toFixed(2) + " %";
}

export {
  formatQuantity,
  formatCurrency,
  formatCurrencyLucro,
  formatPercent
};

