# Proyecto de grado

## Sincronizar los submodulos

git submodule update --init --recursive

NOTA: `--init` solo es necesario la primera vez para sincronizarlos.

---
## Instalación

### Hilloc

Crear entorno virtual con la version de python necesaria y activarlo, en caso de no usar gpu sacar el `-gpu` de tensorflow:

* conda create --name hilloc python=3.7.9 tensorflow-gpu=1.13.1
* conda activate hilloc

Instalar el resto de dependencias:

* pip install -r requirements.txt

### IDF

Crear entorno virtual con la version de python necesaria y activarlo:

* conda create --name idf python=3.8
* conda activate idf

Instalar pytorch y cudatoolkit (en caso de usar gpu):

* conda install pytorch torchvision cudatoolkit=10.0 -c pytorch\

Instalar el resto de dependencias:

* pip install -r requirements.txt

### RC

Correr el siguiente comando para tener asignado un node en cluster:
* srun --pty bash -l

Instalar libbpg usando el script `bpg_install.sh` que se encuentra en la raíz (es necesario correrlo desde `home`):
* mv bpg_install.sh ~/bpg_install.sh
* cd ~/
* sh bpg_install.sh

Para probar que libbpg se instaló correctamente usar el script `test_bpg_available.sh` que se encuentra en `rc/RC-PyTorch/src`:
* bash test_bpg_available.sh

Crear entorno virtual con la version de python necesaria y activarlo:
* conda create --name rc python==3.7 pip -y
* conda activate rc

Instalar requerimientos, `requirements.txt` se encuentra en `rc/RC-PyTorch/src`:

* conda install pytorch==1.1.0 torchvision cudatoolkit==10.0.130 -c pytorch
* pip install -r requirements.txt


### LBB

#### Instalación

* conda create --name lbb 3.6.7
* conda activate lbb

* conda install pytorch torchvision cudatoolkit=10.0 -c pytorch
* pip install tqdm

* Build de la libreria C++ que esta en el repositorio (se necesita un compilador con soporte OpenMP):

```sh
cd compression/ans
mkdir build
cd build
cmake ..
make -j4
```

#### Correr

Para correr es necesario definir el PYTHON_PATH para que tome la libreria compilada y las carpetas del repositorio, por ejemplo parado en la carpeta `lbb/localbitsback`:

* PYTHONPATH=./:compression/ans/build/ python scripts/run_compression.py
