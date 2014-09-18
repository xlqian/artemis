import json
import logging
import os
import time
import psutil


class ProfilingPoint:
    def __init__(self, pids):
        self.time = time.clock()

        self.memory_by_instance = {}
        if not pids:
            logging.getLogger(__name__).info("no krakens loaded yet")
            return
        for name, pid in pids.iteritems():
            self.memory_by_instance[name] = psutil.Process(pid).memory_info()


class FixtureMonitor:
    def __init__(self, fixture):
        self.name = fixture.__name__
        self.start_time = time.clock()
        self.after_setup = None
        self.end = None
        self.tests = []

        self.kraken_pids = None


def default_json_format(obj):
    """call to_dict if exist (if we want to customize), else __dict__"""
    try:
        return obj.to_dict()
    except AttributeError:
        return obj.__dict__


class PerformanceMonitor:
    """
    Performance monitor for artemis.

    Utility class used to log memory usage and excecution times of the tests

    for the moment we only log key moment, but we could also easily log every n miliseconds during tests

    for the moment it cannot be run in parallel
    """

    def __init__(self, logfile):
        self.logfile = logfile  # output file
        #remove the log file if exists
        os.remove(logfile) if os.path.exists(logfile) else None
        self.fixtures = []

    def start_fixture(self, fixture):
        fix = FixtureMonitor(fixture)

        self.fixtures.append(fix)

    def end_fixture(self, fixture):
        last_fixture_prof = self.fixtures[-1]
        last_fixture_prof.end = ProfilingPoint(fixture.kraken_pids)
        self.write_file()

    def end_fixture_init(self, fixture):
        last_fixture_prof = self.fixtures[-1]
        last_fixture_prof.after_setup = ProfilingPoint(fixture.kraken_pids)

    def start_test(self, test):
        pass

    def end_test(self, test):
        pass

    def write_file(self):
        output = open(self.logfile, 'a')
        output.write("--test")
        output.write(json.dumps(self.fixtures, default=default_json_format, sort_keys=True))

        output.close()