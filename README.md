# Proyecto de grado

## Sincronizar los submodulos

git submodule update --init --recursive

NOTA: `--init` solo es necesario la primera vez para sincronizarlos.

## Configurar mail para los batch

Dentro de cada submodulo en la carpeta `batch` se encuentran los scripts para la ejecucion de los comandos en el cluster. En caso usar los batch y querer tener el mail configurado para todos los scripts se puede agregar la siguiente linea al archivo `~/.bashrc` cambiando por el mail correspondiente:

alias sbatch='sbatch --mail-user=cr.silper@gmail.com'

O modificar en cada uno de los archivos reemplazando `user@email` por el correspondiente.

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

* conda install pytorch torchvision cudatoolkit=10.0 -c pytorch

Instalar el resto de dependencias:

* pip install -r requirements.txt

### RC

Correr el siguiente comando para tener asignado un node en cluster:
* srun --pty bash -l

Instalar libbpg usando el script `bpg_install.sh` que se encuentra en la raíz (es necesario correrlo desde `home`):
* mv bpg_install.sh ~/bpg_install.sh
* mv SDL_x11sym.h ~/SDL_x11sym.h
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

* conda create --name lbb python=3.6.7
* conda activate lbb

* conda install pytorch torchvision cudatoolkit=10.0 -c pytorch
* pip install -r requirements.txt

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

---

## Algoritmos clásicos

### FLIF

Clonar este [repositorio](https://github.com/FLIF-hub/FLIF) y seguir las instrcciones de instalación en la plataforma correspondiente

Para correr una compresión sin perdida usar el siguiente comando:
* flif {input} {out}

### Webp

Descargar el paquete de instalación necesario de [aquí](https://storage.googleapis.com/downloads.webmproject.org/releases/webp/index.html) o descargar los fuentes, descomprimir y agregar el directorio `bin` al `PATH` del sistema.

Para correr una compresión sin perdida usar el siguiente comando:
* cwebp --lossles {input} -o {out}

### Batch sobre directorios

Para correr la compresion y calcular el bpd sobre un directorio o varios directorios de imagenes usar este [script](classics/encode.py). Para correr:

* python encode.py webp ~/Desktop/datasets_proyecto/mobile
