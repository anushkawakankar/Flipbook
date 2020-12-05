# Flippr
##### Anushka Wakankar
---
A language created to help a user create a flipbook, using images chosen by them! This easy to understand and super easy to use language will create a flipbook for you in no time. 
A Flippr code can be written in a .flip file. After one passes a flip file with the right format to the python code, it will read, parse, and run the commands mentioned in the file to generate an output of your choosing. Right now, this code supports .gif and .avi outputs.
This language will be used exclusively to create flipbooks, hence its grammar is very specific to its usecase.

### Setup
Clone the repository using the command.
```sh
$ git clone https://github.com/anushkawakankar/Flipbook.git
```
Install the dependencies.
```sh
$ make install
```
### Running the code

Use the following command to run the code
```sh
$ python3 code.py {path to .flip file} {output video name}
```


### Rules of the Language (Syntax)
* A line describing a consecutive set of frames should be of the following format
`{start_frame} {end_frame} {path to image}` or
`{start_frame} {end_frame} {x_index} {y_index} {filename}`
* `fps` and `loop` are keywords which can be mentioned anywhere in the code(not in the middle of a frame definition). `fps` lets the user set the framerate of the generated video. `loop` lets the user determine how many times a set of frames will be looped. This parameter matters only while generating a .avi file.
* There is sufficient error handling for the following cases- 
    * When the code is not stored in a file with a .flip extension.
    * When the output format is not .gif or .avi.
    * When the filename specified does not exist.
    * Syntax errors in the .flip code.
    * Images mentioned in the .flip code do not exist.
