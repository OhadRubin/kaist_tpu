sudo apt-get install -y -qq software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get install -y -qq python3.11-full python3.11-dev

python3.11 -m venv ~/venv

. ~/venv/bin/activate

pip install -U pip
pip install -U wheel
pip install -U "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
printf ". ~/venv/bin/activate" >> ~/.bashrc
