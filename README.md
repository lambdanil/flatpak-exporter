# Flatpak exporter

Flatpak exporter is a small utility, designed to simplify using flatpaks from the command line.

## Usage

Simply run ``main.py`` with ``python3 main.py``, it's automatically going to create a ``bin`` directory inside the current directory  
Next add the executable permission to these exported files ``sudo chmod +x ./bin/*``  
Now add files from ``./bin`` somewhere into your ``$PATH`` (for example if adding into ``~/.local/bin/``: ``cp ./bin/* ~/.local/bin/``)
