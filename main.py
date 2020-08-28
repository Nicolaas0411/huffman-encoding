from nameko.rpc import rpc
import huffman
import collections


class Assessment:
    name = "engineering_assessment"
    encodedStringDictionary = {}

    def encodeString(self, string):
        code = ""
        for i in huffman.codebook(collections.Counter(string).items()).values():
            code += str(i)
        return code

    @rpc
    def squareOddNumbers(self, listOfNumbers):
        even_sq, odd_sq = [], []
        for i in listOfNumbers:
            (even_sq if i % 2 == 0 else odd_sq).append(i*i)
        return odd_sq

    @rpc
    def createEncodedDictionary(self, listOfStrings):
        encodedStrings = []
        for string in listOfStrings:
            encodedStrings.append(self.encodeString(string))
        self.encodedStringDictionary.update(
            dict(zip(listOfStrings, encodedStrings)))
        return self.encodedStringDictionary

    @rpc
    def decode(self, encodedString):
        for key, value in self.encodedStringDictionary.items():
            if value == encodedString:
                return key
        return 'Encoding does not exist in dictionary!'
