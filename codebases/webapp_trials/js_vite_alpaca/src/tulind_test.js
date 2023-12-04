const tulind = require('tulind');
const { promisify } = require('util');


const sma_async = promisify(tulind.indicators.sma.indicator);
const ema_async = promisify(tulind.indicators.ema.indicator);
// const rsi_async = promisify(tulind.indicators.rsi.indicator);
// const macd_async = promisify(tulind.indicators.macd.indicator);

const sma_inc = async (data) => {
  const d1 = data.map((d) => d.close);
  const results = await sma_async([d1], [100]);
  const d2 = results[0];
  const diff = data.length - d2.length;
  const emptyArray = [...new Array(diff)].map((d) => '');
  const d3 = [...emptyArray, ...d2];
  data = data.map((d, i) => ({ ...d, sma: d3[i] }));
  return data;
};

const ema_inc = async (data) => {
  const d1 = data.map((d) => d.close);
  const results = await ema_async([d1], [21]);
  const d2 = results[0];
  const diff = data.length - d2.length;
  const emptyArray = [...new Array(diff)].map((d) => '');
  const d3 = [...emptyArray, ...d2];
  data = data.map((d, i) => ({ ...d, ema: d3[i] }));
  return data;
};

// const rsi_inc = async (data) => {
//   const d1 = data.map((d) => d.close);
//   const results = await rsi_async([d1], [21]);
//   const d2 = results[0];
//   const diff = data.length - d2.length;
//   const emptyArray = [...new Array(diff)].map((d) => '');
//   const d3 = [...emptyArray, ...d2];
//   data = data.map((d, i) => ({ ...d, rsi: d3[i] }));
//   return data;
// };

// longer crossed shorter towards up  (long up)- sell
// shorter crossed longer towards up  (short up)- buy

const markers_inc = (data) => {

  data = data.map((d, i, arr) => {
    const SELL =
      arr[i]?.ema > arr[i]?.sma && arr[i - 1]?.ema < arr[i - 1]?.sma
        ? true
        : false;
    const BUY =
      arr[i]?.ema < arr[i]?.sma && arr[i - 1]?.ema > arr[i - 1]?.sma
        ? true
        : false;
    return { ...d, SELL, BUY };
  });
  return data;
};

// const macd_inc = async (data) => {
//   const d1 = data.map((d) => d.close);
//   const results = await macd_async([d1], [12, 26, 9]);
//   const diff = data.length - results[0].length;
//   const emptyArray = [...new Array(diff)].map((d) => '');

//   const macd1 = [...emptyArray, ...results[0]];
//   const macd2 = [...emptyArray, ...results[1]];
//   const macd3 = [...emptyArray, ...results[2]];

//   data = data.map((d, i) => ({
//     ...d,
//     macd_fast: macd1[i],
//     macd_slow: macd2[i],
//     macd_histogram: macd3[i],
//   }));
//   return data;
// };





// one unit buy/sell 

init_balance = 10000000;
curr_balance = init_balance;
disc_rate = 100;
init_close = current.close;
buy_unit = 0;
buy_flag_balance = 0;
close_aftersold = 0;
init_flag = false;

// (LOOP) 
if(init_flag == false && curr_balance > current.close && current.close < init_close - disc_rate){
  // BUY order placed; update ticker
  curr_balance = curr_balance - current.close;
  buy_flag_balance = current.close;
  buy_unit = buy_unit + 1;
  init_flag = true;
}

if(init_flag == true && curr_balance > current.close && current.close < close_aftersold - disc_rate){
  // BUY order placed; update ticker
  curr_balance = curr_balance - current.close;
  buy_flag_balance = current.close;
  buy_unit = buy_unit + 1;
}

if(current.close > buy_flag_balance + disc_rate && buy_unit > 0){
  // SELL order placed; update ticker 
  curr_balance = curr_balance + current.close;
  buy_unit = buy_unit - 1;
  close_aftersold = current.close;
}