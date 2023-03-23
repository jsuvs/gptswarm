from chatgpt import ChatGpt

#A classifier acts like a natural language to enum converter
#It classifies a natural language input into one of a range of pre-defined output classes passed in on construction
#It does this based on a natural language instruction passed in on construction
#If an input cannot not be classified then None is returned
#The classifier guarantees that only the pre-defined outputs or None is returned 
#For example a classifier could be instructed to answer yes/no questions with outputs range defined as "yes" or "no"
class Classifier:
    def __init__(self, chatapi, instructions, outputs, logger=None):
        self.__bot = ChatGpt(chatapi)
        self.__bot.addSystemMessage(instructions)
        self.__outputs = outputs

    def classify(self, input):
        nls_output = self.__bot.send(input)
        output = self.to_output(nls_output)
        return output
    
    def to_output(self, nls_output):
        nls_output = nls_output.lower()
        nls_output = nls_output.replace('.', '')
        #todo this simple matching can easily create false positives
        for output in self.__outputs:
            if output in nls_output:
                return output
        return None