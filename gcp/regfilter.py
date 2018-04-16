import re 

with open('bigquery.practice','r') as file_read:
    with open('gcp.bigquery.practice','w') as file_write:
        data = file_read.read()
        #pattern = re.compile('C:\\\[^Prog].*|http:.*') # gcp storage practice 
        #pattern = re.compile('C:\\\[^Prog].*|http:.*|Table.*|\s*.*complete|\s*.*created|\s*.*DONE|\s*.*Id') # gcp bigquery practice 
        pattern = re.compile('C:\\\[^Prog].*|http:.*|Table.*|bq.*|\s*.*complete|\s*.*created|\s*.*DONE|\s*.*Id|') # gcp bigquery practice 
        match = pattern.finditer(data)
        print(match)
        tmplist = []
        for mat in match:
            if mat.group() not in tmplist:
                tmplist.append(mat.group())
                file_write.write(mat.group().strip('\n'))
                file_write.write('\n')

    for tmp in tmplist:
        print(tmp)        
          # for i in range(0,len(mat),2):
          #     print(mat[i])