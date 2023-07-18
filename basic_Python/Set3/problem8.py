# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"


def createFirstFile() :
    file = open("input.txt", "w");
    file.write("Hello world");
    file.close();
    createSecondFile();
    
def createSecondFile():
    file = open("input.txt", "r");
    wordArr = file.read().split(" ");
    file.close();
    
    count = len(wordArr);
    
    outputFile = open("output.txt", "w");
    
    outputFile.write("Number of words: " + str(count));
    
    outputFile.close();
    outputFileReader = open("output.txt", "r");
    print(outputFileReader.read());
    outputFileReader.close();
    
    
    
createFirstFile();