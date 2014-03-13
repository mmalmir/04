import urllib2
import re

######## load train and test ids
print "loading train and test IDs..."
f = open("epconfessions-trainIDs.txt","rt")
trainIDs = []
for line in f:
    trainIDs.append(int(line))

f = open("epconfessions-testIDs.txt","rt")
testIDs = []
for line in f:
    testIDs.append(int(line))


print "loading web pages..."
f = open("epconfessions-release.txt","rt")

tags = ["Hugs","Rocks","Teehee","Understand","Wow"]
# exemplar line: http://www.experienceproject.com/confessions.php?cid=2,0,3,19,0,3
url = "http://www.experienceproject.com/confessions.php?cid="
linrex = re.compile("http\:\/\/www\.experienceproject\.com\/confessions\.php\?cid\=([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+)")
exprex = re.compile("<div class=\"story-content\" id=\"confession_div\">([\s\w].+?)</div>")
wrdrex = re.compile("([\w]+)")
for line in f:
    list = linrex.findall(line)[0]
    id = int(list[0])
    if id in trainIDs or id in testIDs:
        #read experience, parse it
        try:
            f = urllib2.urlopen(url+list[0])
        except:
            print "Exception in opening url:"+url+list[0]
            continue
        html = f.read()
        content = exprex.findall(html)
        if len(content)>0:
            words = wrdrex.findall(content[0])
            print words
            print content
f.close()

