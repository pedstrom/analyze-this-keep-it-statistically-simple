#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line sample for the Google Prediction API

Command-line application that trains on your input data. This sample does
the same thing as the Hello Prediction! example. You might want to run
the setup.sh script to load the sample data to Google Storage.

Usage:
  $ python prediction.py "bucket/object" "model_id" "project_id"

You can also get help on all the command-line flags the program understands
by running:

  $ python prediction.py --help

To get detailed log output run:

  $ python prediction.py --logging_level=DEBUG
"""
from __future__ import print_function

import argparse
import os
import pprint
import sys
import time
import csv
import time

from apiclient import discovery
from apiclient import sample_tools
from oauth2client import client


# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('model_id',
    help='Model Id of your choosing to name trained model')
argparser.add_argument('project_id',
    help='Project Id of your Google Cloud Project')

def print_header(line):
  '''Format and print header block sized to length of line'''
  header_str = '='
  header_line = header_str * len(line)
  print('\n' + header_line)
  print(line)
  print(header_line)


def main(argv):
  # If you previously ran this app with an earlier version of the API
  # or if you change the list of scopes below, revoke your app's permission
  # here: https://accounts.google.com/IssuedAuthSubTokens
  # Then re-run the app to re-authorize it.
  service, flags = sample_tools.init(
      argv, 'prediction', 'v1.6', __doc__, __file__, parents=[argparser],
      scope=(
          'https://www.googleapis.com/auth/prediction',
          'https://www.googleapis.com/auth/devstorage.read_only'))

  try:
    # Get access to the Prediction API.
    papi = service.trainedmodels()

    # List models.
    #print_header('Fetching list of first ten models')
    #result = papi.list(maxResults=10, project=flags.project_id).execute()
    #print('List results:')
    #pprint.pprint(result)

    # Describe model.
    #print_header('Fetching model description')
    #result = papi.analyze(id=flags.model_id, project=flags.project_id).execute()
    #print('Analyze results:')
    #pprint.pprint(result)

    
    arrayYes = ["A","A","0","0","0","0","0","0","0","1","0","0","0","0","1","0","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","0","0","0","0","0","1","0","0","0","0","0","0","0","0","0","55125","1","2","1","1","0","0","0"]
        
    body = {'input': {'csvInstance': arrayYes}}
    
    f = open('matches.txt', 'w')
    
    pprint.pprint ('body:{}'.format(body))
    result = papi.predict( body=body, id=flags.model_id, project=flags.project_id).execute()
    print('Prediction results for "%s"...' % arrayYes)
    pprint.pprint(result)
    count = 1
    with open('test-only-quotes.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print_header('Making some predictions')
            body = {'input': {'csvInstance': row}}
            try:
                result = papi.predict( body=body, id=flags.model_id, project=flags.project_id).execute()
                #    print('Prediction results for "%s"...' % row)
                #    print("#############here {0}".format(result))
                if result['outputLabel'] == 'Y':
                    f.write("Line: {0} Renewed from the test dataset. Row Value: {1}".format(count, row))
                    pprint.pprint("Result {0} and count {1}".format(result['outputLabel'], count))
                    
                    time.sleep(.1)
                count = count+1    
            except:
                e = sys.exc_info()[0]
                print("Error. Continue....{0}".format(e))
    f.close()
  except client.AccessTokenRefreshError:
        print ('The credentials have been revoked or expired, please re-run '
           'the application to re-authorize.')


if __name__ == '__main__':
  main(sys.argv)