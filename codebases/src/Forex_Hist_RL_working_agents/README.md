EUR-USD, USD-JPY train and test models with splitted data in `Data` directory. Model checkpoints can be saved and loaded.  
Q Learning based methods have been applied on different datasets. 



## *** STARTER GUIDE***
* /Data - historical data format
* /logs - all the logs previously generated
* /Models - pretrained models that can be used later on for coninuous train-test-val.
* notebooks can be run sequentially without prior setup. It just require ./Data dir in the same source control.
* On the other hand, ```python train.py``` will work on same way as the notebook but with file format structure.  


Run - 

```python train.py [args]```

for training and

```python eval.py [args]``` 

for evaluation.

```
2021-08-09 09:52:32 c01ae99aeb99 root[60] DEBUG switching to TensorFlow for CPU
/usr/local/lib/python3.7/dist-packages/tensorflow/python/keras/optimizer_v2/optimizer_v2.py:375: UserWarning: The `lr` argument is deprecated, use `learning_rate` instead.
  "The `lr` argument is deprecated, use `learning_rate` instead.")
Episode 1/10: 100%|██████████| 2317/2317 [31:39<00:00,  1.22it/s]
2021-08-09 10:24:11 c01ae99aeb99 root[60] DEBUG Buy at: $108.53
2021-08-09 10:24:11 c01ae99aeb99 root[60] DEBUG Sell at: $108.72 | Position: +$0.1900
2021-08-09 10:24:12 c01ae99aeb99 root[60] DEBUG Buy at: $109.39
2021-08-09 10:24:12 c01ae99aeb99 root[60] DEBUG Buy at: $109.03
2021-08-09 10:24:12 c01ae99aeb99 root[60] DEBUG Buy at: $109.50
2021-08-09 10:24:12 c01ae99aeb99 root[60] DEBUG Sell at: $109.89 | Position: +$0.5000
2021-08-09 10:24:12 c01ae99aeb99 root[60] DEBUG Sell at: $109.97 | Position: +$0.9400
2021-08-09 10:24:12 c01ae99aeb99 root[60] DEBUG Sell at: $109.97 | Position: +$0.4700
2021-08-09 10:24:13 c01ae99aeb99 root[60] DEBUG Buy at: $110.50
2021-08-09 10:24:13 c01ae99aeb99 root[60] DEBUG Sell at: $110.62 | Position: +$0.1200
2021-08-09 10:24:13 c01ae99aeb99 root[60] DEBUG Buy at: $110.69
2021-08-09 10:24:13 c01ae99aeb99 root[60] DEBUG Sell at: $111.06 | Position: +$0.3700
2021-08-09 10:24:13 c01ae99aeb99 root[60] DEBUG Buy at: $110.58
2021-08-09 10:24:13 c01ae99aeb99 root[60] DEBUG Buy at: $111.00
2021-08-09 10:24:13 c01ae99aeb99 root[60] DEBUG Sell at: $111.39 | Position: +$0.8100
2021-08-09 10:24:13 c01ae99aeb99 root[60] DEBUG Sell at: $111.92 | Position: +$0.9200
2021-08-09 10:24:13 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 10:24:13 c01ae99aeb99 root[60] DEBUG Sell at: $111.20 | Position: +$0.0300
2021-08-09 10:24:13 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 10:24:13 c01ae99aeb99 root[60] DEBUG Buy at: $110.69
2021-08-09 10:24:13 c01ae99aeb99 root[60] DEBUG Buy at: $110.81
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Buy at: $109.97
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Sell at: $110.64 | Position: -$0.5300
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Buy at: $110.52
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Sell at: $110.86 | Position: +$0.1700
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Sell at: $111.36 | Position: +$0.5500
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Sell at: $111.33 | Position: +$1.3600
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Buy at: $111.67
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Sell at: $111.73 | Position: +$1.2100
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Sell at: $111.14 | Position: -$0.5300
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Buy at: $111.02
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Sell at: $111.67 | Position: +$0.6500
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Buy at: $111.97
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Buy at: $111.92
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Sell at: $111.86 | Position: -$0.1100
2021-08-09 10:24:14 c01ae99aeb99 root[60] DEBUG Sell at: $112.19 | Position: +$0.2700
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Buy at: $111.42
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Buy at: $111.39
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Buy at: $111.52
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Buy at: $111.11
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Buy at: $110.78
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Buy at: $110.25
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Buy at: $110.11
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Buy at: $109.76
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Buy at: $110.50
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Sell at: $110.36 | Position: -$1.0600
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Buy at: $109.52
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Buy at: $109.38
2021-08-09 10:24:15 c01ae99aeb99 root[60] DEBUG Sell at: $109.59 | Position: -$1.8000
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Buy at: $108.14
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.47 | Position: -$3.0500
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.42 | Position: -$2.6900
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.52 | Position: -$2.2600
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Buy at: $108.50
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.39 | Position: -$1.8600
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.56 | Position: -$1.5500
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Buy at: $108.56
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Buy at: $108.11
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Sell at: $107.31 | Position: -$2.4500
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Buy at: $107.19
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Buy at: $107.78
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.44 | Position: -$0.8700
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Buy at: $107.89
2021-08-09 10:24:16 c01ae99aeb99 root[60] DEBUG Buy at: $108.47
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.72 | Position: -$1.7800
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.86 | Position: -$0.4500
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.47 | Position: -$1.0500
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.50 | Position: -$0.8800
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Buy at: $107.91
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Sell at: $107.72 | Position: -$0.4200
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Buy at: $107.88
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.22 | Position: -$0.2800
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.64 | Position: +$0.0800
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: +$0.5600
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.78 | Position: +$1.5900
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Buy at: $108.75
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Buy at: $107.34
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Sell at: $106.59 | Position: -$1.1900
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Buy at: $105.95
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Sell at: $106.48 | Position: -$1.4100
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Buy at: $106.28
2021-08-09 10:24:17 c01ae99aeb99 root[60] DEBUG Buy at: $106.08
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Buy at: $105.31
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Buy at: $106.75
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Buy at: $105.91
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Sell at: $106.38 | Position: -$2.0900
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Sell at: $106.64 | Position: -$1.2700
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Sell at: $106.23 | Position: -$1.6500
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Sell at: $106.62 | Position: -$2.1300
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Sell at: $106.44 | Position: -$0.9000
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Buy at: $106.14
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Buy at: $105.73
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Buy at: $106.12
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Sell at: $106.52 | Position: +$0.5700
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Buy at: $106.31
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Buy at: $106.39
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Sell at: $106.92 | Position: +$0.6400
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Buy at: $107.55
2021-08-09 10:24:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.11 | Position: +$2.0300
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: +$2.8300
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: +$1.3900
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.02 | Position: +$2.1100
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Sell at: $107.56 | Position: +$1.4200
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Buy at: $107.56
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Buy at: $107.06
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Sell at: $107.78 | Position: +$2.0500
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Sell at: $107.94 | Position: +$1.8200
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.08 | Position: +$1.7700
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Buy at: $106.92
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Buy at: $106.94
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Sell at: $107.30 | Position: +$0.9100
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Sell at: $107.97 | Position: +$0.4200
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.42 | Position: +$0.8600
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.39 | Position: +$1.3300
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.86 | Position: +$1.9400
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.77 | Position: +$1.8300
2021-08-09 10:24:19 c01ae99aeb99 root[60] DEBUG Buy at: $108.43
2021-08-09 10:24:20 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$0.1800
2021-08-09 10:24:20 c01ae99aeb99 root[60] DEBUG Buy at: $108.61
2021-08-09 10:24:20 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 10:24:20 c01ae99aeb99 root[60] DEBUG Sell at: $108.58 | Position: -$0.0300
2021-08-09 10:24:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.16 | Position: +$0.9700
2021-08-09 10:24:20 c01ae99aeb99 root[60] DEBUG Buy at: $108.41
2021-08-09 10:24:20 c01ae99aeb99 root[60] DEBUG Buy at: $108.67
2021-08-09 10:24:20 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$0.2000
2021-08-09 10:24:20 c01ae99aeb99 root[60] DEBUG Sell at: $108.66 | Position: -$0.0100
2021-08-09 10:24:21 c01ae99aeb99 root[60] DEBUG Buy at: $109.56
2021-08-09 10:24:21 c01ae99aeb99 root[60] DEBUG Buy at: $109.52
2021-08-09 10:24:21 c01ae99aeb99 root[60] DEBUG Sell at: $109.00 | Position: -$0.5600
2021-08-09 10:24:21 c01ae99aeb99 root[60] DEBUG Sell at: $108.64 | Position: -$0.8800
2021-08-09 10:24:21 c01ae99aeb99 root[60] DEBUG Buy at: $108.86
2021-08-09 10:24:21 c01ae99aeb99 root[60] DEBUG Sell at: $108.56 | Position: -$0.3000
2021-08-09 10:24:21 c01ae99aeb99 root[60] DEBUG Buy at: $108.71
2021-08-09 10:24:21 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 10:24:21 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$0.6700
2021-08-09 10:24:21 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$0.1900
2021-08-09 10:24:21 c01ae99aeb99 root[60] DEBUG Buy at: $109.44
2021-08-09 10:24:21 c01ae99aeb99 root[60] DEBUG Buy at: $109.64
2021-08-09 10:24:21 c01ae99aeb99 root[60] DEBUG Buy at: $109.42
2021-08-09 10:24:21 c01ae99aeb99 root[60] INFO Episode 1/10 - Train Position: +$1327.2200  Val Position: +$0.8800  Train Loss: 0.2262746)
Episode 2/10: 100%|██████████| 2317/2317 [31:29<00:00,  1.23it/s]
2021-08-09 10:55:52 c01ae99aeb99 root[60] DEBUG Buy at: $109.03
2021-08-09 10:55:52 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$0.4700
2021-08-09 10:55:53 c01ae99aeb99 root[60] DEBUG Buy at: $110.50
2021-08-09 10:55:53 c01ae99aeb99 root[60] DEBUG Sell at: $110.62 | Position: +$0.1200
2021-08-09 10:55:53 c01ae99aeb99 root[60] DEBUG Buy at: $110.69
2021-08-09 10:55:53 c01ae99aeb99 root[60] DEBUG Sell at: $111.06 | Position: +$0.3700
2021-08-09 10:55:53 c01ae99aeb99 root[60] DEBUG Buy at: $111.00
2021-08-09 10:55:53 c01ae99aeb99 root[60] DEBUG Sell at: $111.39 | Position: +$0.3900
2021-08-09 10:55:53 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 10:55:53 c01ae99aeb99 root[60] DEBUG Sell at: $111.20 | Position: +$0.0300
2021-08-09 10:55:53 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 10:55:53 c01ae99aeb99 root[60] DEBUG Buy at: $111.72
2021-08-09 10:55:53 c01ae99aeb99 root[60] DEBUG Buy at: $111.42
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Buy at: $110.69
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Buy at: $110.81
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Buy at: $109.97
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Sell at: $110.64 | Position: -$0.5300
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Buy at: $110.52
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Sell at: $110.64 | Position: -$1.0800
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Buy at: $110.86
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.36 | Position: -$0.0600
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.33 | Position: +$0.6400
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Buy at: $111.48
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.67 | Position: +$0.8600
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.73 | Position: +$1.7600
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.48 | Position: +$0.9600
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.14 | Position: +$0.2800
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.67 | Position: +$0.1900
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Buy at: $112.06
2021-08-09 10:55:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.86 | Position: -$0.2000
2021-08-09 10:55:55 c01ae99aeb99 root[60] DEBUG Buy at: $111.52
2021-08-09 10:55:55 c01ae99aeb99 root[60] DEBUG Buy at: $111.11
2021-08-09 10:55:55 c01ae99aeb99 root[60] DEBUG Buy at: $110.25
2021-08-09 10:55:55 c01ae99aeb99 root[60] DEBUG Buy at: $110.11
2021-08-09 10:55:55 c01ae99aeb99 root[60] DEBUG Buy at: $109.76
2021-08-09 10:55:55 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 10:55:55 c01ae99aeb99 root[60] DEBUG Buy at: $109.61
2021-08-09 10:55:55 c01ae99aeb99 root[60] DEBUG Buy at: $109.59
2021-08-09 10:55:55 c01ae99aeb99 root[60] DEBUG Sell at: $110.06 | Position: -$1.4600
2021-08-09 10:55:55 c01ae99aeb99 root[60] DEBUG Sell at: $110.36 | Position: -$0.7500
2021-08-09 10:55:55 c01ae99aeb99 root[60] DEBUG Buy at: $109.61
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.28
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: -$2.1100
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Sell at: $108.42 | Position: -$1.6900
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.52
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Sell at: $108.50 | Position: -$1.2600
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.39
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.56
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.11
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Buy at: $107.31
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Buy at: $107.30
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Buy at: $107.19
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Sell at: $108.44 | Position: -$0.8700
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Buy at: $107.89
2021-08-09 10:55:56 c01ae99aeb99 root[60] DEBUG Sell at: $107.81 | Position: -$1.8000
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Buy at: $108.50
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Sell at: $107.72 | Position: -$1.8700
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Buy at: $107.88
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Buy at: $108.22
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Buy at: $108.64
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: -$0.9400
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Sell at: $108.78 | Position: +$0.5000
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Sell at: $108.75 | Position: +$0.5600
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Buy at: $107.34
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Buy at: $106.59
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Buy at: $105.95
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Buy at: $106.28
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Buy at: $106.08
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Buy at: $105.67
2021-08-09 10:55:57 c01ae99aeb99 root[60] DEBUG Buy at: $105.31
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Buy at: $105.91
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Sell at: $106.12 | Position: -$2.4000
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Buy at: $106.38
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Buy at: $106.62
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Sell at: $106.44 | Position: -$1.9500
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Sell at: $106.14 | Position: -$2.4200
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Buy at: $105.73
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Sell at: $106.52 | Position: -$1.5900
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Buy at: $106.31
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Sell at: $106.22 | Position: -$1.0900
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Buy at: $106.39
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Sell at: $106.92 | Position: -$0.3800
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Sell at: $108.11 | Position: +$0.9200
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Buy at: $108.08
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: +$0.2500
2021-08-09 10:55:58 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: -$0.3600
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Sell at: $108.02 | Position: +$0.1400
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Buy at: $107.56
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Buy at: $107.06
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Sell at: $107.78 | Position: -$0.4400
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Sell at: $107.94 | Position: -$0.7000
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Sell at: $108.08 | Position: +$0.7400
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Sell at: $107.75 | Position: +$1.1600
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Buy at: $106.92
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Buy at: $106.94
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Sell at: $107.30 | Position: +$1.3500
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Buy at: $107.47
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Sell at: $108.42 | Position: +$2.1400
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Sell at: $108.39 | Position: +$2.3100
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Sell at: $108.86 | Position: +$3.1900
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Sell at: $108.77 | Position: +$3.4600
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: +$2.7600
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Buy at: $108.43
2021-08-09 10:55:59 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$2.2300
2021-08-09 10:56:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.69 | Position: +$2.0700
2021-08-09 10:56:00 c01ae99aeb99 root[60] DEBUG Buy at: $108.61
2021-08-09 10:56:00 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 10:56:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.58 | Position: +$2.8500
2021-08-09 10:56:00 c01ae99aeb99 root[60] DEBUG Sell at: $109.16 | Position: +$2.8500
2021-08-09 10:56:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.97 | Position: +$2.5800
2021-08-09 10:56:00 c01ae99aeb99 root[60] DEBUG Buy at: $109.28
2021-08-09 10:56:00 c01ae99aeb99 root[60] DEBUG Sell at: $109.06 | Position: +$0.9800
2021-08-09 10:56:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.83 | Position: +$1.2700
2021-08-09 10:56:00 c01ae99aeb99 root[60] DEBUG Buy at: $108.67
2021-08-09 10:56:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$1.5500
2021-08-09 10:56:00 c01ae99aeb99 root[60] DEBUG Buy at: $108.64
2021-08-09 10:56:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.92 | Position: +$2.0000
2021-08-09 10:56:00 c01ae99aeb99 root[60] DEBUG Sell at: $109.05 | Position: +$2.1100
2021-08-09 10:56:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.52 | Position: +$2.0500
2021-08-09 10:56:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.00 | Position: +$0.5700
2021-08-09 10:56:01 c01ae99aeb99 root[60] DEBUG Buy at: $108.86
2021-08-09 10:56:01 c01ae99aeb99 root[60] DEBUG Sell at: $108.56 | Position: -$0.0500
2021-08-09 10:56:01 c01ae99aeb99 root[60] DEBUG Buy at: $108.71
2021-08-09 10:56:01 c01ae99aeb99 root[60] DEBUG Sell at: $108.56 | Position: +$0.3700
2021-08-09 10:56:01 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 10:56:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$0.1000
2021-08-09 10:56:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$0.8300
2021-08-09 10:56:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.53 | Position: +$0.8900
2021-08-09 10:56:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$0.5200
2021-08-09 10:56:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.39 | Position: +$0.6800
2021-08-09 10:56:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.64 | Position: +$0.3300
2021-08-09 10:56:01 c01ae99aeb99 root[60] INFO Episode 2/10 - Train Position: +$2256.8700  Val Position: +$26.3800  Train Loss: 0.2539677)
Episode 3/10: 100%|██████████| 2317/2317 [31:25<00:00,  1.23it/s]
2021-08-09 11:27:27 c01ae99aeb99 root[60] DEBUG Buy at: $109.60
2021-08-09 11:27:27 c01ae99aeb99 root[60] DEBUG Sell at: $109.55 | Position: -$0.0500
2021-08-09 11:27:28 c01ae99aeb99 root[60] DEBUG Buy at: $109.39
2021-08-09 11:27:28 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$0.1100
2021-08-09 11:27:28 c01ae99aeb99 root[60] DEBUG Buy at: $109.97
2021-08-09 11:27:28 c01ae99aeb99 root[60] DEBUG Sell at: $109.73 | Position: -$0.2400
2021-08-09 11:27:28 c01ae99aeb99 root[60] DEBUG Buy at: $110.50
2021-08-09 11:27:28 c01ae99aeb99 root[60] DEBUG Sell at: $110.62 | Position: +$0.1200
2021-08-09 11:27:28 c01ae99aeb99 root[60] DEBUG Buy at: $110.69
2021-08-09 11:27:28 c01ae99aeb99 root[60] DEBUG Buy at: $111.06
2021-08-09 11:27:28 c01ae99aeb99 root[60] DEBUG Buy at: $110.58
2021-08-09 11:27:28 c01ae99aeb99 root[60] DEBUG Buy at: $111.00
2021-08-09 11:27:28 c01ae99aeb99 root[60] DEBUG Sell at: $111.39 | Position: +$0.7000
2021-08-09 11:27:28 c01ae99aeb99 root[60] DEBUG Sell at: $111.92 | Position: +$0.8600
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Sell at: $111.75 | Position: +$1.1700
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Buy at: $111.89
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Sell at: $111.77 | Position: +$0.7700
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Sell at: $111.59 | Position: -$0.3000
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Sell at: $111.20 | Position: +$0.0300
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Buy at: $110.69
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Buy at: $110.81
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Sell at: $110.64 | Position: -$0.5300
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Buy at: $110.52
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Buy at: $110.86
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Sell at: $111.33 | Position: +$0.6400
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Sell at: $111.67 | Position: +$0.8600
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Sell at: $111.73 | Position: +$1.2100
2021-08-09 11:27:29 c01ae99aeb99 root[60] DEBUG Sell at: $111.48 | Position: +$0.6200
2021-08-09 11:27:30 c01ae99aeb99 root[60] DEBUG Buy at: $111.14
2021-08-09 11:27:30 c01ae99aeb99 root[60] DEBUG Sell at: $111.67 | Position: +$0.5300
2021-08-09 11:27:30 c01ae99aeb99 root[60] DEBUG Buy at: $112.06
2021-08-09 11:27:30 c01ae99aeb99 root[60] DEBUG Sell at: $111.92 | Position: -$0.1400
2021-08-09 11:27:30 c01ae99aeb99 root[60] DEBUG Buy at: $111.42
2021-08-09 11:27:30 c01ae99aeb99 root[60] DEBUG Buy at: $111.39
2021-08-09 11:27:30 c01ae99aeb99 root[60] DEBUG Buy at: $111.52
2021-08-09 11:27:30 c01ae99aeb99 root[60] DEBUG Buy at: $111.11
2021-08-09 11:27:30 c01ae99aeb99 root[60] DEBUG Buy at: $110.11
2021-08-09 11:27:30 c01ae99aeb99 root[60] DEBUG Buy at: $109.76
2021-08-09 11:27:30 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 11:27:31 c01ae99aeb99 root[60] DEBUG Buy at: $109.59
2021-08-09 11:27:31 c01ae99aeb99 root[60] DEBUG Buy at: $110.06
2021-08-09 11:27:31 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 11:27:31 c01ae99aeb99 root[60] DEBUG Buy at: $108.28
2021-08-09 11:27:31 c01ae99aeb99 root[60] DEBUG Buy at: $108.14
2021-08-09 11:27:31 c01ae99aeb99 root[60] DEBUG Sell at: $108.47 | Position: -$2.9500
2021-08-09 11:27:31 c01ae99aeb99 root[60] DEBUG Buy at: $108.42
2021-08-09 11:27:31 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 11:27:31 c01ae99aeb99 root[60] DEBUG Sell at: $108.50 | Position: -$2.8900
2021-08-09 11:27:31 c01ae99aeb99 root[60] DEBUG Buy at: $108.39
2021-08-09 11:27:31 c01ae99aeb99 root[60] DEBUG Buy at: $108.56
2021-08-09 11:27:31 c01ae99aeb99 root[60] DEBUG Sell at: $108.56 | Position: -$2.9600
2021-08-09 11:27:31 c01ae99aeb99 root[60] DEBUG Buy at: $108.11
2021-08-09 11:27:32 c01ae99aeb99 root[60] DEBUG Buy at: $107.31
2021-08-09 11:27:32 c01ae99aeb99 root[60] DEBUG Sell at: $107.19 | Position: -$3.9200
2021-08-09 11:27:32 c01ae99aeb99 root[60] DEBUG Buy at: $107.89
2021-08-09 11:27:32 c01ae99aeb99 root[60] DEBUG Sell at: $107.83 | Position: -$2.2800
2021-08-09 11:27:32 c01ae99aeb99 root[60] DEBUG Buy at: $107.81
2021-08-09 11:27:32 c01ae99aeb99 root[60] DEBUG Buy at: $108.86
2021-08-09 11:27:32 c01ae99aeb99 root[60] DEBUG Sell at: $108.24 | Position: -$1.5200
2021-08-09 11:27:32 c01ae99aeb99 root[60] DEBUG Sell at: $107.72 | Position: -$1.5900
2021-08-09 11:27:32 c01ae99aeb99 root[60] DEBUG Buy at: $108.22
2021-08-09 11:27:32 c01ae99aeb99 root[60] DEBUG Sell at: $108.64 | Position: -$0.9500
2021-08-09 11:27:32 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: -$1.3900
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Sell at: $108.78 | Position: -$0.5300
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Sell at: $108.75 | Position: +$0.4700
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Buy at: $107.34
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Buy at: $105.95
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Buy at: $106.28
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Buy at: $106.08
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Buy at: $105.31
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Buy at: $106.12
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Buy at: $106.38
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Buy at: $106.62
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Buy at: $106.44
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Buy at: $105.73
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Buy at: $106.12
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Sell at: $106.52 | Position: -$1.6200
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Buy at: $106.31
2021-08-09 11:27:33 c01ae99aeb99 root[60] DEBUG Sell at: $106.22 | Position: -$2.2000
2021-08-09 11:27:34 c01ae99aeb99 root[60] DEBUG Buy at: $106.39
2021-08-09 11:27:34 c01ae99aeb99 root[60] DEBUG Sell at: $106.92 | Position: -$1.2700
2021-08-09 11:27:34 c01ae99aeb99 root[60] DEBUG Buy at: $107.55
2021-08-09 11:27:34 c01ae99aeb99 root[60] DEBUG Sell at: $108.11 | Position: -$0.2800
2021-08-09 11:27:34 c01ae99aeb99 root[60] DEBUG Buy at: $108.08
2021-08-09 11:27:34 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: -$0.4200
2021-08-09 11:27:34 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: +$0.0300
2021-08-09 11:27:34 c01ae99aeb99 root[60] DEBUG Sell at: $108.45 | Position: +$1.1400
2021-08-09 11:27:34 c01ae99aeb99 root[60] DEBUG Sell at: $108.02 | Position: +$0.1300
2021-08-09 11:27:34 c01ae99aeb99 root[60] DEBUG Sell at: $107.56 | Position: -$0.2500
2021-08-09 11:27:34 c01ae99aeb99 root[60] DEBUG Buy at: $107.06
2021-08-09 11:27:34 c01ae99aeb99 root[60] DEBUG Sell at: $107.78 | Position: -$1.0800
2021-08-09 11:27:34 c01ae99aeb99 root[60] DEBUG Sell at: $107.94 | Position: -$0.2800
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Sell at: $108.08 | Position: +$0.7400
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Sell at: $107.75 | Position: +$1.8000
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Sell at: $107.30 | Position: +$1.0200
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Sell at: $107.97 | Position: +$1.8900
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Sell at: $108.42 | Position: +$3.1100
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Sell at: $108.39 | Position: +$2.2700
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Sell at: $108.86 | Position: +$2.4800
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Sell at: $108.77 | Position: +$2.1500
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: +$2.2300
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Buy at: $108.43
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$2.8800
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Sell at: $108.69 | Position: +$2.5700
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Sell at: $108.58 | Position: +$2.2700
2021-08-09 11:27:35 c01ae99aeb99 root[60] DEBUG Sell at: $109.16 | Position: +$2.7700
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Sell at: $108.97 | Position: +$1.4200
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Buy at: $109.28
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$1.2000
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Sell at: $109.06 | Position: +$2.0000
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Sell at: $108.83 | Position: +$0.4000
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Buy at: $108.67
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$0.4200
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Buy at: $108.64
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Sell at: $108.66 | Position: -$0.6200
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Sell at: $108.92 | Position: +$0.2500
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Sell at: $109.05 | Position: +$0.4100
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Buy at: $109.00
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Buy at: $108.86
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Buy at: $108.61
2021-08-09 11:27:36 c01ae99aeb99 root[60] DEBUG Buy at: $108.71
2021-08-09 11:27:37 c01ae99aeb99 root[60] DEBUG Sell at: $109.31 | Position: +$0.3100
2021-08-09 11:27:37 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$0.5200
2021-08-09 11:27:37 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$0.8900
2021-08-09 11:27:37 c01ae99aeb99 root[60] DEBUG Sell at: $109.48 | Position: +$0.7700
2021-08-09 11:27:37 c01ae99aeb99 root[60] INFO Episode 3/10 - Train Position: +$1897.3700  Val Position: +$15.9000  Train Loss: 0.2288210)
Episode 4/10: 100%|██████████| 2317/2317 [31:41<00:00,  1.22it/s]
2021-08-09 11:59:18 c01ae99aeb99 root[60] DEBUG Buy at: $108.53
2021-08-09 11:59:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.75 | Position: +$0.2200
2021-08-09 11:59:19 c01ae99aeb99 root[60] DEBUG Buy at: $109.60
2021-08-09 11:59:19 c01ae99aeb99 root[60] DEBUG Buy at: $109.64
2021-08-09 11:59:19 c01ae99aeb99 root[60] DEBUG Buy at: $109.39
2021-08-09 11:59:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.03 | Position: -$0.5700
2021-08-09 11:59:19 c01ae99aeb99 root[60] DEBUG Buy at: $109.50
2021-08-09 11:59:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.89 | Position: +$0.2500
2021-08-09 11:59:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.97 | Position: +$0.5800
2021-08-09 11:59:19 c01ae99aeb99 root[60] DEBUG Buy at: $109.97
2021-08-09 11:59:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.81 | Position: +$0.3100
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Sell at: $110.38 | Position: +$0.4100
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Buy at: $111.00
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Sell at: $110.48 | Position: -$0.5200
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Buy at: $110.50
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Sell at: $110.62 | Position: +$0.1200
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Buy at: $110.69
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Buy at: $111.06
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Buy at: $110.58
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Buy at: $111.00
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Sell at: $111.39 | Position: +$0.7000
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Sell at: $111.92 | Position: +$0.8600
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Sell at: $111.89 | Position: +$1.3100
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Sell at: $111.77 | Position: +$0.7700
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 11:59:20 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 11:59:21 c01ae99aeb99 root[60] DEBUG Buy at: $110.69
2021-08-09 11:59:21 c01ae99aeb99 root[60] DEBUG Buy at: $110.81
2021-08-09 11:59:21 c01ae99aeb99 root[60] DEBUG Sell at: $110.64 | Position: -$0.5300
2021-08-09 11:59:21 c01ae99aeb99 root[60] DEBUG Buy at: $110.52
2021-08-09 11:59:21 c01ae99aeb99 root[60] DEBUG Buy at: $110.86
2021-08-09 11:59:21 c01ae99aeb99 root[60] DEBUG Sell at: $111.36 | Position: +$0.1900
2021-08-09 11:59:21 c01ae99aeb99 root[60] DEBUG Sell at: $111.33 | Position: +$0.6400
2021-08-09 11:59:21 c01ae99aeb99 root[60] DEBUG Sell at: $111.67 | Position: +$0.8600
2021-08-09 11:59:21 c01ae99aeb99 root[60] DEBUG Sell at: $111.73 | Position: +$1.2100
2021-08-09 11:59:21 c01ae99aeb99 root[60] DEBUG Sell at: $111.48 | Position: +$0.6200
2021-08-09 11:59:21 c01ae99aeb99 root[60] DEBUG Buy at: $111.14
2021-08-09 11:59:21 c01ae99aeb99 root[60] DEBUG Sell at: $111.67 | Position: +$0.5300
2021-08-09 11:59:21 c01ae99aeb99 root[60] DEBUG Buy at: $112.03
2021-08-09 11:59:21 c01ae99aeb99 root[60] DEBUG Sell at: $112.03 | Position: +$0.0000
2021-08-09 11:59:22 c01ae99aeb99 root[60] DEBUG Buy at: $112.19
2021-08-09 11:59:22 c01ae99aeb99 root[60] DEBUG Buy at: $111.42
2021-08-09 11:59:22 c01ae99aeb99 root[60] DEBUG Buy at: $111.39
2021-08-09 11:59:22 c01ae99aeb99 root[60] DEBUG Buy at: $110.25
2021-08-09 11:59:22 c01ae99aeb99 root[60] DEBUG Buy at: $110.11
2021-08-09 11:59:22 c01ae99aeb99 root[60] DEBUG Buy at: $109.76
2021-08-09 11:59:22 c01ae99aeb99 root[60] DEBUG Buy at: $109.94
2021-08-09 11:59:22 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 11:59:22 c01ae99aeb99 root[60] DEBUG Buy at: $109.59
2021-08-09 11:59:22 c01ae99aeb99 root[60] DEBUG Sell at: $110.06 | Position: -$2.1300
2021-08-09 11:59:22 c01ae99aeb99 root[60] DEBUG Buy at: $109.61
2021-08-09 11:59:22 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 11:59:22 c01ae99aeb99 root[60] DEBUG Buy at: $109.52
2021-08-09 11:59:23 c01ae99aeb99 root[60] DEBUG Sell at: $108.47 | Position: -$2.9500
2021-08-09 11:59:23 c01ae99aeb99 root[60] DEBUG Buy at: $108.42
2021-08-09 11:59:23 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 11:59:23 c01ae99aeb99 root[60] DEBUG Buy at: $108.50
2021-08-09 11:59:23 c01ae99aeb99 root[60] DEBUG Buy at: $108.39
2021-08-09 11:59:23 c01ae99aeb99 root[60] DEBUG Buy at: $108.56
2021-08-09 11:59:23 c01ae99aeb99 root[60] DEBUG Buy at: $108.11
2021-08-09 11:59:23 c01ae99aeb99 root[60] DEBUG Buy at: $107.31
2021-08-09 11:59:23 c01ae99aeb99 root[60] DEBUG Buy at: $107.30
2021-08-09 11:59:23 c01ae99aeb99 root[60] DEBUG Buy at: $107.19
2021-08-09 11:59:23 c01ae99aeb99 root[60] DEBUG Buy at: $107.78
2021-08-09 11:59:23 c01ae99aeb99 root[60] DEBUG Sell at: $107.89 | Position: -$3.5000
2021-08-09 11:59:23 c01ae99aeb99 root[60] DEBUG Buy at: $107.89
2021-08-09 11:59:23 c01ae99aeb99 root[60] DEBUG Buy at: $107.81
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Sell at: $108.47 | Position: -$1.7800
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Buy at: $107.92
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Buy at: $107.72
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Sell at: $107.88 | Position: -$2.2300
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Buy at: $108.22
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Sell at: $108.64 | Position: -$1.1200
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: -$1.2700
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Sell at: $108.78 | Position: -$0.5300
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Buy at: $108.75
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Sell at: $107.34 | Position: -$2.2500
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Buy at: $105.95
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Buy at: $106.48
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Buy at: $106.28
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Buy at: $106.08
2021-08-09 11:59:24 c01ae99aeb99 root[60] DEBUG Buy at: $105.31
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Buy at: $106.75
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Sell at: $106.12 | Position: -$3.4900
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Buy at: $106.38
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Sell at: $106.62 | Position: -$2.6900
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Buy at: $106.44
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Buy at: $106.14
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Sell at: $106.12 | Position: -$3.4000
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Buy at: $106.52
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Buy at: $106.31
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Buy at: $106.39
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Buy at: $107.25
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Sell at: $108.11 | Position: -$0.3100
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Buy at: $108.08
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: -$0.0500
2021-08-09 11:59:25 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: -$0.3600
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $108.45 | Position: +$0.0600
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $108.02 | Position: -$0.5400
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Buy at: $107.56
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $107.06 | Position: -$1.0500
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $107.78 | Position: +$0.4700
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $107.94 | Position: +$0.6400
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $108.08 | Position: +$0.8900
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $107.75 | Position: -$0.0300
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Buy at: $106.92
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Buy at: $106.94
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $107.30 | Position: -$0.5900
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Buy at: $107.08
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $107.97 | Position: +$0.1600
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $108.42 | Position: +$0.5000
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $108.39 | Position: +$0.6700
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $108.86 | Position: +$0.6400
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $108.77 | Position: +$0.0200
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: +$2.7200
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Buy at: $108.43
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$2.1300
2021-08-09 11:59:26 c01ae99aeb99 root[60] DEBUG Sell at: $108.48 | Position: +$2.2000
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Sell at: $108.69 | Position: +$2.6100
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Sell at: $108.58 | Position: +$3.2700
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Sell at: $109.16 | Position: +$2.4100
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Sell at: $108.97 | Position: +$2.5900
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$2.8400
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$3.1400
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Sell at: $109.06 | Position: +$2.5400
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Buy at: $108.83
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Buy at: $108.67
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Buy at: $108.55
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$2.3000
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Buy at: $108.64
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Sell at: $108.66 | Position: +$2.2700
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Sell at: $108.92 | Position: +$1.6700
2021-08-09 11:59:27 c01ae99aeb99 root[60] DEBUG Sell at: $109.56 | Position: +$1.4800
2021-08-09 11:59:28 c01ae99aeb99 root[60] DEBUG Sell at: $109.52 | Position: +$1.9600
2021-08-09 11:59:28 c01ae99aeb99 root[60] DEBUG Sell at: $109.00 | Position: +$2.0800
2021-08-09 11:59:28 c01ae99aeb99 root[60] DEBUG Buy at: $108.86
2021-08-09 11:59:28 c01ae99aeb99 root[60] DEBUG Buy at: $108.71
2021-08-09 11:59:28 c01ae99aeb99 root[60] DEBUG Sell at: $109.31 | Position: +$2.3700
2021-08-09 11:59:28 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$2.3000
2021-08-09 11:59:28 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$1.0700
2021-08-09 11:59:28 c01ae99aeb99 root[60] DEBUG Sell at: $109.48 | Position: +$1.2900
2021-08-09 11:59:28 c01ae99aeb99 root[60] DEBUG Sell at: $109.53 | Position: +$0.7000
2021-08-09 11:59:28 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$0.7100
2021-08-09 11:59:28 c01ae99aeb99 root[60] DEBUG Sell at: $109.39 | Position: +$0.8400
2021-08-09 11:59:28 c01ae99aeb99 root[60] DEBUG Sell at: $109.36 | Position: +$0.7200
2021-08-09 11:59:28 c01ae99aeb99 root[60] INFO Episode 4/10 - Train Position: +$2454.7500  Val Position: +$29.9500  Train Loss: 0.2072693)
Episode 5/10: 100%|██████████| 2317/2317 [31:39<00:00,  1.22it/s]
2021-08-09 12:31:08 c01ae99aeb99 root[60] DEBUG Buy at: $109.72
2021-08-09 12:31:08 c01ae99aeb99 root[60] DEBUG Sell at: $108.88 | Position: -$0.8400
2021-08-09 12:31:08 c01ae99aeb99 root[60] DEBUG Buy at: $108.53
2021-08-09 12:31:08 c01ae99aeb99 root[60] DEBUG Sell at: $108.75 | Position: +$0.2200
2021-08-09 12:31:08 c01ae99aeb99 root[60] DEBUG Buy at: $109.60
2021-08-09 12:31:08 c01ae99aeb99 root[60] DEBUG Sell at: $109.64 | Position: +$0.0400
2021-08-09 12:31:09 c01ae99aeb99 root[60] DEBUG Buy at: $108.88
2021-08-09 12:31:09 c01ae99aeb99 root[60] DEBUG Buy at: $109.50
2021-08-09 12:31:09 c01ae99aeb99 root[60] DEBUG Sell at: $109.89 | Position: +$1.0100
2021-08-09 12:31:09 c01ae99aeb99 root[60] DEBUG Sell at: $109.97 | Position: +$0.4700
2021-08-09 12:31:09 c01ae99aeb99 root[60] DEBUG Buy at: $110.50
2021-08-09 12:31:09 c01ae99aeb99 root[60] DEBUG Sell at: $110.62 | Position: +$0.1200
2021-08-09 12:31:09 c01ae99aeb99 root[60] DEBUG Buy at: $110.69
2021-08-09 12:31:09 c01ae99aeb99 root[60] DEBUG Buy at: $111.06
2021-08-09 12:31:09 c01ae99aeb99 root[60] DEBUG Buy at: $110.58
2021-08-09 12:31:09 c01ae99aeb99 root[60] DEBUG Sell at: $111.92 | Position: +$1.2300
2021-08-09 12:31:09 c01ae99aeb99 root[60] DEBUG Sell at: $111.75 | Position: +$0.6900
2021-08-09 12:31:09 c01ae99aeb99 root[60] DEBUG Sell at: $111.89 | Position: +$1.3100
2021-08-09 12:31:10 c01ae99aeb99 root[60] DEBUG Buy at: $111.77
2021-08-09 12:31:10 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 12:31:10 c01ae99aeb99 root[60] DEBUG Sell at: $111.20 | Position: -$0.5700
2021-08-09 12:31:10 c01ae99aeb99 root[60] DEBUG Sell at: $111.36 | Position: +$0.1900
2021-08-09 12:31:10 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 12:31:10 c01ae99aeb99 root[60] DEBUG Buy at: $111.42
2021-08-09 12:31:10 c01ae99aeb99 root[60] DEBUG Buy at: $110.69
2021-08-09 12:31:10 c01ae99aeb99 root[60] DEBUG Buy at: $110.81
2021-08-09 12:31:10 c01ae99aeb99 root[60] DEBUG Buy at: $110.52
2021-08-09 12:31:10 c01ae99aeb99 root[60] DEBUG Sell at: $110.86 | Position: -$0.3100
2021-08-09 12:31:10 c01ae99aeb99 root[60] DEBUG Sell at: $111.36 | Position: -$0.0600
2021-08-09 12:31:10 c01ae99aeb99 root[60] DEBUG Sell at: $111.33 | Position: +$0.6400
2021-08-09 12:31:10 c01ae99aeb99 root[60] DEBUG Sell at: $111.67 | Position: +$0.8600
2021-08-09 12:31:10 c01ae99aeb99 root[60] DEBUG Sell at: $111.73 | Position: +$1.2100
2021-08-09 12:31:11 c01ae99aeb99 root[60] DEBUG Buy at: $112.19
2021-08-09 12:31:11 c01ae99aeb99 root[60] DEBUG Buy at: $111.59
2021-08-09 12:31:11 c01ae99aeb99 root[60] DEBUG Buy at: $111.42
2021-08-09 12:31:11 c01ae99aeb99 root[60] DEBUG Sell at: $111.39 | Position: -$0.8000
2021-08-09 12:31:11 c01ae99aeb99 root[60] DEBUG Buy at: $111.52
2021-08-09 12:31:11 c01ae99aeb99 root[60] DEBUG Buy at: $110.25
2021-08-09 12:31:11 c01ae99aeb99 root[60] DEBUG Buy at: $110.11
2021-08-09 12:31:11 c01ae99aeb99 root[60] DEBUG Buy at: $109.76
2021-08-09 12:31:11 c01ae99aeb99 root[60] DEBUG Buy at: $109.94
2021-08-09 12:31:11 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Buy at: $109.61
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Buy at: $109.59
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Sell at: $110.06 | Position: -$1.5300
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Buy at: $109.61
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Buy at: $109.52
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Sell at: $109.59 | Position: -$1.8300
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Buy at: $108.28
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Buy at: $108.14
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Sell at: $108.47 | Position: -$3.0500
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Sell at: $108.42 | Position: -$1.8300
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Buy at: $108.50
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Buy at: $108.39
2021-08-09 12:31:12 c01ae99aeb99 root[60] DEBUG Buy at: $108.56
2021-08-09 12:31:13 c01ae99aeb99 root[60] DEBUG Sell at: $108.56 | Position: -$1.5500
2021-08-09 12:31:13 c01ae99aeb99 root[60] DEBUG Buy at: $108.45
2021-08-09 12:31:13 c01ae99aeb99 root[60] DEBUG Buy at: $108.11
2021-08-09 12:31:13 c01ae99aeb99 root[60] DEBUG Buy at: $107.31
2021-08-09 12:31:13 c01ae99aeb99 root[60] DEBUG Buy at: $107.30
2021-08-09 12:31:13 c01ae99aeb99 root[60] DEBUG Buy at: $107.19
2021-08-09 12:31:13 c01ae99aeb99 root[60] DEBUG Buy at: $107.80
2021-08-09 12:31:13 c01ae99aeb99 root[60] DEBUG Buy at: $108.44
2021-08-09 12:31:13 c01ae99aeb99 root[60] DEBUG Sell at: $107.89 | Position: -$1.8700
2021-08-09 12:31:13 c01ae99aeb99 root[60] DEBUG Buy at: $107.81
2021-08-09 12:31:13 c01ae99aeb99 root[60] DEBUG Sell at: $108.72 | Position: -$1.2200
2021-08-09 12:31:13 c01ae99aeb99 root[60] DEBUG Buy at: $108.86
2021-08-09 12:31:13 c01ae99aeb99 root[60] DEBUG Buy at: $107.91
2021-08-09 12:31:13 c01ae99aeb99 root[60] DEBUG Buy at: $107.92
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Buy at: $107.94
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Buy at: $107.72
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Sell at: $108.22 | Position: -$1.0900
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: -$0.9400
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Sell at: $108.78 | Position: -$0.8100
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Sell at: $108.75 | Position: -$0.8600
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Buy at: $107.34
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Buy at: $105.95
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Buy at: $106.48
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Buy at: $106.28
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Buy at: $106.08
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Buy at: $105.31
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Buy at: $106.75
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Buy at: $105.91
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Buy at: $106.12
2021-08-09 12:31:14 c01ae99aeb99 root[60] DEBUG Buy at: $106.38
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Buy at: $106.62
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Buy at: $106.44
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Buy at: $106.14
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Buy at: $105.73
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Buy at: $106.12
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Buy at: $106.31
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Buy at: $106.39
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Sell at: $106.92 | Position: -$2.3900
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Sell at: $106.92 | Position: -$2.6000
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Buy at: $107.25
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Sell at: $108.11 | Position: -$0.1700
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: +$0.0000
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: -$0.0500
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Sell at: $108.45 | Position: -$0.0500
2021-08-09 12:31:15 c01ae99aeb99 root[60] DEBUG Sell at: $108.02 | Position: -$0.3700
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Buy at: $107.56
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Buy at: $107.56
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.08 | Position: -$0.4800
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Buy at: $107.18
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Buy at: $106.92
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Buy at: $106.94
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Sell at: $107.30 | Position: -$1.1500
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Sell at: $107.97 | Position: -$0.1400
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.42 | Position: +$1.1100
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.39 | Position: +$1.0900
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.86 | Position: +$1.6700
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.77 | Position: +$0.9700
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: +$0.2300
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Buy at: $108.43
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$0.8000
2021-08-09 12:31:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.48 | Position: -$0.3800
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.69 | Position: +$0.7800
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Buy at: $108.61
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.95 | Position: +$1.0300
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Buy at: $108.84
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.58 | Position: +$0.6400
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Sell at: $109.16 | Position: +$1.4400
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.97 | Position: +$1.6300
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$3.3300
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$2.8000
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Sell at: $109.06 | Position: +$2.7800
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.83 | Position: +$2.7500
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Buy at: $108.41
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Buy at: $108.55
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$3.3000
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Buy at: $108.64
2021-08-09 12:31:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.66 | Position: +$1.9100
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.92 | Position: +$3.0100
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.05 | Position: +$2.9300
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.56 | Position: +$3.1800
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.52 | Position: +$2.9000
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Buy at: $108.64
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Buy at: $108.86
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Buy at: $108.61
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.31 | Position: +$2.8700
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$3.2400
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$3.7700
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.48 | Position: +$3.3600
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.53 | Position: +$3.2200
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$2.9900
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Buy at: $109.44
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.39 | Position: +$2.1400
2021-08-09 12:31:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.36 | Position: +$1.8000
2021-08-09 12:31:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.64 | Position: +$2.0800
2021-08-09 12:31:19 c01ae99aeb99 root[60] DEBUG Buy at: $109.42
2021-08-09 12:31:19 c01ae99aeb99 root[60] DEBUG Buy at: $108.88
2021-08-09 12:31:19 c01ae99aeb99 root[60] INFO Episode 5/10 - Train Position: +$3631.4200  Val Position: +$46.8000  Train Loss: 0.2335540)
Episode 6/10: 100%|██████████| 2317/2317 [32:03<00:00,  1.20it/s]
2021-08-09 13:03:23 c01ae99aeb99 root[60] DEBUG Buy at: $109.72
2021-08-09 13:03:23 c01ae99aeb99 root[60] DEBUG Sell at: $108.53 | Position: -$1.1900
2021-08-09 13:03:23 c01ae99aeb99 root[60] DEBUG Buy at: $109.03
2021-08-09 13:03:23 c01ae99aeb99 root[60] DEBUG Buy at: $108.88
2021-08-09 13:03:23 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$0.4700
2021-08-09 13:03:23 c01ae99aeb99 root[60] DEBUG Sell at: $109.89 | Position: +$1.0100
2021-08-09 13:03:24 c01ae99aeb99 root[60] DEBUG Buy at: $110.62
2021-08-09 13:03:24 c01ae99aeb99 root[60] DEBUG Sell at: $110.62 | Position: +$0.0000
2021-08-09 13:03:24 c01ae99aeb99 root[60] DEBUG Buy at: $110.69
2021-08-09 13:03:24 c01ae99aeb99 root[60] DEBUG Sell at: $110.58 | Position: -$0.1100
2021-08-09 13:03:24 c01ae99aeb99 root[60] DEBUG Buy at: $111.77
2021-08-09 13:03:24 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 13:03:24 c01ae99aeb99 root[60] DEBUG Sell at: $111.20 | Position: -$0.5700
2021-08-09 13:03:24 c01ae99aeb99 root[60] DEBUG Buy at: $111.42
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Buy at: $110.69
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Buy at: $110.81
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Buy at: $109.97
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Buy at: $110.64
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Buy at: $110.86
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Sell at: $111.36 | Position: +$0.1900
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Sell at: $111.33 | Position: -$0.0900
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Buy at: $111.48
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Sell at: $111.67 | Position: +$0.9800
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Sell at: $111.73 | Position: +$0.9200
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Sell at: $111.48 | Position: +$1.5100
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Buy at: $111.14
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Buy at: $111.02
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Sell at: $112.03 | Position: +$1.3900
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Sell at: $112.00 | Position: +$1.1400
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Sell at: $112.06 | Position: +$0.5800
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Sell at: $111.97 | Position: +$0.8300
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Buy at: $111.92
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Sell at: $111.94 | Position: +$0.9200
2021-08-09 13:03:25 c01ae99aeb99 root[60] DEBUG Sell at: $111.86 | Position: -$0.0600
2021-08-09 13:03:26 c01ae99aeb99 root[60] DEBUG Buy at: $111.42
2021-08-09 13:03:26 c01ae99aeb99 root[60] DEBUG Buy at: $111.39
2021-08-09 13:03:26 c01ae99aeb99 root[60] DEBUG Buy at: $111.52
2021-08-09 13:03:26 c01ae99aeb99 root[60] DEBUG Buy at: $110.25
2021-08-09 13:03:26 c01ae99aeb99 root[60] DEBUG Buy at: $110.11
2021-08-09 13:03:26 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 13:03:26 c01ae99aeb99 root[60] DEBUG Buy at: $109.59
2021-08-09 13:03:26 c01ae99aeb99 root[60] DEBUG Buy at: $110.06
2021-08-09 13:03:26 c01ae99aeb99 root[60] DEBUG Sell at: $110.36 | Position: -$1.0600
2021-08-09 13:03:26 c01ae99aeb99 root[60] DEBUG Buy at: $109.61
2021-08-09 13:03:26 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Buy at: $108.28
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Buy at: $108.08
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Sell at: $108.47 | Position: -$2.9200
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Buy at: $108.42
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Buy at: $108.52
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Buy at: $108.50
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Buy at: $108.56
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Sell at: $108.11 | Position: -$3.4100
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Buy at: $107.31
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Buy at: $107.30
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Buy at: $107.78
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Buy at: $107.80
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Buy at: $108.44
2021-08-09 13:03:27 c01ae99aeb99 root[60] DEBUG Buy at: $107.89
2021-08-09 13:03:28 c01ae99aeb99 root[60] DEBUG Buy at: $107.83
2021-08-09 13:03:28 c01ae99aeb99 root[60] DEBUG Sell at: $108.72 | Position: -$1.5300
2021-08-09 13:03:28 c01ae99aeb99 root[60] DEBUG Sell at: $108.86 | Position: -$1.2500
2021-08-09 13:03:28 c01ae99aeb99 root[60] DEBUG Sell at: $108.50 | Position: -$0.8100
2021-08-09 13:03:28 c01ae99aeb99 root[60] DEBUG Buy at: $107.92
2021-08-09 13:03:28 c01ae99aeb99 root[60] DEBUG Sell at: $107.72 | Position: -$1.8700
2021-08-09 13:03:28 c01ae99aeb99 root[60] DEBUG Buy at: $108.22
2021-08-09 13:03:28 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: -$1.3900
2021-08-09 13:03:28 c01ae99aeb99 root[60] DEBUG Buy at: $108.75
2021-08-09 13:03:28 c01ae99aeb99 root[60] DEBUG Buy at: $107.34
2021-08-09 13:03:28 c01ae99aeb99 root[60] DEBUG Buy at: $105.95
2021-08-09 13:03:28 c01ae99aeb99 root[60] DEBUG Buy at: $106.48
2021-08-09 13:03:28 c01ae99aeb99 root[60] DEBUG Buy at: $106.28
2021-08-09 13:03:29 c01ae99aeb99 root[60] DEBUG Buy at: $105.67
2021-08-09 13:03:29 c01ae99aeb99 root[60] DEBUG Buy at: $105.31
2021-08-09 13:03:29 c01ae99aeb99 root[60] DEBUG Buy at: $106.75
2021-08-09 13:03:29 c01ae99aeb99 root[60] DEBUG Buy at: $105.91
2021-08-09 13:03:29 c01ae99aeb99 root[60] DEBUG Buy at: $106.12
2021-08-09 13:03:29 c01ae99aeb99 root[60] DEBUG Sell at: $106.64 | Position: -$2.9700
2021-08-09 13:03:29 c01ae99aeb99 root[60] DEBUG Buy at: $106.62
2021-08-09 13:03:29 c01ae99aeb99 root[60] DEBUG Buy at: $106.44
2021-08-09 13:03:29 c01ae99aeb99 root[60] DEBUG Buy at: $106.14
2021-08-09 13:03:29 c01ae99aeb99 root[60] DEBUG Buy at: $105.73
2021-08-09 13:03:29 c01ae99aeb99 root[60] DEBUG Buy at: $106.12
2021-08-09 13:03:29 c01ae99aeb99 root[60] DEBUG Buy at: $106.52
2021-08-09 13:03:29 c01ae99aeb99 root[60] DEBUG Buy at: $106.39
2021-08-09 13:03:29 c01ae99aeb99 root[60] DEBUG Buy at: $107.25
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Sell at: $108.11 | Position: -$1.2000
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Buy at: $108.14
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: -$0.1400
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Sell at: $108.45 | Position: +$0.3700
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Sell at: $107.56 | Position: -$0.8600
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Sell at: $107.83 | Position: -$0.3600
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Sell at: $107.94 | Position: -$0.5800
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Sell at: $107.75 | Position: -$0.7500
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Buy at: $107.18
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Buy at: $106.92
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Buy at: $106.94
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Sell at: $107.30 | Position: -$1.2600
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Sell at: $107.08 | Position: -$0.2300
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Sell at: $107.97 | Position: +$0.6700
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Sell at: $108.42 | Position: +$0.6400
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Sell at: $108.39 | Position: +$0.5900
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Sell at: $108.86 | Position: +$0.4200
2021-08-09 13:03:30 c01ae99aeb99 root[60] DEBUG Sell at: $108.77 | Position: +$0.8800
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: +$0.8400
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Buy at: $108.43
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$0.6900
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Sell at: $108.48 | Position: +$0.2600
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Buy at: $108.61
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Sell at: $108.66 | Position: -$0.0900
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Sell at: $108.95 | Position: +$1.6100
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Buy at: $108.03
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Sell at: $108.58 | Position: +$2.6300
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Sell at: $109.16 | Position: +$2.6800
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Sell at: $108.97 | Position: +$2.6900
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$3.6100
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$3.9700
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Sell at: $109.06 | Position: +$2.3100
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Sell at: $109.02 | Position: +$3.1100
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Sell at: $108.83 | Position: +$2.7100
2021-08-09 13:03:31 c01ae99aeb99 root[60] DEBUG Buy at: $108.41
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Buy at: $108.64
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Sell at: $108.66 | Position: +$2.0400
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Sell at: $108.92 | Position: +$2.4800
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Sell at: $109.05 | Position: +$2.9100
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Sell at: $109.56 | Position: +$3.8300
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Buy at: $109.52
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Sell at: $109.00 | Position: +$2.8800
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Buy at: $108.61
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Sell at: $109.31 | Position: +$2.7900
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$2.9900
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$2.2500
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Sell at: $109.48 | Position: +$1.3400
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Sell at: $109.53 | Position: +$2.3500
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$2.4600
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Buy at: $109.44
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Sell at: $109.39 | Position: +$2.4500
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Sell at: $109.36 | Position: +$0.9300
2021-08-09 13:03:32 c01ae99aeb99 root[60] DEBUG Sell at: $109.64 | Position: +$1.0300
2021-08-09 13:03:33 c01ae99aeb99 root[60] DEBUG Buy at: $109.42
2021-08-09 13:03:33 c01ae99aeb99 root[60] DEBUG Buy at: $108.88
2021-08-09 13:03:33 c01ae99aeb99 root[60] INFO Episode 6/10 - Train Position: +$3490.6700  Val Position: +$48.6500  Train Loss: 0.2594008)
Episode 7/10: 100%|██████████| 2317/2317 [31:36<00:00,  1.22it/s]
2021-08-09 13:35:10 c01ae99aeb99 root[60] DEBUG Buy at: $109.03
2021-08-09 13:35:10 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$0.4700
2021-08-09 13:35:10 c01ae99aeb99 root[60] DEBUG Buy at: $111.00
2021-08-09 13:35:10 c01ae99aeb99 root[60] DEBUG Sell at: $110.50 | Position: -$0.5000
2021-08-09 13:35:11 c01ae99aeb99 root[60] DEBUG Buy at: $110.69
2021-08-09 13:35:11 c01ae99aeb99 root[60] DEBUG Sell at: $110.58 | Position: -$0.1100
2021-08-09 13:35:11 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 13:35:11 c01ae99aeb99 root[60] DEBUG Buy at: $110.81
2021-08-09 13:35:12 c01ae99aeb99 root[60] DEBUG Sell at: $110.86 | Position: -$0.3100
2021-08-09 13:35:12 c01ae99aeb99 root[60] DEBUG Sell at: $111.33 | Position: +$0.5200
2021-08-09 13:35:12 c01ae99aeb99 root[60] DEBUG Buy at: $112.19
2021-08-09 13:35:12 c01ae99aeb99 root[60] DEBUG Buy at: $111.42
2021-08-09 13:35:13 c01ae99aeb99 root[60] DEBUG Buy at: $110.11
2021-08-09 13:35:13 c01ae99aeb99 root[60] DEBUG Buy at: $109.94
2021-08-09 13:35:13 c01ae99aeb99 root[60] DEBUG Sell at: $110.08 | Position: -$2.1100
2021-08-09 13:35:13 c01ae99aeb99 root[60] DEBUG Buy at: $110.06
2021-08-09 13:35:13 c01ae99aeb99 root[60] DEBUG Buy at: $109.52
2021-08-09 13:35:13 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: -$3.2800
2021-08-09 13:35:13 c01ae99aeb99 root[60] DEBUG Sell at: $108.47 | Position: -$1.6400
2021-08-09 13:35:13 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 13:35:14 c01ae99aeb99 root[60] DEBUG Buy at: $108.50
2021-08-09 13:35:14 c01ae99aeb99 root[60] DEBUG Sell at: $108.39 | Position: -$1.5500
2021-08-09 13:35:14 c01ae99aeb99 root[60] DEBUG Buy at: $108.56
2021-08-09 13:35:14 c01ae99aeb99 root[60] DEBUG Buy at: $108.45
2021-08-09 13:35:14 c01ae99aeb99 root[60] DEBUG Sell at: $108.11 | Position: -$1.9500
2021-08-09 13:35:14 c01ae99aeb99 root[60] DEBUG Buy at: $107.19
2021-08-09 13:35:14 c01ae99aeb99 root[60] DEBUG Sell at: $107.89 | Position: -$1.6300
2021-08-09 13:35:14 c01ae99aeb99 root[60] DEBUG Sell at: $107.89 | Position: -$0.3000
2021-08-09 13:35:14 c01ae99aeb99 root[60] DEBUG Buy at: $107.83
2021-08-09 13:35:14 c01ae99aeb99 root[60] DEBUG Sell at: $108.72 | Position: +$0.2200
2021-08-09 13:35:14 c01ae99aeb99 root[60] DEBUG Buy at: $107.92
2021-08-09 13:35:15 c01ae99aeb99 root[60] DEBUG Buy at: $107.72
2021-08-09 13:35:15 c01ae99aeb99 root[60] DEBUG Buy at: $108.75
2021-08-09 13:35:15 c01ae99aeb99 root[60] DEBUG Buy at: $107.34
2021-08-09 13:35:15 c01ae99aeb99 root[60] DEBUG Buy at: $105.95
2021-08-09 13:35:15 c01ae99aeb99 root[60] DEBUG Buy at: $106.48
2021-08-09 13:35:15 c01ae99aeb99 root[60] DEBUG Buy at: $106.75
2021-08-09 13:35:15 c01ae99aeb99 root[60] DEBUG Buy at: $105.91
2021-08-09 13:35:15 c01ae99aeb99 root[60] DEBUG Sell at: $106.64 | Position: -$1.9200
2021-08-09 13:35:15 c01ae99aeb99 root[60] DEBUG Buy at: $106.62
2021-08-09 13:35:16 c01ae99aeb99 root[60] DEBUG Buy at: $106.44
2021-08-09 13:35:16 c01ae99aeb99 root[60] DEBUG Sell at: $106.52 | Position: -$1.9300
2021-08-09 13:35:16 c01ae99aeb99 root[60] DEBUG Buy at: $108.14
2021-08-09 13:35:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: +$0.9500
2021-08-09 13:35:16 c01ae99aeb99 root[60] DEBUG Buy at: $107.56
2021-08-09 13:35:17 c01ae99aeb99 root[60] DEBUG Sell at: $107.30 | Position: -$0.5300
2021-08-09 13:35:17 c01ae99aeb99 root[60] DEBUG Sell at: $107.97 | Position: +$0.0500
2021-08-09 13:35:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.42 | Position: +$0.7000
2021-08-09 13:35:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.39 | Position: -$0.3600
2021-08-09 13:35:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.86 | Position: +$1.5200
2021-08-09 13:35:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: +$2.7200
2021-08-09 13:35:17 c01ae99aeb99 root[60] DEBUG Buy at: $108.43
2021-08-09 13:35:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$2.1300
2021-08-09 13:35:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.48 | Position: +$1.7300
2021-08-09 13:35:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.69 | Position: +$2.7800
2021-08-09 13:35:17 c01ae99aeb99 root[60] DEBUG Buy at: $108.61
2021-08-09 13:35:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.95 | Position: +$2.3300
2021-08-09 13:35:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.58 | Position: +$2.1400
2021-08-09 13:35:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.16 | Position: +$1.0200
2021-08-09 13:35:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.97 | Position: +$1.4100
2021-08-09 13:35:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$0.8500
2021-08-09 13:35:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$0.6700
2021-08-09 13:35:18 c01ae99aeb99 root[60] DEBUG Buy at: $108.64
2021-08-09 13:35:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.66 | Position: +$0.0200
2021-08-09 13:35:18 c01ae99aeb99 root[60] DEBUG Buy at: $108.86
2021-08-09 13:35:18 c01ae99aeb99 root[60] DEBUG Buy at: $108.61
2021-08-09 13:35:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.31 | Position: +$0.4500
2021-08-09 13:35:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$0.7700
2021-08-09 13:35:19 c01ae99aeb99 root[60] DEBUG Buy at: $109.44
2021-08-09 13:35:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.39 | Position: -$0.0500
2021-08-09 13:35:19 c01ae99aeb99 root[60] INFO Episode 7/10 - Train Position: +$3342.2900  Val Position: +$5.2800  Train Loss: 0.2758647)
Episode 8/10: 100%|██████████| 2317/2317 [31:51<00:00,  1.21it/s]
2021-08-09 14:07:11 c01ae99aeb99 root[60] DEBUG Buy at: $108.53
2021-08-09 14:07:11 c01ae99aeb99 root[60] DEBUG Sell at: $108.72 | Position: +$0.1900
2021-08-09 14:07:11 c01ae99aeb99 root[60] DEBUG Buy at: $108.42
2021-08-09 14:07:11 c01ae99aeb99 root[60] DEBUG Sell at: $108.55 | Position: +$0.1300
2021-08-09 14:07:11 c01ae99aeb99 root[60] DEBUG Buy at: $109.03
2021-08-09 14:07:11 c01ae99aeb99 root[60] DEBUG Buy at: $108.88
2021-08-09 14:07:11 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$0.4700
2021-08-09 14:07:11 c01ae99aeb99 root[60] DEBUG Sell at: $109.89 | Position: +$1.0100
2021-08-09 14:07:12 c01ae99aeb99 root[60] DEBUG Buy at: $110.62
2021-08-09 14:07:12 c01ae99aeb99 root[60] DEBUG Sell at: $110.70 | Position: +$0.0800
2021-08-09 14:07:12 c01ae99aeb99 root[60] DEBUG Buy at: $111.59
2021-08-09 14:07:12 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 14:07:12 c01ae99aeb99 root[60] DEBUG Sell at: $111.20 | Position: -$0.3900
2021-08-09 14:07:12 c01ae99aeb99 root[60] DEBUG Buy at: $111.42
2021-08-09 14:07:13 c01ae99aeb99 root[60] DEBUG Buy at: $110.81
2021-08-09 14:07:13 c01ae99aeb99 root[60] DEBUG Buy at: $110.64
2021-08-09 14:07:13 c01ae99aeb99 root[60] DEBUG Sell at: $110.86 | Position: -$0.3100
2021-08-09 14:07:13 c01ae99aeb99 root[60] DEBUG Sell at: $111.36 | Position: -$0.0600
2021-08-09 14:07:13 c01ae99aeb99 root[60] DEBUG Sell at: $111.33 | Position: +$0.5200
2021-08-09 14:07:13 c01ae99aeb99 root[60] DEBUG Sell at: $111.48 | Position: +$0.8400
2021-08-09 14:07:13 c01ae99aeb99 root[60] DEBUG Buy at: $111.02
2021-08-09 14:07:13 c01ae99aeb99 root[60] DEBUG Buy at: $111.67
2021-08-09 14:07:13 c01ae99aeb99 root[60] DEBUG Sell at: $112.03 | Position: +$1.0100
2021-08-09 14:07:13 c01ae99aeb99 root[60] DEBUG Sell at: $112.03 | Position: +$0.3600
2021-08-09 14:07:13 c01ae99aeb99 root[60] DEBUG Buy at: $111.92
2021-08-09 14:07:13 c01ae99aeb99 root[60] DEBUG Sell at: $111.94 | Position: +$0.0200
2021-08-09 14:07:14 c01ae99aeb99 root[60] DEBUG Buy at: $111.42
2021-08-09 14:07:14 c01ae99aeb99 root[60] DEBUG Buy at: $111.39
2021-08-09 14:07:14 c01ae99aeb99 root[60] DEBUG Buy at: $110.11
2021-08-09 14:07:14 c01ae99aeb99 root[60] DEBUG Buy at: $109.94
2021-08-09 14:07:14 c01ae99aeb99 root[60] DEBUG Buy at: $110.06
2021-08-09 14:07:14 c01ae99aeb99 root[60] DEBUG Buy at: $110.50
2021-08-09 14:07:14 c01ae99aeb99 root[60] DEBUG Buy at: $110.36
2021-08-09 14:07:14 c01ae99aeb99 root[60] DEBUG Buy at: $109.61
2021-08-09 14:07:14 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 14:07:14 c01ae99aeb99 root[60] DEBUG Buy at: $109.52
2021-08-09 14:07:14 c01ae99aeb99 root[60] DEBUG Buy at: $109.38
2021-08-09 14:07:15 c01ae99aeb99 root[60] DEBUG Buy at: $108.28
2021-08-09 14:07:15 c01ae99aeb99 root[60] DEBUG Sell at: $108.47 | Position: -$2.9500
2021-08-09 14:07:15 c01ae99aeb99 root[60] DEBUG Buy at: $108.50
2021-08-09 14:07:15 c01ae99aeb99 root[60] DEBUG Buy at: $108.56
2021-08-09 14:07:15 c01ae99aeb99 root[60] DEBUG Buy at: $108.45
2021-08-09 14:07:15 c01ae99aeb99 root[60] DEBUG Buy at: $107.31
2021-08-09 14:07:15 c01ae99aeb99 root[60] DEBUG Buy at: $107.30
2021-08-09 14:07:15 c01ae99aeb99 root[60] DEBUG Buy at: $107.19
2021-08-09 14:07:15 c01ae99aeb99 root[60] DEBUG Sell at: $107.78 | Position: -$3.6100
2021-08-09 14:07:15 c01ae99aeb99 root[60] DEBUG Sell at: $108.44 | Position: -$1.6700
2021-08-09 14:07:15 c01ae99aeb99 root[60] DEBUG Buy at: $107.89
2021-08-09 14:07:15 c01ae99aeb99 root[60] DEBUG Buy at: $107.83
2021-08-09 14:07:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.47 | Position: -$1.4700
2021-08-09 14:07:16 c01ae99aeb99 root[60] DEBUG Buy at: $108.50
2021-08-09 14:07:16 c01ae99aeb99 root[60] DEBUG Buy at: $107.92
2021-08-09 14:07:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.24 | Position: -$1.8200
2021-08-09 14:07:16 c01ae99aeb99 root[60] DEBUG Buy at: $107.94
2021-08-09 14:07:16 c01ae99aeb99 root[60] DEBUG Buy at: $107.88
2021-08-09 14:07:16 c01ae99aeb99 root[60] DEBUG Buy at: $108.22
2021-08-09 14:07:16 c01ae99aeb99 root[60] DEBUG Sell at: $108.64 | Position: -$1.8600
2021-08-09 14:07:16 c01ae99aeb99 root[60] DEBUG Buy at: $108.78
2021-08-09 14:07:16 c01ae99aeb99 root[60] DEBUG Buy at: $108.75
2021-08-09 14:07:16 c01ae99aeb99 root[60] DEBUG Buy at: $107.34
2021-08-09 14:07:16 c01ae99aeb99 root[60] DEBUG Buy at: $105.95
2021-08-09 14:07:16 c01ae99aeb99 root[60] DEBUG Buy at: $106.48
2021-08-09 14:07:16 c01ae99aeb99 root[60] DEBUG Sell at: $106.75 | Position: -$3.6100
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Buy at: $105.91
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Buy at: $106.38
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Sell at: $106.23 | Position: -$3.3800
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Buy at: $106.62
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Sell at: $106.44 | Position: -$2.8700
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Buy at: $105.41
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Buy at: $105.73
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Sell at: $106.52 | Position: -$3.0000
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Buy at: $106.39
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Buy at: $107.25
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Buy at: $107.55
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Sell at: $107.83 | Position: -$1.5500
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Buy at: $108.11
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Buy at: $108.14
2021-08-09 14:07:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: -$0.1400
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.45 | Position: -$0.0500
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Buy at: $107.56
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Sell at: $107.06 | Position: -$1.5000
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Buy at: $107.78
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Buy at: $107.94
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.08 | Position: -$0.3700
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Sell at: $107.75 | Position: +$0.4400
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Buy at: $107.18
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Buy at: $106.94
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Sell at: $107.30 | Position: +$0.0000
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Buy at: $107.97
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.39 | Position: +$1.2000
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.86 | Position: +$0.9700
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.77 | Position: +$0.9400
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: +$0.1700
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Buy at: $108.43
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$0.6900
2021-08-09 14:07:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.48 | Position: +$0.5400
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.69 | Position: +$0.8100
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Buy at: $108.61
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.95 | Position: +$0.7300
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Buy at: $108.84
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Buy at: $108.03
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.58 | Position: -$0.2000
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.16 | Position: +$0.4100
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.97 | Position: +$1.6300
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$3.3300
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$2.8000
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.06 | Position: +$3.1500
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.02 | Position: +$2.6400
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.83 | Position: +$2.2100
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.41 | Position: +$3.0000
2021-08-09 14:07:19 c01ae99aeb99 root[60] DEBUG Buy at: $108.67
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$2.8800
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $108.66 | Position: +$2.2700
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $108.92 | Position: +$1.6700
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.05 | Position: +$1.5000
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.56 | Position: +$1.4500
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.52 | Position: +$1.3800
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Buy at: $109.52
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.00 | Position: +$1.4400
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Buy at: $108.86
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $108.76 | Position: +$0.9800
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.31 | Position: +$1.3700
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$2.2000
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$2.5600
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.48 | Position: +$1.5100
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.53 | Position: +$1.1000
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$0.7700
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.44 | Position: +$0.6000
2021-08-09 14:07:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.39 | Position: +$1.3600
2021-08-09 14:07:21 c01ae99aeb99 root[60] DEBUG Sell at: $109.39 | Position: +$1.2000
2021-08-09 14:07:21 c01ae99aeb99 root[60] DEBUG Sell at: $109.36 | Position: +$0.6900
2021-08-09 14:07:21 c01ae99aeb99 root[60] DEBUG Sell at: $109.64 | Position: +$0.1200
2021-08-09 14:07:21 c01ae99aeb99 root[60] DEBUG Buy at: $108.88
2021-08-09 14:07:21 c01ae99aeb99 root[60] INFO Episode 8/10 - Train Position: +$3689.8100  Val Position: +$26.5300  Train Loss: 0.2615593)
Episode 9/10: 100%|██████████| 2317/2317 [31:47<00:00,  1.21it/s]
2021-08-09 14:39:09 c01ae99aeb99 root[60] DEBUG Buy at: $109.72
2021-08-09 14:39:09 c01ae99aeb99 root[60] DEBUG Buy at: $108.53
2021-08-09 14:39:09 c01ae99aeb99 root[60] DEBUG Sell at: $108.72 | Position: -$1.0000
2021-08-09 14:39:09 c01ae99aeb99 root[60] DEBUG Buy at: $108.42
2021-08-09 14:39:09 c01ae99aeb99 root[60] DEBUG Sell at: $108.55 | Position: +$0.0200
2021-08-09 14:39:09 c01ae99aeb99 root[60] DEBUG Sell at: $108.17 | Position: -$0.2500
2021-08-09 14:39:09 c01ae99aeb99 root[60] DEBUG Buy at: $109.60
2021-08-09 14:39:09 c01ae99aeb99 root[60] DEBUG Sell at: $109.64 | Position: +$0.0400
2021-08-09 14:39:09 c01ae99aeb99 root[60] DEBUG Buy at: $109.55
2021-08-09 14:39:10 c01ae99aeb99 root[60] DEBUG Buy at: $109.39
2021-08-09 14:39:10 c01ae99aeb99 root[60] DEBUG Buy at: $109.03
2021-08-09 14:39:10 c01ae99aeb99 root[60] DEBUG Sell at: $109.89 | Position: +$0.3400
2021-08-09 14:39:10 c01ae99aeb99 root[60] DEBUG Sell at: $109.97 | Position: +$0.5800
2021-08-09 14:39:10 c01ae99aeb99 root[60] DEBUG Sell at: $109.73 | Position: +$0.7000
2021-08-09 14:39:10 c01ae99aeb99 root[60] DEBUG Buy at: $110.62
2021-08-09 14:39:10 c01ae99aeb99 root[60] DEBUG Sell at: $110.62 | Position: +$0.0000
2021-08-09 14:39:10 c01ae99aeb99 root[60] DEBUG Buy at: $111.06
2021-08-09 14:39:10 c01ae99aeb99 root[60] DEBUG Sell at: $110.58 | Position: -$0.4800
2021-08-09 14:39:10 c01ae99aeb99 root[60] DEBUG Buy at: $111.00
2021-08-09 14:39:11 c01ae99aeb99 root[60] DEBUG Sell at: $111.39 | Position: +$0.3900
2021-08-09 14:39:11 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 14:39:11 c01ae99aeb99 root[60] DEBUG Buy at: $111.39
2021-08-09 14:39:11 c01ae99aeb99 root[60] DEBUG Buy at: $109.97
2021-08-09 14:39:11 c01ae99aeb99 root[60] DEBUG Sell at: $110.64 | Position: -$0.5300
2021-08-09 14:39:11 c01ae99aeb99 root[60] DEBUG Buy at: $110.52
2021-08-09 14:39:11 c01ae99aeb99 root[60] DEBUG Buy at: $110.64
2021-08-09 14:39:11 c01ae99aeb99 root[60] DEBUG Buy at: $110.86
2021-08-09 14:39:11 c01ae99aeb99 root[60] DEBUG Sell at: $111.36 | Position: -$0.0300
2021-08-09 14:39:12 c01ae99aeb99 root[60] DEBUG Sell at: $111.33 | Position: +$1.3600
2021-08-09 14:39:12 c01ae99aeb99 root[60] DEBUG Sell at: $111.48 | Position: +$0.9600
2021-08-09 14:39:12 c01ae99aeb99 root[60] DEBUG Sell at: $111.73 | Position: +$1.0900
2021-08-09 14:39:12 c01ae99aeb99 root[60] DEBUG Sell at: $111.48 | Position: +$0.6200
2021-08-09 14:39:12 c01ae99aeb99 root[60] DEBUG Buy at: $111.14
2021-08-09 14:39:12 c01ae99aeb99 root[60] DEBUG Sell at: $111.67 | Position: +$0.5300
2021-08-09 14:39:12 c01ae99aeb99 root[60] DEBUG Buy at: $112.03
2021-08-09 14:39:12 c01ae99aeb99 root[60] DEBUG Sell at: $112.00 | Position: -$0.0300
2021-08-09 14:39:12 c01ae99aeb99 root[60] DEBUG Buy at: $111.86
2021-08-09 14:39:12 c01ae99aeb99 root[60] DEBUG Sell at: $112.19 | Position: +$0.3300
2021-08-09 14:39:12 c01ae99aeb99 root[60] DEBUG Buy at: $111.42
2021-08-09 14:39:12 c01ae99aeb99 root[60] DEBUG Buy at: $111.39
2021-08-09 14:39:13 c01ae99aeb99 root[60] DEBUG Buy at: $109.61
2021-08-09 14:39:13 c01ae99aeb99 root[60] DEBUG Buy at: $109.86
2021-08-09 14:39:13 c01ae99aeb99 root[60] DEBUG Buy at: $110.08
2021-08-09 14:39:13 c01ae99aeb99 root[60] DEBUG Sell at: $110.06 | Position: -$1.3600
2021-08-09 14:39:13 c01ae99aeb99 root[60] DEBUG Buy at: $110.50
2021-08-09 14:39:13 c01ae99aeb99 root[60] DEBUG Buy at: $109.38
2021-08-09 14:39:13 c01ae99aeb99 root[60] DEBUG Buy at: $108.08
2021-08-09 14:39:13 c01ae99aeb99 root[60] DEBUG Sell at: $108.47 | Position: -$2.9200
2021-08-09 14:39:13 c01ae99aeb99 root[60] DEBUG Buy at: $108.42
2021-08-09 14:39:14 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 14:39:14 c01ae99aeb99 root[60] DEBUG Buy at: $108.50
2021-08-09 14:39:14 c01ae99aeb99 root[60] DEBUG Buy at: $108.56
2021-08-09 14:39:14 c01ae99aeb99 root[60] DEBUG Buy at: $108.45
2021-08-09 14:39:14 c01ae99aeb99 root[60] DEBUG Buy at: $107.30
2021-08-09 14:39:14 c01ae99aeb99 root[60] DEBUG Buy at: $107.19
2021-08-09 14:39:14 c01ae99aeb99 root[60] DEBUG Buy at: $107.78
2021-08-09 14:39:14 c01ae99aeb99 root[60] DEBUG Sell at: $107.80 | Position: -$1.8100
2021-08-09 14:39:14 c01ae99aeb99 root[60] DEBUG Sell at: $108.44 | Position: -$1.4200
2021-08-09 14:39:14 c01ae99aeb99 root[60] DEBUG Buy at: $107.83
2021-08-09 14:39:14 c01ae99aeb99 root[60] DEBUG Buy at: $108.47
2021-08-09 14:39:14 c01ae99aeb99 root[60] DEBUG Buy at: $108.86
2021-08-09 14:39:15 c01ae99aeb99 root[60] DEBUG Sell at: $108.47 | Position: -$1.6100
2021-08-09 14:39:15 c01ae99aeb99 root[60] DEBUG Sell at: $108.50 | Position: -$2.0000
2021-08-09 14:39:15 c01ae99aeb99 root[60] DEBUG Buy at: $107.92
2021-08-09 14:39:15 c01ae99aeb99 root[60] DEBUG Buy at: $107.94
2021-08-09 14:39:15 c01ae99aeb99 root[60] DEBUG Buy at: $107.72
2021-08-09 14:39:15 c01ae99aeb99 root[60] DEBUG Sell at: $108.22 | Position: -$1.1600
2021-08-09 14:39:15 c01ae99aeb99 root[60] DEBUG Buy at: $108.61
2021-08-09 14:39:15 c01ae99aeb99 root[60] DEBUG Buy at: $108.75
2021-08-09 14:39:15 c01ae99aeb99 root[60] DEBUG Buy at: $107.34
2021-08-09 14:39:15 c01ae99aeb99 root[60] DEBUG Buy at: $106.48
2021-08-09 14:39:16 c01ae99aeb99 root[60] DEBUG Buy at: $106.75
2021-08-09 14:39:16 c01ae99aeb99 root[60] DEBUG Buy at: $106.12
2021-08-09 14:39:16 c01ae99aeb99 root[60] DEBUG Buy at: $106.62
2021-08-09 14:39:16 c01ae99aeb99 root[60] DEBUG Buy at: $106.44
2021-08-09 14:39:16 c01ae99aeb99 root[60] DEBUG Buy at: $105.73
2021-08-09 14:39:16 c01ae99aeb99 root[60] DEBUG Buy at: $106.52
2021-08-09 14:39:16 c01ae99aeb99 root[60] DEBUG Sell at: $106.31 | Position: -$1.7700
2021-08-09 14:39:16 c01ae99aeb99 root[60] DEBUG Buy at: $106.39
2021-08-09 14:39:16 c01ae99aeb99 root[60] DEBUG Sell at: $106.92 | Position: -$1.5000
2021-08-09 14:39:16 c01ae99aeb99 root[60] DEBUG Buy at: $107.25
2021-08-09 14:39:16 c01ae99aeb99 root[60] DEBUG Buy at: $107.83
2021-08-09 14:39:16 c01ae99aeb99 root[60] DEBUG Buy at: $108.11
2021-08-09 14:39:16 c01ae99aeb99 root[60] DEBUG Buy at: $108.08
2021-08-09 14:39:16 c01ae99aeb99 root[60] DEBUG Buy at: $108.14
2021-08-09 14:39:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: -$0.0500
2021-08-09 14:39:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.45 | Position: -$0.0500
2021-08-09 14:39:17 c01ae99aeb99 root[60] DEBUG Buy at: $108.02
2021-08-09 14:39:17 c01ae99aeb99 root[60] DEBUG Buy at: $107.56
2021-08-09 14:39:17 c01ae99aeb99 root[60] DEBUG Sell at: $107.78 | Position: -$0.7800
2021-08-09 14:39:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.08 | Position: -$0.3700
2021-08-09 14:39:17 c01ae99aeb99 root[60] DEBUG Buy at: $107.18
2021-08-09 14:39:17 c01ae99aeb99 root[60] DEBUG Buy at: $106.94
2021-08-09 14:39:17 c01ae99aeb99 root[60] DEBUG Sell at: $107.97 | Position: +$0.6700
2021-08-09 14:39:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.42 | Position: +$1.2300
2021-08-09 14:39:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.39 | Position: +$0.6100
2021-08-09 14:39:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.86 | Position: +$1.0300
2021-08-09 14:39:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.77 | Position: +$0.3000
2021-08-09 14:39:17 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: -$0.1900
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Buy at: $108.43
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$0.6900
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.48 | Position: +$0.5400
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.69 | Position: +$0.9700
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Buy at: $108.61
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.66 | Position: +$0.0500
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.95 | Position: +$0.2000
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Buy at: $108.84
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.58 | Position: +$1.2400
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.16 | Position: +$2.6800
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.97 | Position: +$2.2200
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$3.1600
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$2.6600
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.06 | Position: +$2.6200
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Sell at: $109.02 | Position: +$3.2900
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.83 | Position: +$2.3100
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Sell at: $108.41 | Position: +$2.0200
2021-08-09 14:39:18 c01ae99aeb99 root[60] DEBUG Buy at: $108.67
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$1.3600
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.64 | Position: +$0.8100
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.66 | Position: +$0.5500
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.92 | Position: +$0.8400
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.05 | Position: +$0.9100
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.56 | Position: +$1.5400
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.52 | Position: +$1.9600
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Buy at: $109.52
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.00 | Position: +$1.8200
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Buy at: $108.64
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Buy at: $108.86
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $108.76 | Position: +$1.8200
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Buy at: $108.71
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.31 | Position: +$0.8800
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$0.7700
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$0.6600
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.48 | Position: +$1.2900
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.53 | Position: +$0.8600
2021-08-09 14:39:19 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: -$0.1400
2021-08-09 14:39:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.44 | Position: +$0.8000
2021-08-09 14:39:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.39 | Position: +$0.5300
2021-08-09 14:39:20 c01ae99aeb99 root[60] DEBUG Sell at: $109.39 | Position: +$0.6800
2021-08-09 14:39:20 c01ae99aeb99 root[60] DEBUG Buy at: $109.42
2021-08-09 14:39:20 c01ae99aeb99 root[60] INFO Episode 9/10 - Train Position: +$3320.7900  Val Position: +$34.0800  Train Loss: 0.2329046)
Episode 10/10: 100%|██████████| 2317/2317 [32:30<00:00,  1.19it/s]
INFO:tensorflow:Assets written to: models/model_debug_10_10/assets
2021-08-09 15:11:51 c01ae99aeb99 tensorflow[60] INFO Assets written to: models/model_debug_10_10/assets
2021-08-09 15:11:51 c01ae99aeb99 root[60] DEBUG Buy at: $109.72
2021-08-09 15:11:51 c01ae99aeb99 root[60] DEBUG Buy at: $108.53
2021-08-09 15:11:51 c01ae99aeb99 root[60] DEBUG Sell at: $108.75 | Position: -$0.9700
2021-08-09 15:11:51 c01ae99aeb99 root[60] DEBUG Buy at: $108.17
2021-08-09 15:11:51 c01ae99aeb99 root[60] DEBUG Buy at: $108.42
2021-08-09 15:11:51 c01ae99aeb99 root[60] DEBUG Sell at: $108.55 | Position: +$0.0200
2021-08-09 15:11:51 c01ae99aeb99 root[60] DEBUG Sell at: $108.17 | Position: +$0.0000
2021-08-09 15:11:51 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: +$0.2500
2021-08-09 15:11:52 c01ae99aeb99 root[60] DEBUG Buy at: $109.60
2021-08-09 15:11:52 c01ae99aeb99 root[60] DEBUG Sell at: $109.64 | Position: +$0.0400
2021-08-09 15:11:52 c01ae99aeb99 root[60] DEBUG Buy at: $109.39
2021-08-09 15:11:52 c01ae99aeb99 root[60] DEBUG Buy at: $109.03
2021-08-09 15:11:52 c01ae99aeb99 root[60] DEBUG Buy at: $108.88
2021-08-09 15:11:52 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$0.1100
2021-08-09 15:11:52 c01ae99aeb99 root[60] DEBUG Sell at: $109.89 | Position: +$0.8600
2021-08-09 15:11:52 c01ae99aeb99 root[60] DEBUG Sell at: $109.97 | Position: +$1.0900
2021-08-09 15:11:53 c01ae99aeb99 root[60] DEBUG Buy at: $111.06
2021-08-09 15:11:53 c01ae99aeb99 root[60] DEBUG Sell at: $110.58 | Position: -$0.4800
2021-08-09 15:11:53 c01ae99aeb99 root[60] DEBUG Buy at: $111.89
2021-08-09 15:11:53 c01ae99aeb99 root[60] DEBUG Buy at: $111.77
2021-08-09 15:11:53 c01ae99aeb99 root[60] DEBUG Buy at: $111.59
2021-08-09 15:11:53 c01ae99aeb99 root[60] DEBUG Buy at: $111.17
2021-08-09 15:11:53 c01ae99aeb99 root[60] DEBUG Sell at: $111.20 | Position: -$0.6900
2021-08-09 15:11:53 c01ae99aeb99 root[60] DEBUG Sell at: $111.36 | Position: -$0.4100
2021-08-09 15:11:53 c01ae99aeb99 root[60] DEBUG Buy at: $111.42
2021-08-09 15:11:53 c01ae99aeb99 root[60] DEBUG Buy at: $111.39
2021-08-09 15:11:53 c01ae99aeb99 root[60] DEBUG Buy at: $110.69
2021-08-09 15:11:53 c01ae99aeb99 root[60] DEBUG Buy at: $110.81
2021-08-09 15:11:53 c01ae99aeb99 root[60] DEBUG Buy at: $109.92
2021-08-09 15:11:53 c01ae99aeb99 root[60] DEBUG Buy at: $109.97
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Sell at: $110.64 | Position: -$0.9500
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Buy at: $110.52
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Buy at: $110.86
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.33 | Position: +$0.1600
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.48 | Position: +$0.0600
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.67 | Position: +$0.2800
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.73 | Position: +$1.0400
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.48 | Position: +$0.6700
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.14 | Position: +$1.2200
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.67 | Position: +$1.7000
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Sell at: $112.03 | Position: +$1.5100
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Sell at: $112.03 | Position: +$1.1700
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Buy at: $112.00
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Buy at: $112.06
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.97 | Position: -$0.0300
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Buy at: $111.92
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Sell at: $111.94 | Position: -$0.1200
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Buy at: $111.86
2021-08-09 15:11:54 c01ae99aeb99 root[60] DEBUG Sell at: $112.19 | Position: +$0.2700
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $111.64
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $111.42
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $111.39
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $111.52
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $110.78
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $110.25
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $110.11
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $109.76
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $109.61
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $109.59
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $109.86
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $110.08
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Sell at: $110.06 | Position: -$1.8000
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $110.50
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $109.61
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $109.31
2021-08-09 15:11:55 c01ae99aeb99 root[60] DEBUG Buy at: $109.38
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $109.59
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $109.61
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.28
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.08
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Sell at: $108.47 | Position: -$3.1700
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.44
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.50
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.56
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.56
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.45
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $108.11
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $107.31
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $107.31
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $107.30
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $107.19
2021-08-09 15:11:56 c01ae99aeb99 root[60] DEBUG Buy at: $107.80
2021-08-09 15:11:57 c01ae99aeb99 root[60] DEBUG Buy at: $108.44
2021-08-09 15:11:57 c01ae99aeb99 root[60] DEBUG Buy at: $107.89
2021-08-09 15:11:57 c01ae99aeb99 root[60] DEBUG Buy at: $107.83
2021-08-09 15:11:57 c01ae99aeb99 root[60] DEBUG Buy at: $107.81
2021-08-09 15:11:57 c01ae99aeb99 root[60] DEBUG Buy at: $108.72
2021-08-09 15:11:57 c01ae99aeb99 root[60] DEBUG Buy at: $108.86
2021-08-09 15:11:57 c01ae99aeb99 root[60] DEBUG Buy at: $108.50
2021-08-09 15:11:57 c01ae99aeb99 root[60] DEBUG Buy at: $107.91
2021-08-09 15:11:57 c01ae99aeb99 root[60] DEBUG Buy at: $107.92
2021-08-09 15:11:57 c01ae99aeb99 root[60] DEBUG Buy at: $108.24
2021-08-09 15:11:57 c01ae99aeb99 root[60] DEBUG Buy at: $107.94
2021-08-09 15:11:57 c01ae99aeb99 root[60] DEBUG Buy at: $107.72
2021-08-09 15:11:57 c01ae99aeb99 root[60] DEBUG Buy at: $108.64
2021-08-09 15:11:57 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: -$2.7500
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Sell at: $108.75 | Position: -$2.6400
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Sell at: $107.34 | Position: -$4.1800
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Buy at: $105.95
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Buy at: $106.48
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Buy at: $106.08
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Buy at: $105.67
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Buy at: $105.31
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Buy at: $106.12
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Buy at: $106.38
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Sell at: $106.23 | Position: -$4.5500
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Buy at: $106.62
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Buy at: $106.44
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Buy at: $105.41
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Buy at: $106.14
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Buy at: $105.73
2021-08-09 15:11:58 c01ae99aeb99 root[60] DEBUG Buy at: $106.52
2021-08-09 15:11:59 c01ae99aeb99 root[60] DEBUG Buy at: $106.31
2021-08-09 15:11:59 c01ae99aeb99 root[60] DEBUG Sell at: $106.22 | Position: -$4.0300
2021-08-09 15:11:59 c01ae99aeb99 root[60] DEBUG Buy at: $106.39
2021-08-09 15:11:59 c01ae99aeb99 root[60] DEBUG Sell at: $106.92 | Position: -$3.1900
2021-08-09 15:11:59 c01ae99aeb99 root[60] DEBUG Sell at: $107.25 | Position: -$2.5100
2021-08-09 15:11:59 c01ae99aeb99 root[60] DEBUG Buy at: $108.11
2021-08-09 15:11:59 c01ae99aeb99 root[60] DEBUG Buy at: $108.14
2021-08-09 15:11:59 c01ae99aeb99 root[60] DEBUG Sell at: $108.14 | Position: -$1.4700
2021-08-09 15:11:59 c01ae99aeb99 root[60] DEBUG Sell at: $108.45 | Position: -$1.1400
2021-08-09 15:11:59 c01ae99aeb99 root[60] DEBUG Buy at: $107.56
2021-08-09 15:11:59 c01ae99aeb99 root[60] DEBUG Sell at: $107.78 | Position: -$2.0800
2021-08-09 15:11:59 c01ae99aeb99 root[60] DEBUG Sell at: $108.08 | Position: -$2.0000
2021-08-09 15:11:59 c01ae99aeb99 root[60] DEBUG Buy at: $107.75
2021-08-09 15:11:59 c01ae99aeb99 root[60] DEBUG Buy at: $107.18
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Buy at: $106.92
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Buy at: $107.30
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Buy at: $107.97
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Buy at: $108.42
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.39 | Position: -$2.1100
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.86 | Position: -$0.7500
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.77 | Position: -$0.5400
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.67 | Position: -$0.7100
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Buy at: $108.43
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: -$0.9800
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.48 | Position: -$1.1300
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.69 | Position: +$0.4100
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Buy at: $108.61
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.95 | Position: +$0.8700
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Buy at: $108.84
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Buy at: $108.03
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Buy at: $108.19
2021-08-09 15:12:00 c01ae99aeb99 root[60] DEBUG Sell at: $108.58 | Position: +$0.3900
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.16 | Position: +$0.7200
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $108.97 | Position: +$0.4700
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$0.7200
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.28 | Position: +$0.7200
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.06 | Position: +$0.6100
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.02 | Position: +$0.9100
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $108.83 | Position: +$1.5200
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $108.41 | Position: +$1.1000
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Buy at: $108.75
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Buy at: $108.67
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $108.61 | Position: +$1.3100
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $108.64 | Position: +$1.4500
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $108.66 | Position: +$0.8600
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $108.92 | Position: +$0.4800
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.05 | Position: +$1.1600
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.56 | Position: +$1.7300
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.52 | Position: +$1.7100
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Buy at: $109.52
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $109.00 | Position: +$0.2800
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Buy at: $108.86
2021-08-09 15:12:01 c01ae99aeb99 root[60] DEBUG Sell at: $108.76 | Position: -$0.1000
2021-08-09 15:12:02 c01ae99aeb99 root[60] DEBUG Buy at: $108.56
2021-08-09 15:12:02 c01ae99aeb99 root[60] DEBUG Buy at: $108.71
2021-08-09 15:12:02 c01ae99aeb99 root[60] DEBUG Sell at: $109.31 | Position: +$0.8100
2021-08-09 15:12:02 c01ae99aeb99 root[60] DEBUG Sell at: $109.50 | Position: +$1.5900
2021-08-09 15:12:02 c01ae99aeb99 root[60] DEBUG Sell at: $109.48 | Position: +$1.5600
2021-08-09 15:12:02 c01ae99aeb99 root[60] DEBUG Sell at: $109.53 | Position: +$1.2900
2021-08-09 15:12:02 c01ae99aeb99 root[60] DEBUG Sell at: $109.38 | Position: +$1.4400
2021-08-09 15:12:02 c01ae99aeb99 root[60] DEBUG Sell at: $109.44 | Position: +$1.7200
2021-08-09 15:12:02 c01ae99aeb99 root[60] DEBUG Sell at: $109.39 | Position: +$0.7500
2021-08-09 15:12:02 c01ae99aeb99 root[60] DEBUG Sell at: $109.39 | Position: +$3.4400
2021-08-09 15:12:02 c01ae99aeb99 root[60] DEBUG Sell at: $109.36 | Position: +$2.8800
2021-08-09 15:12:02 c01ae99aeb99 root[60] DEBUG Sell at: $109.64 | Position: +$3.5600
2021-08-09 15:12:02 c01ae99aeb99 root[60] DEBUG Buy at: $109.42
2021-08-09 15:12:02 c01ae99aeb99 root[60] DEBUG Buy at: $108.88
2021-08-09 15:12:02 c01ae99aeb99 root[60] INFO Episode 10/10 - Train Position: +$5106.7700  Val Position: +$1.4300  Train Loss: 0.2320849)
```
