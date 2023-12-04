import "./style.css";

// import moment from "moment";

import {
  createChart,
  CrosshairMode,
  SeriesMarker,
  Time,
} from "lightweight-charts";

import {createOrders, createOrder, getAccount} from "./trade";
// createOrders();
getAccount();

// alert('gridbot');

const url = "wss://stream.data.alpaca.markets/v1beta1/crypto";
const socket = new WebSocket(url);

// console.log(socket);

// https://alpaca.markets/docs/api-references/market-data-api/crypto-pricing-data/realtime/
const API_KEY = "PK0QVYEBFKW5LR396EHU";
const SECRET_KEY = "5D8ewbpdV9A8QUIm3qjN5zckwdoiYPbr20m2Pdv0";
const auth = { action: "auth", key: API_KEY, secret: SECRET_KEY };

const subscribe = {
  action: "subscribe",
  trades: ["ETHUSD"],
  quotes: ["ETHUSD"],
  bars: ["ETHUSD"],
};

const quotesElement = document.getElementById("quotes");
const tradesElement = document.getElementById("trades");

let currentBar = {};
// @ts-ignore
let trades: any = [];

// live emulation template starts here
// https://jsfiddle.net/TradingView/yozeu6k1/
var chart = createChart(document.getElementById("chart")!, {
  width: 700,
  height: 600,
  layout: {
    backgroundColor: "#000000",
    textColor: "#ffffff",
  },
  grid: {
    vertLines: {
      color: "#404040",
    },
    horzLines: {
      color: "#404040",
    },
  },
  crosshair: {
    mode: CrosshairMode.Normal,
  },
  // priceScale: {
  //   borderColor: "#cccccc",
  // },
  timeScale: {
    borderColor: "#cccccc",
    timeVisible: true,
  },
});

const conditionalOrder = async (init_balance: any, curr_balance: any, disc_rate: any, init_close: any, buy_unit: any, buy_flag_balance: any, close_aftersold: any, init_flag: any, trades: any) => {
  if(init_flag == false && curr_balance > trades[trades.length - 1] && trades[trades.length - 1] < init_close - disc_rate){
    // BUY order placed; update ticker
    curr_balance = curr_balance - trades[trades.length - 1];
    buy_flag_balance = trades[trades.length - 1];
    buy_unit = buy_unit + 1;
    init_flag = true;
    console.log("BUY from logic 1");
    let res1 = await createOrder("ETHUSD", 1, "buy", "market", "gtc");
    addMarker(res1.toString(), curr_balance, "buy");
    console.log(`This is result from logic 1 ${res1}`);
  }
  
  if(init_flag == true && curr_balance > trades[trades.length - 1] && trades[trades.length - 1] < close_aftersold - disc_rate){
    // BUY order placed; update ticker
    curr_balance = curr_balance - trades[trades.length - 1];
    buy_flag_balance = trades[trades.length - 1];
    buy_unit = buy_unit + 1;
    console.log("BUY from logic 2");
    let res2 = await createOrder("ETHUSD", 1, "buy", "market", "gtc");
    addMarker(res2.toString(), curr_balance, "buy");
    console.log(`This is result from logic 1 ${res2}`);
  }
  
  if(trades[trades.length - 1] > buy_flag_balance + disc_rate && buy_unit > 0){
    // SELL order placed; update ticker 
    let res3 = await createOrder("ETHUSD", buy_unit, "sell", "market", "gtc");
    addMarker(res3.toString(), curr_balance, "sell");
    console.log(`This is result from logic 1 ${res3}`);

    curr_balance = curr_balance + trades[trades.length - 1];
    buy_unit = 0;
    close_aftersold = trades[trades.length - 1];
    console.log("SELL from logic 3");
  }

  // console.log(`init_balance: ${init_balance}, curr_balance: ${curr_balance}, disc_rate: ${disc_rate}, init_close: ${init_close}, buy_unit: ${buy_unit}, buy_flag_balance: ${buy_flag_balance}, close_aftersold: ${close_aftersold}, init_flag: ${init_flag}, trades: ${trades}`)
}

var candleSeries = chart.addCandlestickSeries();
// query params - https://alpaca.markets/docs/api-references/market-data-api/crypto-pricing-data/historical/
var start = new Date(Date.now() - 3600 * 2 * 1000).toISOString();
console.log(start);
var bars_url =
  "https://data.alpaca.markets/v1beta1/crypto/ETHUSD/bars?exchanges=CBSE&timeframe=1Min&start=" +
  start;
fetch(bars_url, {
  headers: {
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY,
  },
})
  .then((r) => r.json())
  .then((response) => {
    console.log("bar data");
    console.log(response);
    const data = response.bars.map((bar: any) => ({
      open: bar.o,
      high: bar.h,
      low: bar.l,
      close: bar.c,
      time: Date.parse(bar.t) / 1000,
    }));
    currentBar = data[data.length - 1];
    console.log(data);
    candleSeries.setData(data);
  });

// live emulation template ends here.

// let i = 0;

