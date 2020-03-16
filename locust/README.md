# Locust

Install `python 3.7+` and `pip`.

```bash
yum install gcc openssl-devel bzip2-devel libffi-devel python-pip python3-psutil
cd /opt
wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
tar xzf Python-3.8.2.tgz
cd Python-3.8.2
./configure --enable-optimizations
make altinstall
rm Python-3.8.2.tgz

python3.8 -V

pip3 install -r requirements.txt
locust -f lsp_script.py
```

open a browser and browse to <http://127.0.0.1:8089>
