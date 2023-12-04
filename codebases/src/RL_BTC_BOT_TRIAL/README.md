Buy sell tracker for BTCUSD (historical) pairs. Proximal Policy Optimization (PPO) agent have been utilized on this trial.

Outcome visualizer (matplotlib, buy-sell) :

![viz](https://github.com/TashinAhmed/TradeX/blob/main/codebases/src/RL_BTC_BOT_TRIAL/IMAGES/gameplay.gif)


More on the outcomes can be found from [here](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/RL_BTC_BOT_TRIAL/IMAGES)

weight files, parameters, logs are from [here](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/RL_BTC_BOT_TRIAL/2021_02_21_17_54_Crypto_trader)

## *** STARTER GUIDE***
* ```indicators.py``` - will use the technical indicators on decision making. can be imported from ./methods/technical_directories dir as well.
* ```model.py``` - implemented DL models, can be implemented from ./methods/AI_methods as well.
* ``` multiprocessing_env.py``` - can be used via parallel GPUs.

- run ```python download.py``` - it will trigger the downloader to download the dataset from bitfinex.
- run ```python RL-Bitcoin-trading-bot_7.py``` to run the custom environment and agent file.
- multiple indicators can be added in ```indicators.py```


Requirements:

```
# This file may be used to create an environment using:
# $ conda create --name <env> --file <this file>
# platform: win-64
absl-py=1.0.0=pypi_0
astunparse=1.6.3=pypi_0
blas=1.0=mkl
ca-certificates=2021.10.26=haa95532_2
cachetools=4.2.4=pypi_0
certifi=2021.10.8=py38haa95532_0
charset-normalizer=2.0.9=pypi_0
cycler=0.11.0=pypi_0
fonttools=4.28.2=pypi_0
gast=0.3.3=pypi_0
google-auth=2.3.3=pypi_0
google-auth-oauthlib=0.4.6=pypi_0
google-pasta=0.2.0=pypi_0
grpcio=1.42.0=pypi_0
h5py=2.10.0=pypi_0
icc_rt=2019.0.0=h0cc432a_1
idna=3.3=pypi_0
importlib-metadata=4.8.2=pypi_0
intel-openmp=2021.4.0=haa95532_3556
keras-preprocessing=1.1.2=pypi_0
kiwisolver=1.3.2=pypi_0
markdown=3.3.6=pypi_0
matplotlib=3.5.0=pypi_0
mkl=2021.4.0=haa95532_640
mkl-service=2.4.0=py38h2bbff1b_0
mkl_fft=1.3.1=py38h277e83a_0
mkl_random=1.2.2=py38hf11a4ad_0
mplfinance=0.12.7a17=pypi_0
numpy=1.18.5=pypi_0
numpy-base=1.21.2=py38h0829f74_0
oauthlib=3.1.1=pypi_0
opencv-python=4.5.4.60=pypi_0
openssl=1.1.1l=h2bbff1b_0
opt-einsum=3.3.0=pypi_0
packaging=21.3=pypi_0
pandas=1.3.4=pypi_0
pillow=8.4.0=pypi_0
pip=21.2.2=py38haa95532_0
protobuf=3.19.1=pypi_0
pyasn1=0.4.8=pypi_0
pyasn1-modules=0.2.8=pypi_0
pyparsing=3.0.6=pypi_0
python=3.8.12=h6244533_0
python-dateutil=2.8.2=pypi_0
pytz=2021.3=pypi_0
requests=2.26.0=pypi_0
requests-oauthlib=1.3.0=pypi_0
rsa=4.8=pypi_0
scipy=1.7.3=pypi_0
seaborn=0.11.2=pypi_0
setuptools=58.0.4=py38haa95532_0
setuptools-scm=6.3.2=pypi_0
six=1.16.0=pyhd3eb1b0_0
sqlite=3.36.0=h2bbff1b_0
ta=0.8.0=pypi_0
tensorboard=2.7.0=pypi_0
tensorboard-data-server=0.6.1=pypi_0
tensorboard-plugin-wit=1.8.0=pypi_0
tensorboardx=2.4.1=pypi_0
tensorflow=2.3.1=pypi_0
tensorflow-estimator=2.3.0=pypi_0
tensorflow-gpu=2.3.1=pypi_0
tensorflow-gpu-estimator=2.3.0=pypi_0
termcolor=1.1.0=pypi_0
tomli=1.2.2=pypi_0
urllib3=1.26.7=pypi_0
vc=14.2=h21ff451_1
vs2015_runtime=14.27.29016=h5e58377_2
werkzeug=2.0.2=pypi_0
wheel=0.37.0=pyhd3eb1b0_1
wincertstore=0.2=py38haa95532_2
wrapt=1.13.3=pypi_0
zipp=3.6.0=pypi_0
```