socket.onerror = function (e) {
  console.error(e);
};

let is_first = true;

let init_balance: any;
let curr_balance: any;
let disc_rate: any;
let init_close: any;
let buy_unit: any;
let buy_flag_balance: any;
let close_aftersold: any;
let init_flag: any;

socket.onmessage = function (event) {
  // console.log(event);
  // console.log(event.data);

  const data = JSON.parse(event.data);
  const message = data[0]["msg"];
  // console.log(data);

  // if (is_first) {
    // init_balance = 100000000;
    // curr_balance = init_balance;
    // disc_rate = 1;
    // init_close = trades[trades.length - 1];
    // buy_unit = 0;
    // buy_flag_balance = 0;
    // close_aftersold = 0;
    // init_flag = false;
    // is_first = false;
  // }
  

  if (message == "connected") {
    console.log("do authentication");
    socket.send(JSON.stringify(auth));
  }

  if (message == "authenticated") {
    // they may send multiple data from different brokers (FTXE, CBSE, ERSX) at the same time so we need to loop through them
    socket.send(JSON.stringify(subscribe));
  }

  // loop to handle multiple data appeared at the same time.
  for (var key in data) {
    // different type of data can come in including trades and quotes -> T = t,q
    // console.log(data[key]);
    const type = data[key].T;

    // i += 1;
    // if (i >= 100) {
    //   console.log("adding marker");
    //   console.log(data[key].t);
    //   const dt = new Date(data[key].t);
    //   console.log(dt);
    //   addMarker(dt.getTime(), 200, Math.round(Math.random()));
    //   i = 0;
    // }

    if (type == "q") {
      // console.log('got a quote');
      // console.log(data[key]);

      const quoteElement = document.createElement("div");

      quoteElement.className = "quote";
      quoteElement.innerHTML = `<b>${data[key].t}</b> ${data[key].bp} ${data[key].ap}`;
      quotesElement?.appendChild(quoteElement);

      // only to show latest 10 real time data inside the panel.
      var elements = document.getElementsByClassName("quote");
      if (elements.length > 10) {
        quotesElement?.removeChild(elements[0]);
      }
    }
    if (type == "t") {
      // console.log('got a trade');
      // console.log(data[key]);

      const tradeElement = document.createElement("div");

      tradeElement.className = "trade";
      tradeElement.innerHTML = `<b>${data[key].t}</b> ${data[key].p} ${data[key].s}`;
      tradesElement?.appendChild(tradeElement);

      // only to show latest 10 real time data inside the panel.
      var elements = document.getElementsByClassName("trade");
      if (elements.length > 10) {
        tradesElement?.removeChild(elements[0]);
      }

      // for continuous chart update in 60 seconds starts here.
      trades.push(data[key].p);
      // console.log(trades[trades.length - 1]);
      var open = trades[0];
      var high = Math.max(...trades);
      var low = Math.min(...trades);
      var close = trades[trades.length - 1];

      //   console.log(open, high, low, close);
      candleSeries.update({
        // @ts-ignore
        time: currentBar.time + 60,
        open: open,
        high: high,
        low: low,
        close: close,
      });
      // setTimeout(() => {
      //   conditionalOrder(init_balance, curr_balance, disc_rate, init_close, buy_unit, buy_flag_balance, close_aftersold, init_flag, trades);
      // }, 5000);
    }
    if (type == "b" && data[key].x == "CBSE") {

      if (is_first) {
        init_balance = 100000000;
        curr_balance = init_balance;
        disc_rate = 1;
        init_close = trades[trades.length - 1];
        buy_unit = 0;
        buy_flag_balance = 0;
        close_aftersold = 0;
        init_flag = false;
        is_first = false;
      }

      console.log("got a new bar");
      console.log(data[key]);
      conditionalOrder(init_balance, curr_balance, disc_rate, init_close, buy_unit, buy_flag_balance, close_aftersold, init_flag, trades);
      var bar = data[key];
      var timestamp = new Date(bar.t).getTime() / 1000;
      currentBar = {
        time: timestamp,
        open: bar.o,
        high: bar.h,
        low: bar.l,
        close: bar.c,
      };
      // @ts-ignore
      candleSeries.update(currentBar);
      trades = [];
    }
  }
};

// Closure
const time = new Date(Date.UTC(0, 0, 0, 0, 0, 0));
const markers: SeriesMarker<Time>[] = [];

const addMarker = (
  time: Time,
  price: number,
  variant: "buy" | "sell" = "buy"
) => {
  // const time_object = moment(time)
  // const time_object2 = time_object.utc().format('YYYY-MM-DD');
  console.log("marker 1")
  const color = variant === "buy" ? "#e91e63" : "#fff";
  const text = `${variant === "buy" ? "Buy" : "Sell"} @ ${price}`;
  markers.push({ time: time, position: variant === "buy" ? "aboveBar" : "belowBar", color, shape: variant === "buy" ? "arrowDown" : "arrowUp", text });
  console.log("marker 2");
  candleSeries.setMarkers([...markers]);
};

