#module have same extension as like progrma ".py"
#it imports module from sys.path
#.pyc file is created when module is imported
# to install  navigate to pyhtoninstallation folder\script and use pip install "package name"

def square(x):
    return x*x

def cube(x):
    return x**3

def main():
    print ("This is ran from main console")

if __name__== "__main__":
    main()
