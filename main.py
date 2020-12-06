import compiler
import utils

import os
import sys

if __name__ == "__main__":
    
    infile = sys.argv[1]
    outfile = 'output.gif'

    if "flip" != infile.split('.')[-1]:
        print("Error: File must be of .flip format")
        exit()

    with open(infile) as f:
        lines = f.read().split('\n')
    
    tasks = []
    for line in lines:
        if line == "": continue
        
        print(f"Parsing: {line}")
        lexer = compiler.Lexer().get()
        pg = compiler.Parser()
        pg.parse()
        parser = pg.get()

        tasks.append(parser.parse(lexer.lex(line)))

    # Default values
    FRAMES = []
    FPS = 15
    LOOP = 1
    output_path = "flipbook.pdf"
    

    for task in tasks:
        if 'fps' in task: FPS = task['fps']
        if 'loop' in task: LOOP = task['loop']
        if 'frames' in task: FRAMES += task['frames']

    utils.generate_gif(FPS, LOOP, FRAMES, outfile)
    print("DONE")