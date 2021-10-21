import os
import pyttsx3


# Reading the file, and generating a list
class FileReader(object):
    """
    docstring for FileReader:
    This class generates a list of Strings.
    The class FileReader takes a file name as an input.
    If the file exits, this will return a list of Strings using getText() function to the place
    from where it is being called.
    Otherwise, will show 'File Not Found!' and the program will be terminate.
    """

    def __init__(self, file_name):
        super(FileReader, self).__init__()
        self.file_name = file_name
        self.list = []
        self.reader()

    # 1st way to read the input file
    # def reader(self):
    #     try:
    #         file = open(self.filename, "r")
    #         self.list.append(file.read())
    #     except FileNotFoundError:
    #         print("File Not Found!")
    #         exit(0)

    # 2nd way to read the input file
    def reader(self):
        if os.path.isfile(self.file_name):
            file = open(self.file_name, "r")
            self.list.append(file.read())
        else:
            print("File Not Found!")
            exit(0)

    def getText(self):
        return self.list


# Performing Speech on the given list
class Speech(object):
    """
    docstring for Speech:
    This class can read (voice) a file and can generate an audio file as well.
    The class Speech takes the required rate and the words_list as input parameters.
    Depending upon our requirement/need, we can make the program to read the list, or could
    save the audio file of the speech.
    This class uses the pyttsx3 module, so make sure to install and import pyttsx3 module first.
    The audio file can be generated using the method generate().
    Note: The file name of the audio file will be Output+'Rate'.mp3  [Rate <- The rate you gave as input]
    """

    def __init__(self, rate, words_list):
        super(Speech, self).__init__()
        # self.engine = pyttsx3.init('sapi5')
        self.engine = pyttsx3.init()  # This will initialize the engine with the default driver
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)  # Male Voice
        # self.engine.setProperty('voice', self.voices[1].id)  # Female Voice
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate)
        self.current_rate = rate
        self.words_list = words_list

    # Not used in this program, but can be used later if needed
    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def speakFile(self):
        self.engine.say((str(self.words_list).replace("\\n", ", ")).replace("\\t", "  ").replace("i.e.", "that is "))
        self.engine.runAndWait()

    def generate(self):
        output_filename = "Output_" + str(self.current_rate) + ".mp3"
        self.engine.save_to_file(
            ((str(self.words_list).replace("\\n", ", ")).replace("\\t", "  ")).replace("i.e.", "that is "),
            output_filename)
        self.engine.runAndWait()


def getList():
    filename = input("Enter the filename: ")
    if ".txt" not in filename:  # Uncomment this if want to read only .txt files without any exception
        filename += ".txt"
    file = FileReader(filename)

    # Downloads Location: Downloads\THE STORY OF ALADDIN AND HIS MAGICAL LAMP.txt [Tried reading a story]
    # file = FileReader("Reader.txt")  # Opens and reads the Reader.txt file
    return file.getText()


def main(rate_option):
    if "both" in rate_option.lower():
        required_rate = [60, 80, 100, 120, int(rate_option[rate_option.index('h') + 2:])]

    elif rate_option.isdigit():
        required_rate = [int(rate_option)]

    elif "default" in rate_option.lower():
        required_rate = [60, 80, 100, 120]

    else:
        print("Unsupported input format!!!")
        exit(0)

    words_list = getList()

    # noinspection PyUnboundLocalVariable
    for rate in required_rate:
        Speech(rate, words_list).speakFile()  # Only reads the file
        # Speech(rate, words_list).generate()  # Only generates the audio files


if __name__ == "__main__":
    # Taking choice from the user
    choice = input("Want to generate audio at specific rate or default?" +
                   "\nEnter a <custom (int)> rate or write \'default\' for default playback rate" +
                   "\nor \'both <space another rate>\' for both default playback rate together with a custom rate: ")

    # * Good if want to embed this program in anywhere else->
    main(choice)

    """
    * Previous Version (Not good for embedding)->
    if "both" in choice.lower():
        required_rate = [60, 80, 100, 120, int(choice[choice.index('h') + 2:])]
        # print(required_rate)

    elif choice.isdigit():
        required_rate = [int(choice)]

    elif "default" in choice.lower():
        required_rate = [60, 80, 100, 120]

    else:
        print("Unsupported input format!!!")
        exit(0)

    # print(required_rate)
    words_list = getList()
    # print(words_list)

    # noinspection PyUnboundLocalVariable
    for rate in required_rate:
        # Speech(rate, words_list).speakFile()
        Speech(rate, words_list).generate()

    * Base frame used for entire feature->
    temp = Speech(150, words_list)
    temp.speak(str(words_list).replace("\\n", ",")) 
    Modified to -> temp.speak(((str(self.words_list).replace("\\n", ", ")).replace("\\t", "  "))
    temp.speakFile()
    temp.generate()

    * Sample Layout->
    sp60 = Speech(60)
    for word in word_list:
        print(word)
        sp60.speak(word)

    sp80 = Speech(80)
    for word in word_list:
        print(word)
        sp80.speak(word)
    """
