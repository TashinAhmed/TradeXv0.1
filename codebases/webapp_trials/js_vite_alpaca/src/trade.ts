import axios from "axios";

delete axios.defaults.headers.common["content-type"];

const config = {
  API_KEY: "PK0QVYEBFKW5LR396EHU",
  SECRET_KEY: "5D8ewbpdV9A8QUIm3qjN5zckwdoiYPbr20m2Pdv0",
};

const BASE_URL = "https://paper-api.alpaca.markets";
const ACCOUNT_URL = BASE_URL + "/v2/account";
const ORDERS_URL = BASE_URL + "/v2/orders";
const HEADERS = {
  "APCA-API-KEY-ID": config.API_KEY,
  "APCA-API-SECRET-KEY": config.SECRET_KEY,
};

export const getAccount = async () => {
  return axios.get(ACCOUNT_URL, {
    headers: HEADERS,
  });
};

export const createOrder = async (symbol: string, qty: number, side: "buy" | "sell", type: string, timeInForce: string
) => {
  const data = {symbol, qty, side, type: type, time_in_force: timeInForce};
  try {
    const res = await fetch(ORDERS_URL, {
      method: "POST",
      body: JSON.stringify(data),
      headers: HEADERS,
      });
      const d = await res.json();
      return d.created_at;
  } 
  catch (err) {
    console.log(err);
  }
  // const res = await fetch(ORDERS_URL, {
  //   method: "POST",
  //   body: JSON.stringify(data),
  //   headers: HEADERS,
  //   });
  //   const data = await res.json();
  //   return data.created_at;
  //   .then(function(response) {
  //   return response.json();
  //   }).then(function(data) {
  //   return data.created_at;
  //   }).catch(function() {
  //   console.log("Booo");
  //   });
  // return axios.post(ORDERS_URL, { data, headers: HEADERS});
};

export const getOrders = () => {
  return axios.get(ORDERS_URL, { headers: HEADERS });
};

export const createOrders = async () => {
  const res = createOrder("ETHUSD", 1, "buy", "market", "gtc")
  // const res = await createOrder("LTCUSD", 1, "sell", "market", "gtc");
  return res;
};
