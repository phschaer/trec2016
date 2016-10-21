from __future__ import print_function
import scipy.stats as stats
import json, os


####################
# calculate the rank correlation between the site ranks (standard solr rank from SSOAR)
# and our experimental participant ranks.
#
# @author: philipp.schaer@th-koeln.de
####################


results = open('./result.csv', 'w')

json_files = [pos_json for pos_json in os.listdir('./ranks') if pos_json.endswith('.json')]

for js in json_files:
    with open(os.path.join('./ranks',js)) as file:
        data = json.load(file)
        site = list()
        experimental = list()
        for d in data['doclist']:
            site.append(d['site-ranking'])
            experimental.append(d['docid'])
        qid = data['qid']
        print ("x=" + str(site))
        print ("y=" + str(experimental))
        if(len(site)!=0):
            result = qid + ";" + str(stats.kendalltau(site,experimental)[0]) 
            #print (result)        
        else:
            result = qid + ";nan"
            #print (result)            
        results.write(result + '\n')
results.close()

# print stats.kendalltau(x,y)