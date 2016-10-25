from __future__ import print_function
import scipy.stats as stats
import json, os


####################
# calculate the rank correlation between the site ranks (standard solr rank from SSOAR)
# and our experimental participant ranks.
#
# @author: philipp.schaer@th-koeln.de
####################


results = open('./kendall-citeseerx.csv', 'w')

json_files = [pos_json for pos_json in os.listdir('./ranks-citeseer') if pos_json.endswith('.json')]

for js in json_files:
    with open(os.path.join('./ranks-citeseer',js)) as file:
        data = json.load(file)
        site = list()
        experimental = list()
        position = 0
        for d in data['doclist']:
            site.append(d['ranks'])
            experimental.append(position)
            position = position +1
        qid = js
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