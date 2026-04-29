#!/usr/bin/python3

import glob
import os
import subprocess
import sys

sys.dont_write_bytecode = True
from flaky_tests_list import flaky_test_dirs

cwd = os.getcwd()

overall_test_rc = 0
failed_tests = []

# find all dirs that have unit tests
for i in glob.glob('ansible_collections/**/tests/unit', recursive=True):

    # base path to run ansible-test is two levels up
    testdir = os.path.normpath(
        os.path.join(i, '..', '..')
    )

    # skip any tests that are flagged as flaky
    if testdir in flaky_test_dirs:
        print("Skipping", testdir)
        continue

    os.chdir(testdir)

    print ("\n\n", flush=True)
    print ("############################################################", flush=True)
    print ("############################################################", flush=True)
    print ("#### Running tests in", testdir, flush=True)
    print ("############################################################", flush=True)
    print ("############################################################", flush=True)

    rc = subprocess.run([
        '/usr/bin/ansible-test',
        'units',
        '--python-interpreter',
        '/usr/bin/python3',
        '--local'
    ])


    if rc.returncode != 0:
        failed_tests.append(i)
        overall_test_rc = rc.returncode

    os.chdir(cwd)


if overall_test_rc != 0:
    print ("############################################################", flush=True)
    print ("############################################################", flush=True)
    print ("#### failed tests are:", flush=True)
    for i in failed_tests:
        print ("####", i, flush=True)
    print ("############################################################", flush=True)
    print ("############################################################", flush=True)

exit(overall_test_rc)
