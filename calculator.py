class Calculator(object):
    def evaluate(self, string):
        print string
        my_num = str(float(eval(string, {'__builtins__': None}))).split('.')
        return float('.'.join([my_num[0],my_num[1][:3]]))



a = Calculator()
print a.evaluate("1 * 2 * 3")

