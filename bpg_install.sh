# Crear carpeta y arrancar un trabajo rápido
mkdir libs
cd libs

# CMake
wget https://github.com/Kitware/CMake/releases/download/v3.20.0-rc3/cmake-3.20.0-rc3.tar.gz
tar xvf cmake-3.20.0-rc3.tar.gz
cd cmake-3.20.0-rc3
./bootstrap --prefix=`pwd`/install
make -j20 install

cd ..
export PATH=$PATH:~/libs/cmake-3.20.0-rc3/install/bin/

# BPG dependencies

## SDL
wget http://libsdl.org/release/SDL-1.2.15.tar.gz
tar xvf SDL-1.2.15.tar.gz
wget https://www.libsdl.org/projects/SDL_image/release/SDL_image-1.2.12.tar.gz
tar xvf SDL_image-1.2.12.tar.gz

cd SDL-1.2.15
cp ~/SDL_x11sym.h src/video/x11/SDL_x11sym.h
CFLAGS=-DSDL_VIDEO_DRIVER_X11_CONST_PARAM_XDATA32 ./configure --prefix=`pwd`/install
make -j20 install

cd ../SDL_image-1.2.12
./configure --prefix=`pwd`/../SDL-1.2.15/install
make -j20 install

cd ..
export PATH=$PATH:~/libs/SDL-1.2.15/install/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/libs/SDL-1.2.15/install/lib/
export LIBRARY_PATH=$LD_LIBRARY_PATH
export CPATH=$CPATH:~/libs/SDL-1.2.15/install/include

## YASM
wget http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz
tar xvf yasm-1.3.0.tar.gz
cd yasm-1.3.0
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=../install ..
make -j20 install

cd ../../
export PATH=$PATH:~/libs/yasm-1.3.0/install/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/libs/yasm-1.3.0/install/lib/
export LIBRARY_PATH=$LD_LIBRARY_PATH
export CPATH=$CPATH:~/libs/yasm-1.3.0/install/include

# BPG
wget https://bellard.org/bpg/libbpg-0.9.8.tar.gz
tar xvf libbpg-0.9.8.tar.gz
cd libbpg-0.9.8
mkdir bin
make -j20 install prefix=`pwd`

cd ..
export PATH=$PATH:~/libs/libbpg-0.9.8/bin

# Limpiar los archivos descargados
rm *tar.gz

# Copiar todas las configuraciones de PATH y las otras pariables al final del .bashrc para tener todo configurado en futuras sesiones
cat <<EOT >> ~/.bashrc

## CMake
export PATH=\$PATH:~/libs/cmake-3.20.0-rc3/install/bin/

## SDL
export PATH=\$PATH:~/libs/SDL-1.2.15/install/bin
export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:~/libs/SDL-1.2.15/install/lib/
export LIBRARY_PATH=\$LD_LIBRARY_PATH
export CPATH=\$CPATH:~/libs/SDL-1.2.15/install/include

## YASM
export PATH=\$PATH:~/libs/yasm-1.3.0/install/bin
export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:~/libs/yasm-1.3.0/install/lib/
export LIBRARY_PATH=\$LD_LIBRARY_PATH
export CPATH=\$CPATH:~/libs/yasm-1.3.0/install/include

## BPG
export PATH=\$PATH:~/libs/libbpg-0.9.8/bin

EOT

