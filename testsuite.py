# coding: utf-8

import py_compile
import unittest
import shutil
import os
import glob
import time
import importlib
import pathlib
import sys
import getopt


#from asg0unittest import TestAssignment0
from define_unit_test import assignment_test

class TestResult:
    def __init__(self, file, errors, failures):
        p = pathlib.Path(file)
        self.file = p.stem
        self.errors = str(errors)
        self.failures = str(failures)

def PerformTest(filename):
    try:
        suite = unittest.TestSuite()
        result = unittest.TestResult()
        suite.addTest(assignment_test.get_unit_test())
        runner = unittest.TextTestRunner()
        r = runner.run(suite)
        return(TestResult(filename, len(r.failures), len(r.errors)))
    except:
        print("error")



def CheckFile(filename):
    #dst = "std1.py"
    #shutil.copyfile(filename, dst)
    testResult = PerformTest(filename)
    return(testResult)

def RunTest(inputfile, resultfile):
    #copy file
    #CopyFile(inputfile)
    # perform test
    try:
        #py_compile.compile(inputfile, doraise=True)
        r = CheckFile(inputfile) # copy and run test
        if r.errors == '0' and r.failures == '0':
            towrite = str(r.file + "\tSuccess\n")
        else :
            towrite = str(r.file+", \tErrors: "+r.errors+",\tFailures: "+r.failures+"\n")
    except py_compile.PyCompileError:
        towrite = r.file + ",Compile Error,Compile Error\n"
    except:
        towrite = r.file + ",Error,Error\n"

    # store result
    f = open(resultfile,"a+")
    f.writelines(towrite)
    f.close()

def RaiseErrorAndExit():
    print('testsuite.py -i <inputfile> -r <resultfile>')
    sys.exit(2)


def main(argv):
    if len(argv)==0:
        RaiseErrorAndExit()

    try:
        opts, args = getopt.getopt(argv,"hi:r:")
    except getopt.GetoptError:
        RaiseErrorAndExit()

    inputfile = ''
    outputfile = ''
    resultfile = 'results.txt'
    for opt, arg in opts:
        if opt == '-h':
            print('testsuite.py -i <inputfile> -r <resultfile>')
            sys.exit()
        elif opt in ("-i"):
            inputfile = os.path.join(os.getcwd(), pathlib.Path(arg))
        elif opt in ("-o", "--ofile"):
            outputfile = pathlib.Path(arg)
        elif opt in ("-r"):
            resultfile = pathlib.Path(arg)

    RunTest(inputfile, resultfile)


if __name__ == "__main__":
   main(sys.argv[1:])

