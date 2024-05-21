# Dat2Anim

This is a DAT file converter for animations. The DAT file can contain frame maps, with all frames having the same dimensions. Each tile in a frame can be mapped to a sprite from a sprite set (sprites directory). You can customize your own sprite set, the number of frames, and the frame size.

## How to use?

This app was developed using python 3.12.3. After the python installation, it is recomended that you create an execution virtual environment for the libraries used by this project. Use virtualenv for this. Install virtualenv package using pip an then create a virtual environment inside the Dat2Anim repository directory. With an access to a terminal just type:

```bash
> pip install virtualenv     # virtualenv installation
> virtualenv .venv           # virtual environment creation
#------ Alternatively
> pip3 install virtualenv    # use pip3 when python2 and python3 are both available in the system
> python3 -m venv .venv      # virtual environment creation
```

After the first execution if you want to run the game again just repeat steps 1 and 3.

1. Activate the virtual environment

    ```bash
    # On windows
    > .\.venv\Scripts\activate

    # On GNU/Linux or other unix-like systems
    $ source ./.venv/bin/activate
    ```
    
    * Notice that by activating the virtual environment something like `(.venv)` appears at the beginning of the command line on terminal. This indicates that the virtual environment is activated. To deactivate, type `deactivate`.

2. If this is your first time running Dat2Anim in this virtual environment, then you should install the dependencies:

    ```bash
    > pip install -r requirements.txt
    #------ Alternatively
    > pip3 install -r requirements.txt      # use pip3 when python2 and python3 are both available in the system
    ```

3. Inside the `src` directory execute Dat2Anim:

    ```bash
    > python dat2anim.py
    #------ Alternatively
    > python3 dat2anim.py                       # use python3 when python2 and python3 are both available in the system
    ```

## Usage

By typing the line below:

```bash
python dat2anim.py -h
```

You'll see this:

```bash
pygame-ce 2.4.1 (SDL 2.28.5, Python 3.12.3)
usage: dat2anim.py [-h] [--fps FPS] [-s] [--spr SPR] file

Dat2Anim - convert a dat file containing a frame map into a graphical animation.

positional arguments:
  file        A DAT file containing the frames separated by an end line. See the example "in.dat".

options:
  -h, --help  show this help message and exit
  --fps FPS   Number of frames per second. (default = 1 fps)
  -s          Save the rendered frames in files. A directory will be created containing the rendered frames.
  --spr SPR   Define a path for sprites directory. Each image on this dir may be a png formatted as <id>.png. (e.g. "0.png") for id=0. Make sure
              that all sprites that you'll use has the same height and width. (default = /home/vinicius/Pessoal/dat2anim/sprites)
```

### Running the "in.dat" example:

You can run it by passing the filepath as an argument:

```bash
python dat2anim.py in.dat

# The "in.dat" frames will be printed 1 per second (default FPS).
```

<img src="./screenshot/example.png">

An example with all parameters in use:

```bash
python dat2anim.py --fps 4 --spr ./path/to/sprites2 -s in.dat

# The "in.dat" frames will be printed 4 per second (default FPS).
# The spriteset will be loaded from "./path/to/sprites2"
# The frames will be saved in a directory as png images locally
```
