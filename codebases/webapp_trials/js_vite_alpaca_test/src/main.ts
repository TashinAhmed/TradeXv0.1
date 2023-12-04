import "./style.css";

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
const API_KEY = "PKMFQVNJ8ZA8IH4HQQCD";
const SECRET_KEY = "de4oHxaE4dkbP52P3KevVwURszusWJxjMrbe4zsU";
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


// const conditionalOrder = (init_balance: any, curr_balance: any, disc_rate: any, init_close: any, buy_unit: any, buy_flag_balance: any, close_aftersold: any, init_flag: any, trades: any) => {
  
//   console.log("I curr_balance: " + curr_balance);
//   console.log("I disc_rate: " + disc_rate);
//   console.log("I init_close " + init_close);
//   console.log("I buy_unit " + buy_unit);
//   console.log("I buy_flag_balance " + buy_flag_balance);
//   console.log("I close_aftersold " + close_aftersold);
//   console.log("I init_flag " + init_flag);
//   console.log("I trades " + trades);


//   if(init_flag == false && curr_balance > trades[trades.length - 1] && trades[trades.length - 1] < init_close - disc_rate){
//     // BUY order placed; update ticker
//     createOrder("ETHUSD", 1, "buy", "market", "gtc");
//     curr_balance = curr_balance - trades[trades.length - 1];
//     buy_flag_balance = trades[trades.length - 1];
//     buy_unit = buy_unit + 1;
//     init_flag = true;
//     console.log("C1 BUY BUY BUY");
//     console.log("C1 buy unit: " + buy_unit);
//     console.log("C1 init flag: " + init_flag);
//     console.log("C1 curr_balance" + curr_balance);
//     console.log("C1 buy_flag_balance" + buy_flag_balance);
//   }
  
//   if(init_flag == true && curr_balance > trades[trades.length - 1] && trades[trades.length - 1] < close_aftersold - disc_rate){
//     // BUY order placed; update ticker
//     createOrder("ETHUSD", 1, "buy", "market", "gtc");
//     curr_balance = curr_balance - trades[trades.length - 1];
//     buy_flag_balance = trades[trades.length - 1];
//     buy_unit = buy_unit + 1;
//     console.log("C2 BUY BUY BUY");
//     console.log("C2 buy unit: " + buy_unit);
//     console.log("C2 init flag: " + init_flag);
//     console.log("C2 curr_balance" + curr_balance);
//     console.log("C2 buy_flag_balance" + buy_flag_balance);
    
//   }
  
//   if(trades[trades.length - 1] > buy_flag_balance + disc_rate && buy_unit > 0){
//     // SELL order placed; update ticker 
//     createOrder("ETHUSD", buy_unit, "sell", "market", "gtc");

//     curr_balance = curr_balance + trades[trades.length - 1];
//     buy_unit = 0;
//     close_aftersold = trades[trades.length - 1];

//     console.log("SELL SELL SELL");
//     console.log("S buy unit: " + buy_unit);
//     console.log("S curr_balance" + curr_balance);
//     console.log("S close_aftersold" + close_aftersold);
//   }
// }

const conditionalOrder = async (init_close2: any, trades: any) => {
  if (init_close2 > trades){
    let time = await createOrder("ETHUSD", 1, "buy", "market", "gtc");
    addMarker(time.toString(), trades, "buy");
    console.log(`time for buy ${time}`);
  }
  else{
      let time = await createOrder("ETHUSD", 1, "sell", "market", "gtc");
      addMarker(time.toString(), trades, "sell");
      console.log(`time for sell ${time}`);
  }
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


socket.onmessage = function (event) {
  // console.log(event);
  // console.log(event.data);

  const data = JSON.parse(event.data);
  const message = data[0]["msg"];
  // console.log(data);

  let init_balance = 100000000;
  let curr_balance = init_balance;
  let disc_rate = 1;
  let init_close = trades[trades.length - 1];
  let buy_unit = 0;
  let buy_flag_balance = 0;
  let close_aftersold = 0;
  let init_flag = false;

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
      //   console.log("conditionalOrder calling....");
      //   conditionalOrder(init_balance, curr_balance, disc_rate, init_close, buy_unit, buy_flag_balance, close_aftersold, init_flag, trades);
      // }, 5000);
    }
    if (type == "b" && data[key].x == "CBSE") {
      console.log("got a new bar");
      console.log(data[key]);
      // conditionalOrder(init_balance, curr_balance, disc_rate, init_close, buy_unit, buy_flag_balance, close_aftersold, init_flag, trades);
      conditionalOrder(1079, trades[trades.length - 1]);
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
  const color = variant == "buy" ? "#e91e63" : "#fff";
  const text = `${variant == "buy" ? "Buy" : "Sell"} @ ${price}`;
  markers.push({ time: time, position: variant === "buy" ? "aboveBar" : "belowBar", color, shape: "arrowDown", text });
  candleSeries.setMarkers([...markers]);
};

