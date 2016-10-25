from __future__ import print_function
import scipy.stats as stats
import json, os


####################
# calculate the rank correlation between the site ranks (standard solr rank from SSOAR)
# and our experimental participant ranks.
#
# @author: philipp.schaer@th-koeln.de
####################


results = open('./usage-citeseerx.csv', 'w')

json_files = [pos_json for pos_json in os.listdir('./ranks-citeseer') if pos_json.endswith('.json')]

for js in json_files:
    with open(os.path.join('./ranks-citeseer',js)) as file:
        data = json.load(file)
        for d in data['doclist']:
            cited = d['citeBy']
            docid = d['docid']
            if(len):                                
                result = docid + ";" + str(cited)                
            else:
                result = docid + ";nan"
            results.write(result + '\n')
            
results.close()

# print stats.kendalltau(x,y)