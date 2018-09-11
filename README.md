# PyTimer

A timer application for macOS, with stopwatch and split tracking functionality.

## Running PyTimer

The easiest way to use the application is to download the latest `.app` 
bundle from the [releases page](https://github.com/Cjreynol/PyTimer/releases).

If you want to run from source, then run the `__main__.py` script using 
either `python -m pytimer` or `python pytimer/__main__.py` to bring up the 
application window.

## Building the application from source

Creating the application bundle requires `py2app` to be installed and is 
currently only tested using Python 3.7 and py2app V0.17.

I would suggest creating a virtual environment (`python3 -m venv <env name>`) 
and then installing `py2app` with `pip install py2app`.  

To build from the source run `python app_setup.py py2app` from the project's 
root directory.
