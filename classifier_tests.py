import os
from chatapi import ChatApi
from classifier import Classifier

class ClassifierTester:
    def __init__(self, classifier):
        self.__classifier = classifier
        self.__numrun=0
        self.__fail=[]
    def test(self, input, expected):
        output = self.__classifier.classify(input)
        self.__numrun += 1
        if output != expected:
             self.__fail.append({input, output})
    def summarize(self):
        return "{}/{}".format(self.__numrun-len(self.__fail), self.__numrun)

apikey = os.getenv("OPENAI_API_KEY")
api = ChatApi(apikey)
classifierColor = Classifier(api, "respond with a single word color", ["red", "orange", "blue", "yellow", "green"])
tester = ClassifierTester(classifierColor)
tester.test("the sky", "blue")
tester.test("grass", "green")
tester.test("fire", "orange")
tester.test("berries", "red")
print(tester.summarize())

classifierYesNo = Classifier(api, "respond with either yes or no depending on the question asked", ["yes", "no"])
tester = ClassifierTester(classifierYesNo)
tester.test("Is the sky blue?", "yes")
tester.test("Do dogs have fur?", "yes")
tester.test("Is the Earth flat?", "no")
tester.test("Are tomatoes a fruit?", "yes")
tester.test("Can humans breathe underwater?", "no")
tester.test("What time is it?", None)
tester.test("How many sides does a square have?", None)
tester.test("Does a square have four sides?", "yes")
tester.test("what is the capital of spain?", None)
print(tester.summarize())