__copyright__ = "Copyright 2016-2020, Netflix, Inc."
__license__ = "BSD+Patent"

"""
Run embedded doctests
"""

import doctest

from vmaf.tools import misc
# from vmaf.tools import stats
from vmaf.core import quality_runner

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(misc))
    # tests.addTests(doctest.DocTestSuite(stats)) # commented out because not numerically exact
    tests.addTests(doctest.DocTestSuite(quality_runner))
    return tests
