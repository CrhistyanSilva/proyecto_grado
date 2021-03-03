# Proyecto de grado

## Sincronizar los submodulos

git submodule update --init

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
* conda activate hilloc

Instalar pytorch y cudatoolkit (en caso de usar gpu):

* conda install pytorch torchvision cudatoolkit=10.0 -c pytorch

### RC

### LBB

