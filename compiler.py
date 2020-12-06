from rply import LexerGenerator
from rply import ParserGenerator

from utils import *

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def get(self):

        self.lexer.add('ADD_FRAMES', r'add_frames')
        self.lexer.add('SET_FPS', r'set_fps')
        self.lexer.add('SET_LOOP', r'set_loop')
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('IMAGE', r'[^\s]+(\.(?i)(jpg|png|gif|bmp|jpeg))')
        
        self.lexer.ignore('\s+')

        return self.lexer.build()


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            ['ADD_FRAMES', 'NUMBER', 'IMAGE', 'SET_FPS', 'SET_LOOP']
        )

    def parse(self):
        @self.pg.production('expr : ADD_FRAMES NUMBER IMAGE')
        def expression(p):
            no_frames = int(p[1].value)
            image = p[2].value
            return {'frames': [image]*no_frames}


        @self.pg.production('expr : SET_FPS NUMBER')
        def expression(p):
            fps = int(p[1].value)
            return {'fps': fps}
        
        @self.pg.production('expr : SET_LOOP NUMBER')
        def expression(p):
            loop = int(p[1].value)
            return {'loop': loop}

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get(self):
        return self.pg.build()