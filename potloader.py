import folium
import webbrowser
import os

CWD = os.getcwd()
colours = ['red','blue','green','orange','purple','pink','black']
INFILENAME='pothole20151107-101115.log'
OUTFILENAME='pothole.html'
file = open(INFILENAME, "r")
map_osm = folium.Map(location=[52, -1.3],zoom_start=9)
counter = 0
while 1:
    line = file.readline()
    counter +=1
    if not line:
        break
    #if (counter%5 == 0) and ('GPS' not in line):
    if ('GPS' not in line):
        data = line.split(",")
        lat = data[0][1:]
        lon = data[1][:-1]
        jiggle = abs(int(data[2][2:]))
        '''if abs(int(jiggle)) > 150:
            COL = colours[5]'''
        if jiggle > 250 and jiggle < 499 :
            COL = colours[4]
        elif jiggle > 500 and jiggle < 1000:
            COL = colours[3]
        elif jiggle > 1000:
            COL = colours[0]
        '''else:
            COL = colours[2]'''
        map_osm.simple_marker([lat,lon],popup="bob",marker_icon='info-sign',marker_color=COL)



    map_osm.create_map(path=OUTFILENAME)


webbrowser.open_new('file://'+CWD+'/'+OUTFILENAME)
