@echo off
REM Script para generar el parser ANTLR en Python3

REM Cambia esta ruta si mueves el archivo .jar
set ANTLR_JAR="C:\Users\Confi\Desktop\Universidad\Ingeniería en Sistemas\Quinto Semestre\Compiladores Lab\PF2\Proyecto-2-Compiladores\antlr-4.13.2-complete.jar"

REM Navega a la carpeta donde está tu archivo MiLenguaje.g4
cd /d "C:\Users\Confi\Desktop\Universidad\Ingeniería en Sistemas\Quinto Semestre\Compiladores Lab\PF2\Proyecto-2-Compiladores\Grammar"

echo Generando archivos ANTLR en Python3...
java -jar %ANTLR_JAR% -Dlanguage=Python3 MiLenguaje.g4

echo ----------------------------------------
echo Proceso completado. Verifica que se generaron los archivos .py
pause
