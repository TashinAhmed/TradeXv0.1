// alert('gridbot');

const url = "wss://stream.data.alpaca.markets/v1beta1/crypto";
const socket = new WebSocket(url);
// console.log(socket);



// https://alpaca.markets/docs/api-references/market-data-api/crypto-pricing-data/realtime/
const API_KEY = 'PKNZQPISLAB5T6AOZAGT';
const SECRET_KEY = 'NZJB3jG3SrOqf0NLJ1mdkK40SQsiLCZqqUnidC38';
const auth = {"action": "auth", "key": API_KEY, "secret": SECRET_KEY};
const subscribe = {"action":"subscribe", "trades":["ETHUSD"], "quotes":["ETHUSD"], "bars":["ETHUSD"]}

const quotesElement = document.getElementById('quotes');
const tradesElement = document.getElementById('trades');

let currentBar = {};
let trades = [];

// live emulation template starts here
// https://jsfiddle.net/TradingView/yozeu6k1/
var chart = LightweightCharts.createChart(document.getElementById('chart'), {
	width: 700,
    height: 600,
    layout: {
        backgroundColor: '#000000',
        textColor: '#ffffff',
    },
    grid: {
        vertLines: {
            color: '#404040',
        },
        horzLines: {
            color: '#404040',
        },
    },
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
    priceScale: {
        borderColor: '#cccccc',
    },
    timeScale: {
        borderColor: '#cccccc',
        timeVisible: true,
    },
});

var candleSeries = chart.addCandlestickSeries();
// query params - https://alpaca.markets/docs/api-references/market-data-api/crypto-pricing-data/historical/
var start = new Date(Date.now() - (7200*1000)).toISOString(); // last 2 hrs plus JS receives in mill sec so 7200*1000.
console.log(start);
var bars_url = 'https://data.alpaca.markets/v1beta1/crypto/ETHUSD/bars?exchanges=CBSE&timeframe=1Min&start=' + start;
fetch(bars_url,{
    headers:{
        'APCA-API-KEY-ID': API_KEY,
        'APCA-API-SECRET-KEY': SECRET_KEY
    }
}).then((r) => r.json())
    .then((response) => {
        console.log(response);
        const data = response.bars.map(bar =>(
            {
                open: bar.o,
                high: bar.h,
                low: bar.l,
                close: bar.c,
                time: Date.parse(bar.t) / 1000
            }
        ));
        currentBar = data[data.length-1];
        console.log(data);
        candleSeries.setData(data);
    })


// live emulation template ends here.

socket.onmessage = function(event) {
    // console.log(event);
    // console.log(event.data);

    const data = JSON.parse(event.data);
    const message = data[0]['msg'];
    // console.log(data);

    if(message == 'connected'){
        console.log('do authentication');
        socket.send(JSON.stringify(auth));
    }

    if(message == 'authenticated'){
        // they may send multiple data from different brokers (FTXE, CBSE, ERSX) at the same time so we need to loop through them
        socket.send(JSON.stringify(subscribe)); 
    }

    // loop to handle multiple data appeared at the same time.
    for(var key in data){
        // different type of data can come in including trades and quotes -> T = t,q
        // console.log(data[key]);
        const type = data[key].T;

        if(type == 'q'){
            // console.log('got a quote');
            // console.log(data[key]);

            const quoteElement = document.createElement('div');
            
            quoteElement.className = 'quote';
            quoteElement.innerHTML = `<b>${data[key].t}</b> ${data[key].bp} ${data[key].ap}`;
            quotesElement.appendChild(quoteElement);
            
            // only to show latest 10 real time data inside the panel.
            var elements = document.getElementsByClassName('quote');
            if(elements.length > 10){
                quotesElement.removeChild(elements[0]);
            }

        }
        if(type == 't'){
            // console.log('got a trade');
            // console.log(data[key]);

            const tradeElement = document.createElement('div');
            
            tradeElement.className = 'trade';
            tradeElement.innerHTML = `<b>${data[key].t}</b> ${data[key].p} ${data[key].s}`;
            tradesElement.appendChild(tradeElement);
            
            // only to show latest 10 real time data inside the panel.
            var elements = document.getElementsByClassName('trade');
            if(elements.length > 10){
                tradesElement.removeChild(elements[0]);
            }

            // for continuous chart update in 60 seconds starts here.
            trades.push(data[key].p);
            // console.log(trades);
            var open = trades[0];
            var high = Math.max(...trades);
            var low = Math.min(...trades);
            var close = trades[trades.length-1];

            console.log(open, high, low, close);
            candleSeries.update({
                time: currentBar.time + 60,
                open: open,
                high: high,
                low: low,
                close: close
            })
        }
        if(type == 'b' && data[key].x=='CBSE'){
            console.log('got a new bar');
            console.log(data[key]);

            var bar = data[key];
            var timestamp = new Date(bar.t).getTime() / 1000;
            currentBar = {
                time: timestamp,
                open: bar.o,
                high: bar.h,
                low: bar.l,
                close: bar.c
            }
            candleSeries.update(currentBar);

            trades = [];
        }
    }
}
