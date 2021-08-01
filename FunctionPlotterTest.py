import unittest
from main import MainWidget as mw


class MyTestCase(unittest.TestCase):
    def test_something(self):
        x = [-2, -1, 0, 1, 2]
        expected = [-4,-2,0,2,4]
        function = "2x"
        result=self.functionInput(x,function)
        self.assertEqual(expected,result)  # add assertion here













    def functionInput(self, x,function):
        function = function.replace("^", "**")
        function+="+0"
        temp = ""
        for char in function:
            if char == '*' or char == '+' or char == '-' or char == '/' :
                if("x" in temp):
                    replaceStr=temp
                    if(temp.find("x")!=0):
                        replaceStr=replaceStr.replace("x","*x")
                        function=function.replace(temp,replaceStr)
                temp=""
            else:
                temp += char
        #try:
            print(x)
            print(function)
            y = eval(function)
            print(y)
            return y
        #except:
         #   return "Invalid input eg: x^2 or 3x^3+2x^2"

if __name__ == '__main__':
    unittest.main()
