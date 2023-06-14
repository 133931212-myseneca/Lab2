import sys

def print_arguments():
    script_name = sys.argv[0]
    print("Script name:", script_name)

    if len(sys.argv) > 1:
        arguments = ' '.join(sys.argv[1:])
        print("Script name and arguments:", script_name, arguments)

print_arguments()

def helloWorld():
	print(‘Hello World’)


helloWorld()
