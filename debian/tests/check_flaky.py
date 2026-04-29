#!/usr/bin/python3

# check if the list of flaky tests is actually valid
# Must be run from base of git dir

import os
import subprocess
import sys

sys.dont_write_bytecode = True
from flaky_tests_list import flaky_test_dirs

rc = 0

for i in flaky_test_dirs:

    testdir = os.path.join(i, 'tests', 'unit')

    if not os.path.isdir(testdir):
        print(testdir, 'does not exist. Consider removing it from flaky_test_dirs.py')
        rc=1

exit(rc)
