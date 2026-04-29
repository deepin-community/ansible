#!/usr/bin/python3

import os
import subprocess
import sys

sys.dont_write_bytecode = True
from flaky_tests_list import flaky_test_dirs

cwd = os.getcwd()

overall_test_rc = 0
succeeded_tests = []
failed_tests = []

for i in flaky_test_dirs:

    os.chdir(i)

    print ("\n\n", flush=True)
    print ("############################################################", flush=True)
    print ("############################################################", flush=True)
    print ("#### Running FLAKY tests in", i, flush=True)
    print ("############################################################", flush=True)
    print ("############################################################", flush=True)

    rc = subprocess.run([
        '/usr/bin/ansible-test',
        'units',
        '--python-interpreter',
        '/usr/bin/python3',
        '--local'
    ])

    # don't fail on failed test, continue instead
    print ("## return code is", rc.returncode)

    if rc.returncode == 0:
        succeeded_tests.append(i)
    else:
        failed_tests.append(i)
        overall_test_rc = rc.returncode

    os.chdir(cwd)

print ("############################################################", flush=True)
print ("############################################################", flush=True)
print ("#### failed tests are:", flush=True)
for i in failed_tests:
    print ("####", i, flush=True)
if len(succeeded_tests) > 0:
    print ("#### succeeded tests are:", flush=True)
    for i in succeeded_tests:
        print ("####", i, flush=True)
    print ("#### consider removing them from the flaky tests list.", flush=True)
print ("############################################################", flush=True)
print ("############################################################", flush=True)


exit(overall_test_rc)
