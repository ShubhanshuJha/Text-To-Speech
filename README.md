#**Text To Speech Program**
***
`This TTSP.py program is build on the Text to Speech library
"pyttsx3" which is a text-to-speech conversion library in Python.
Unlike other libraries, it works offline, and is compatible with
both Python 2 and 3.`
***

To install the ``pyttsx3`` library:

``pip install pyttsx3``
***

### About `TTSP.py`
This program can speak/generate the audio/audio file based on the
voice rate given by the user.
By default, it produces all of [60, 80, 100, 120] voice rates output.
The user can produce only a single output based on a single voice rate.
***

* Voice Rate Input Options:

    * `default`
    * `x`
    * `both x`
    
    *Here `x` can be any integer value representing the custom voice rate,
      e.g. 10, 50, 120, ..., etc.*
  
***

* Input File:
  
    *If present in the same directory*
    * `FileName.txt`
      
    *If present in the other directory*
    * `Path of file\FileName.txt`
    
***

* Output Filename:
  
    *Let the voice rate be `R` then, the generated audio output file will be*:
    * `OutputR.mp3`
    * **
    The audio file will be saved where you've saved this program.
  
***

#### Note:
If you want to automate or embed this program somewhere else, make sure to
remove all the unnecessary print statements from the code, and instead of
taking the inputs in the functions, provide the value as the parameter to
that specific function, wherever there's user input part.
***