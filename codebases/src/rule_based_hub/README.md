# RBTB (Rule based bot hub)
Rule based trading bot

Data downloaded by/from [Rapid API](https://rapidapi.com/collection/stock-market-apis)

## Latest work updated on RBTB2
- real time close price and different indicators difference threshold; This threshold would act as a Trigger whether to Buy/Sell if other conditions satisfied.
- three slope calculation thresholds (which count of EMA(20,100,200))
- close value adjacent to EMA(20,100,200) threshold while there is a fixed trend(up/down). It will trigger Buy or Sell directly.
- three different distance thresholds for earlier Buy and Sell trigger. 

## LATEST
### RBTB4
### ***STARTER GUIDE***

- run `python stage_one.py` for running a simple SMA, EMA based bot.
-  

Requirements:

```
# This file may be used to create an environment using:
# $ conda create --name <env> --file <this file>
# platform: osx-arm64
absl-py=0.10.0=pyhd8ed1ab_1
altair=4.2.0=pypi_0
appnope=0.1.2=py39h2804cbe_2
argon2-cffi=21.3.0=pyhd8ed1ab_0
argon2-cffi-bindings=21.2.0=py39h5161555_1
astor=0.8.1=pypi_0
astunparse=1.6.3=pyhd8ed1ab_0
async_generator=1.10=py_0
attrs=21.4.0=pyhd8ed1ab_0
backcall=0.2.0=pyh9f0ad1d_0
backports=1.0=py_2
backports.functools_lru_cache=1.6.4=pyhd8ed1ab_0
base58=2.1.1=pypi_0
bayesian-optimization=1.2.0=pypi_0
bitfinex-tencars=0.0.3=pypi_0
bleach=4.1.0=pyhd8ed1ab_0
blinker=1.4=pypi_0
boto3=1.20.29=pyhd8ed1ab_0
botocore=1.23.29=pyhd8ed1ab_0
brotli=1.0.9=h3422bc3_6
brotli-bin=1.0.9=h3422bc3_6
brotlipy=0.7.0=py39h5161555_1003
bzip2=1.0.8=h3422bc3_4
c-ares=1.18.1=h3422bc3_0
ca-certificates=2021.10.8=h4653dfc_0
cached-property=1.5.2=hd8ed1ab_1
cached_property=1.5.2=pyha770c72_1
cachetools=4.2.4=pypi_0
certifi=2021.10.8=py39h2804cbe_1
cffi=1.15.0=py39h52b1de0_0
charset-normalizer=2.0.9=pyhd8ed1ab_0
click=8.0.3=py39h2804cbe_1
cloudpickle=2.0.0=pypi_0
colorama=0.4.4=pyh9f0ad1d_0
cryptography=36.0.1=py39hfb8cd70_0
cycler=0.11.0=pyhd8ed1ab_0
dataclasses=0.8=pyhc8e2a94_3
debugpy=1.5.1=py39hfb83b0d_0
decorator=5.1.0=pyhd8ed1ab_0
defusedxml=0.7.1=pyhd8ed1ab_0
entrypoints=0.3=pyhd8ed1ab_1003
flask=2.0.2=pyhd8ed1ab_0
flatbuffers=1.12=pypi_0
flit-core=3.6.0=pyhd8ed1ab_0
fonttools=4.28.5=py39h5161555_0
freetype=2.10.4=h17b34a0_1
gast=0.4.0=pyh9f0ad1d_0
gitdb=4.0.9=pypi_0
gitpython=3.1.26=pypi_0
google-auth=2.3.3=pypi_0
google-auth-oauthlib=0.4.6=pypi_0
google-pasta=0.2.0=pyh8c360ce_0
grpcio=1.34.1=py39h1eaaf2b_0
gym=0.21.0=pypi_0
h5py=3.1.0=nompi_py39h99babb8_100
hdf5=1.10.6=nompi_h0fc092c_1114
icu=69.1=hbdafb3b_0
idna=3.1=pyhd3deb0d_0
importlib-metadata=4.10.0=py39h2804cbe_0
importlib_resources=5.4.0=pyhd8ed1ab_0
ipykernel=6.6.1=py39h32adebf_0
ipython=7.31.0=py39h2804cbe_0
ipython_genutils=0.2.0=py_1
ipywidgets=7.6.5=pyhd8ed1ab_0
itsdangerous=2.0.1=pyhd8ed1ab_0
jbig=2.1=h3422bc3_2003
jedi=0.18.1=py39h2804cbe_0
jinja2=3.0.3=pyhd8ed1ab_0
jmespath=0.10.0=pyh9f0ad1d_0
joblib=1.1.0=pyhd8ed1ab_0
jpeg=9d=h27ca646_0
jsonschema=4.3.3=pyhd8ed1ab_0
jupyter=1.0.0=py39h2804cbe_7
jupyter_client=7.1.0=pyhd8ed1ab_0
jupyter_console=6.4.0=pyhd8ed1ab_0
jupyter_core=4.9.1=py39h2804cbe_1
jupyterlab_pygments=0.1.2=pyh9f0ad1d_0
jupyterlab_widgets=1.0.2=pyhd8ed1ab_0
kaggle=1.5.12=pypi_0
keras-nightly=2.5.0.dev2021032900=pypi_0
keras-preprocessing=1.1.2=pyhd8ed1ab_0
kiwisolver=1.3.2=py39h4d2d688_1
krb5=1.19.2=hd92b7a7_3
lcms2=2.12=had6a04f_0
lerc=3.0=hbdafb3b_0
libblas=3.9.0=12_osxarm64_openblas
libbrotlicommon=1.0.9=h3422bc3_6
libbrotlidec=1.0.9=h3422bc3_6
libbrotlienc=1.0.9=h3422bc3_6
libcblas=3.9.0=12_osxarm64_openblas
libcurl=7.80.0=h8fe1914_1
libcxx=12.0.1=h168391b_1
libdeflate=1.8=h3422bc3_0
libedit=3.1.20191231=hc8eb9b7_2
libev=4.33=h642e427_1
libffi=3.4.2=h3422bc3_5
libgfortran=5.0.0.dev0=11_0_1_hf114ba7_23
libgfortran5=11.0.1.dev0=hf114ba7_23
libiconv=1.16=h642e427_0
liblapack=3.9.0=12_osxarm64_openblas
libnghttp2=1.43.0=he4cd7f6_1
libopenblas=0.3.18=openmp_h5dd58f0_0
libpng=1.6.37=hf7e6567_2
libprotobuf=3.19.1=hccf11d3_0
libsodium=1.0.18=h27ca646_1
libssh2=1.10.0=hb80f160_2
libtiff=4.3.0=h74060c4_2
libwebp-base=1.2.1=h3422bc3_0
libxml2=2.9.12=hedbfbf4_1
libxslt=1.1.33=hecd09c7_3
libzlib=1.2.11=hee7b306_1013
llvm-openmp=12.0.1=hf3c4609_1
lxml=4.7.1=py39h3757d6e_0
lz4-c=1.9.3=hbdafb3b_1
markdown=3.3.6=pypi_0
markupsafe=2.0.1=py39h5161555_1
matplotlib=3.5.1=py39hdf13c20_0
matplotlib-base=3.5.1=py39h5aa4fe7_0
matplotlib-inline=0.1.3=pyhd8ed1ab_0
mistune=0.8.4=py39h5161555_1005
mplfinance=0.12.8b6=pypi_0
multitasking=0.0.10=pypi_0
munkres=1.1.4=pyh9f0ad1d_0
nbclient=0.5.9=pyhd8ed1ab_0
nbconvert=6.4.0=py39h2804cbe_0
nbformat=5.1.3=pyhd8ed1ab_0
ncurses=6.2=h9aa5885_4
nest-asyncio=1.5.4=pyhd8ed1ab_0
notebook=6.4.6=pyha770c72_0
numpy=1.22.0=pypi_0
oauthlib=3.1.1=pypi_0
olefile=0.46=pyh9f0ad1d_1
opencv-python=4.5.5.62=pypi_0
openjpeg=2.4.0=h062765e_1
openssl=1.1.1l=h3422bc3_0
opt_einsum=3.3.0=pyhd8ed1ab_1
packaging=21.3=pyhd8ed1ab_0
pandas=1.3.5=py39h7f752ed_0
pandas-datareader=0.10.0=pyh6c4a22f_0
pandocfilters=1.5.0=pyhd8ed1ab_0
parso=0.8.3=pyhd8ed1ab_0
pexpect=4.8.0=pyh9f0ad1d_2
pickleshare=0.7.5=py_1003
pillow=8.4.0=py39ha74c66e_0
pip=21.3.1=pyhd8ed1ab_0
pipdeptree=2.2.1=pypi_0
prometheus_client=0.12.0=pyhd8ed1ab_0
prompt-toolkit=3.0.24=pyha770c72_0
prompt_toolkit=3.0.24=hd8ed1ab_0
protobuf=3.19.1=py39hfb83b0d_1
ptyprocess=0.7.0=pyhd3deb0d_0
pyarrow=7.0.0=pypi_0
pyasn1=0.4.8=pypi_0
pyasn1-modules=0.2.8=pypi_0
pycparser=2.21=pyhd8ed1ab_0
pydeck=0.7.1=pypi_0
pygments=2.11.1=pyhd8ed1ab_0
pympler=1.0.1=pypi_0
pyopenssl=21.0.0=pyhd8ed1ab_0
pyparsing=3.0.6=pyhd8ed1ab_0
pyrsistent=0.18.0=py39h5161555_0
pysocks=1.7.1=py39h2804cbe_4
python=3.9.9=h70c1b39_0_cpython
python-dateutil=2.8.2=pyhd8ed1ab_0
python-slugify=5.0.2=pypi_0
python_abi=3.9=2_cp39
pytz=2021.3=pyhd8ed1ab_0
pytz-deprecation-shim=0.1.0.post0=pypi_0
pyyaml=6.0=py39h5161555_3
pyzmq=22.3.0=py39h02c6a76_1
readline=8.1=hedafd6a_0
requests=2.27.0=pyhd8ed1ab_0
requests-oauthlib=1.3.0=pypi_0
rsa=4.8=pypi_0
s3transfer=0.5.0=pyhd8ed1ab_0
scikit-learn=1.0.2=py39hef7049f_0
scipy=1.7.3=py39h5060c3b_0
seaborn=0.11.2=pypi_0
send2trash=1.8.0=pyhd8ed1ab_0
setuptools=60.2.0=py39h2804cbe_0
six=1.15.0=pyh9f0ad1d_0
smmap=5.0.0=pypi_0
sqlite=3.37.0=h72a2b83_0
streamlit=1.5.1=pypi_0
ta=0.8.0=pypi_0
tensorboard=2.7.0=pypi_0
tensorboard-data-server=0.6.1=pypi_0
tensorboard-plugin-wit=1.8.1=pypi_0
tensorboardx=2.4.1=pypi_0
tensorflow-deps=2.5.0=1
tensorflow-estimator=2.5.0=pypi_0
tensorflow-macos=2.5.0=pypi_0
tensorflow-metal=0.1.2=pypi_0
termcolor=1.1.0=py_2
terminado=0.12.1=py39h2804cbe_1
testpath=0.5.0=pyhd8ed1ab_0
text-unidecode=1.3=pypi_0
threadpoolctl=3.0.0=pyh8a188c0_0
tk=8.6.11=he1e0b03_1
toml=0.10.2=pypi_0
toolz=0.11.2=pypi_0
tornado=6.1=py39h5161555_2
tqdm=4.62.3=pyhd8ed1ab_0
traitlets=5.1.1=pyhd8ed1ab_0
typing_extensions=3.7.4.3=py_0
tzdata=2021.5=pypi_0
tzlocal=4.1=pypi_0
urllib3=1.26.7=pyhd8ed1ab_0
validators=0.18.2=pypi_0
wcwidth=0.2.5=pyh9f0ad1d_2
webencodings=0.5.1=py_1
werkzeug=2.0.1=pyhd8ed1ab_0
wheel=0.35.1=pyh9f0ad1d_0
widgetsnbextension=3.5.2=py39h2804cbe_1
wrapt=1.12.1=py39h5161555_3
xlsxwriter=3.0.2=pypi_0
xz=5.2.5=h642e427_1
yaml=0.2.5=h3422bc3_2
yfinance=0.1.70=pypi_0
zeromq=4.3.4=hbdafb3b_1
zipp=3.6.0=pyhd8ed1ab_0
zlib=1.2.11=hee7b306_1013
zstd=1.5.1=h861e0a7_0
```


These sub directories are collection of backtesting for different rule based bots. 
Quite messy structured inside the codebase as they are all trials of differetn cook-offs of rules.
just go into any directory RBTB# and run ```python main.py``` to run them. 

***they are not that vital for test and observe as the rules are made for backtesting only.***