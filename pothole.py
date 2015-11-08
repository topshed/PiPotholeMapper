import microstacknode.gps.l80gps as mst

import lsm
import time

tmstmp = time.strftime("%Y%m%d-%H%M%S")
f = open('pothole'+ tmstmp+'.log','w')
gps = mst.L80GPS()
lsm = lsm.Adafruit_LSM303()
f.write('starting')
time.sleep(1)

def lock_check():
    try:
        x = gps.gprmc
        return True
    except mst.DataInvalidError:
        return False

def getLatLon():
     coords = gps.gpgll
     lat = coords['latitude']
     lon = coords['longitude']
     return lat,lon

def getAccel():
    acc = lsm.read()
    a_x = acc[0][0]
    a_y = acc[0][1]
    a_z = acc[0][2]
    m_x = acc[1][0]
    m_y = acc[1][1]
    m_z = acc[1][2]
    return a_x, a_y, a_z, m_x, m_y, m_z

while True:
    if lock_check():
        while True:
            try:
                pos = getLatLon()
                for t in range(10):
                    bumps = getAccel()
                    f.write(str(pos)+ ' ' + str(bumps) + '\n')
                    time.sleep(0.1)
            except mst.DataInvalidError:
                f.write('No GPS lock')

    else:
        f.write('No GPS lock')
        print('No GPS Lock')
    time.sleep(60)
f.close()
