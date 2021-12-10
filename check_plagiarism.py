 # coding: utf-8

import mosspy
import sys, getopt
import glob

userId =518584132

m = mosspy.Moss(userId, 'python')
m.setCommentString("Moss is working")

def get_report(directory):
    files = glob.glob(directory + '/*.py')

    for file in files:
        m.addFile(file)

    url = m.send(lambda file_path, display_name: print('*', end="", flush=True))

    print('Report is saved under ./report/report.html')
    print(url)

    m.saveWebPage(url, './report/report.html')

def main(argv):
    directoryToTest = ""

    try:
        opts, args = getopt.getopt(argv, 'd:u')
    except getopt.GetoptError:
        print('python3 check_plagiarism -d <directory_to_check>')

    for opt, arg in opts:
        if opt == '-d':
            print(arg)
            get_report(arg)

if __name__ == "__main__":
   main(sys.argv[1:])
