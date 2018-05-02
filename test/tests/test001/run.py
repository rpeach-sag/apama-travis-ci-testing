# Sample PySys testcase
# Copyright (c) 2015-2016 Software AG, Darmstadt, Germany and/or Software AG USA Inc., Reston, VA, USA, and/or its subsidiaries and/or its affiliates and/or their licensors. 
# Use, reproduction, transfer, publication or disclosure is prohibited except as specifically provided for in your License Agreement with Software AG 

from pysys.constants import *
from pysys.basetest import BaseTest
from apama.correlator import CorrelatorHelper

class PySysTest(BaseTest):

	def execute(self):
		# create the correlator helper, start the correlator and attach an 
		# engine_receive process listening to a test channel. The helper will 
		# automatically get an available port that will be used for all 
		# operations against it
		correlator = CorrelatorHelper(self, name='testcorrelator')
		correlator.start(logfile='testcorrelator.log', config=PROJECT.TEST_SUBJECT_DIR+'/initialization.yaml')
		receiveProcess = correlator.receive(filename='receive.evt', channels=['output'], logChannels=True)
		correlator.applicationEventLogging(enable=True)
		
		# send in the events contained in the test.evt file (directory defaults 
		# to the testcase input)
		correlator.send(filenames=['test.evt'])
			
		# wait for all events to be processed
		correlator.flush()
		
		# wait until the receiver writes the expected events to disk
		self.waitForSignal('receive.evt', expr="Msg", condition="==1")
		
	def validate(self):
		# look for log statements in the correlator log file
		self.assertGrep('testcorrelator.log', expr=' (ERROR|FATAL) ', contains=False)
	
		# check the received events against the reference
		self.assertDiff('receive.evt', 'ref_receive.evt')
		