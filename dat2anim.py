import pygame
import argparse
import os

#----- globals

VER = '1.0'
APPNAME = 'Dat2Anim'

# no edit
WD = os.path.dirname(os.path.realpath(__file__))
SPRDIR = os.path.join(WD, 'sprites')
ARGS = None
FRAMES = {
    'map': [],
    'frameunits': None,
    'tileset': {},
    'tilesize': None
}
SCREEN = None
SAVE_DIR = None

#----- args

def build_args():
    parser = argparse.ArgumentParser(
        description=f'''{APPNAME} - convert a dat file containing a frame map
                        into a graphical animation.'''
    )
    parser.add_argument('--fps', 
                        help='''Number of frames per second. 
                                (default = 1 fps)''', 
                        type=int, default=1)
    parser.add_argument('-s', action='store_true',
                            help='''Save the rendered frames in files. 
                            A directory will be created containing the rendered frames.''')
    parser.add_argument('--spr', 
                        help=f'''Define a path for sprites directory.
                                Each image on this dir may be a png formatted
                                as <id>.png. (e.g. "0.png") for id=0.
                                Make sure that all sprites that you'll use
                                has the same height and width.
                                (default = {SPRDIR})''', 
                        type=str, default=SPRDIR)
    parser.add_argument('file', 
                        help='''A DAT file containing the frames separated by an end line.
                        See the example "in.dat".''',
                        type=argparse.FileType('r'))
    return parser.parse_args()

ARGS = build_args()

#----- util

def create_save_dir():
    global SAVE_DIR
    import datetime
    SAVE_DIR = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    os.mkdir(f'fout-{SAVE_DIR}') 

#----- init

def parse_frames():
    global FRAMES
    print('Parsing frames...')
    frame = []
    for r in ARGS.file:        
        if r[0] in os.linesep:
            FRAMES['map'].append(frame)
            frame = []
        else:
            tiles = r.replace(os.linesep, '').split(',')
            for t in tiles:
                if not t in FRAMES['tileset']:
                    tile = pygame.image.load(
                                os.path.join(SPRDIR, f'{t}.png')
                           )
                    FRAMES['tileset'][t] = tile
            frame.append(tiles)
    FRAMES['frameunits'] = (len(FRAMES['map'][0][0]), 
                          len(FRAMES['map'][0]))
    FRAMES['tilesize'] = FRAMES['tileset'][
                            next(iter(FRAMES['tileset']))
                        ].get_size()

def setup():
    global SCREEN, SPRDIR
    SPRDIR = ARGS.spr
    parse_frames()
    SCREEN = Screen()
    if ARGS.s:
        create_save_dir()

#----- screen

class Screen():
    def __init__(self):
        size = (
            FRAMES['frameunits'][0] * FRAMES['tilesize'][0],
            FRAMES['frameunits'][1] * FRAMES['tilesize'][1]
        )
        self.fidx = 0
        print('Initializing screen...')
        pygame.display.set_mode(size)
        pygame.display.set_caption(f'{APPNAME} (v{VER})')
        self.__fix_tileset()
    def __fix_tileset(self):
        for k, v in FRAMES['tileset'].items():
            FRAMES[k] = v.convert_alpha()
    def __next_frame(self):
        if self.fidx < len(FRAMES['map']):
            f = FRAMES['map'][self.fidx]
            self.fidx += 1
            return f
        return None
    def update(self):
        frame = self.__next_frame()
        if frame:
            surf = pygame.display.get_surface()
            tw, th = FRAMES['tilesize']
            c, r = FRAMES['frameunits']
            for i in range(0, r):
                for j in range(0, c):
                    tile = FRAMES['tileset'][frame[i][j]]
                    surf.blit(tile, (j*tw, i*th))
            pygame.display.flip()
            if ARGS.s:
                pygame.image.save(surf, 
                        os.path.join(f'fout-{SAVE_DIR}', f'{self.fidx}.png'))

#----- main
def main():
    pygame.init()
    setup()
    clk = pygame.time.Clock()
    running = True
    print('Running...')
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                print('Stopping...')
                running = False
        SCREEN.update()
        clk.tick(ARGS.fps)
    pygame.quit()

if __name__ == '__main__':
    main()
