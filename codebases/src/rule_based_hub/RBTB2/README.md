# STATEMENTS

## order of solution: 1A - 1B - 3 - 2A - 2B

### 1A
intersection calculation; No threshold; Trigger in binary value when intersection happen.
- EMA 20 intersection EMA 100
- EMA 100 intersection EMA 200
- EMA 20 intersection EMA 200


### 1B
intersection calculation; No threshold; Trigger in binary value when intersection happen.
- EMA 100 intersection Bollinger Band High
- EMA 100 intersection Bollinger Band Low
- EMA 200 intersection Bollinger Band High
- EMA 200 intersection Bollinger Band Low

1A and 1B trigger conditions(temporary):
- EMA 20 x 100 x 200 (i.e. intersect with each other)
- OR EMA (100 and 200) x (BBH and BBL) 
- OR close value x (100 and 200 and BBH and BBL) 

if above conditions met TRIGGER SET for BUY and SELL


### 2A
calculate how much step will look behind to calculate the trends; currently taking 3 thresholds from users; <br>
if previous EMA values are larger than current one then it will be a down trend. <br>
if previous EMA values are smaller than current one then it will be a up trend. <br>
for down trend SELL and for up trend BUY will be declared if **TRIGGER=1** 

### 2B
real time close value adjacent to EMA values will declare BUY and SELL;
adjacent value will be decided by user input; <br>
if downtrend and close value EMA values lies under the threshold then SELL will be declared as well. <br>
if uptrend and close value EMA values lies under the threshold then BUY will be declared as well.

### 3
Present close price distance with EMA 100, EMA 200, Bollinger Band High and Low. <br>
distance will be measured by user input.
