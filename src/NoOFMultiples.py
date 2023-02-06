class Answer:
    def __init__(self, n):
        self.n = n
        self.three = 3
        self.five = 5
        self.fifteen = 15

    def function(self):
        a = self.n // self.three
        b = self.n // self.five
        self.printer(a + b)

    def printer(self, s1):
        c = self.n // self.fifteen
        print(s1 - c)

def main():
    n = int(input())
    answer = Answer(n)
    answer.function()

if __name__ == '__main__':
    main()