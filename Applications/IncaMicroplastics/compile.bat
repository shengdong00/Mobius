@echo off

REM g++ -O2 -I../../Calibration/MCMC/mcmc/include/ -I../../Calibration/MCMC/mcmc/src/ incased.cpp -m64 -std=c++11 -fopenmp -o incaviewincased.exe ../../sqlite3/sqlite3.o -L../../Calibration/MCMC/libs/ -llapack_win64_MT -lblas_win64_MT -DINCAVIEW_INCLUDE_OPTIMIZER=1 -DINCAVIEW_INCLUDE_GLUE=1 -DINCAVIEW_INCLUDE_MCMC=1
REM g++ incamicroplastics.cpp -std=c++11 -O2 -Werror=return-type -o incamicroplastics.exe ../../sqlite3/sqlite3.o -fmax-errors=5

@REM g++ -c -m64 -std=c++11 -O2 incamicroplastics_dll.cpp -fexceptions -fmax-errors=5
g++ -c -m64 -std=c++14 -O2 incamicroplastics_dll.cpp -fexceptions -fmax-errors=5
g++ -o incamicroplastics.dll -static -static-libgcc -static-libstdc++ -s -shared incamicroplastics_dll.o -Wl,--subsystem,windows -luuid -lole32 -loleaut32