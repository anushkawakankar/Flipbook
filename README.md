# Flipbook

### Link to demo
https://drive.google.com/drive/folders/1t61DQ1L9Kv1QCS94yOvZDi3QdoSQn9nN?usp=sharing

### Files
.
├── compiler.py
├── main.py
├── requirements.txt
├── shark.flip
└── utils.py

- `compiler.py: module contaning Lexer and Parser`
- `utils.py: utility functions`
- `requirements.txt: python depedencies`
- `shark.flip: sample flip file`
- `main.py: entrypoint`

### Setup
Install dependencies using pip
```bash
pip install requirements.txt
```

### Running
```bash
python main.py <flip_file> <output_file>
```

### Syntax 
* The language has the following commands 
    * add_frames - to mention the number of frames an image should be repeated
    * set_fps - to set the fps of the output video/gif
    * set_loop - to set the number of times the video loops (only for avi)
* the format is to add an image is `add_frames x image_name`
* the format to set fps and loops is `set_fps = x` and `set_loop = y`
