import cv2 
import imageio.v3 as io

width, height, size = 0, 0, 0

longs = []
words = []
bytes = []

def runAll():
    buildLongs()
    longtoHex()
    buildWords()
    wordtoHex()
    buildBytes()
    bytetoHex()


def buildLongs():
    index = 0
    for i in range(0, len(bitmap), 32):
        longs.append(bitmap[i:i+32])
    # write longs array to an output file longs.txt
    with open('assets/longs.txt', 'w') as f:
        for item in longs:
            f.write("%s " % item)
            index+=1
            if index == (width / 32):
                f.write('\n')
                index = 0
def buildWords():
    index = 0
    for i in range(0, len(bitmap), 16):
        words.append(bitmap[i:i+16])
    # write longs array to an output file longs.txt
    with open('assets/words.txt', 'w') as f:
        for item in words:
            f.write("%s " % item)
            index+=1
            if index == (width / 16):
                f.write('\n')
                index = 0
def buildBytes():
    index = 0
    for i in range(0, len(bitmap), 8):
        bytes.append(bitmap[i:i+8])
    # write longs array to an output file longs.txt
    with open('assets/bytes.txt', 'w') as f:
        for item in bytes:
            f.write("%s " % item)
            index+=1
            if index == (width / 8):
                f.write('\n')
                index = 0

def longtoHex():
    index = 0
    # convert every item in longs array to a hex value that is 8 digits long
    for i in range(len(longs)):
        longs[i] = hex(int(''.join(map(str, longs[i])), 2)).lstrip("0x").rstrip("L").zfill(8)
    # print longs array to an output file with a comma between each item and a 0x in front of each item
    with open('assets/hex_UINT32.txt', 'w') as f:
        for item in longs:
            f.write("0x%s, " % item)
            index+=1
            if index == (width / 32):
                f.write('\n')
                index = 0
def wordtoHex():
    index = 0
    # convert every item in longs array to a hex value that is 8 digits long
    for i in range(len(words)):
        words[i] = hex(int(''.join(map(str, words[i])), 2)).lstrip("0x").rstrip("L").zfill(4)
    # print longs array to an output file with a comma between each item and a 0x in front of each item
    with open('assets/hex_UINT16.txt', 'w') as f:
        for item in words:
            f.write("0x%s, " % item)
            index+=1
            if index == (width / 16):
                f.write('\n')
                index = 0
def bytetoHex():
    index = 0
    # convert every item in longs array to a hex value that is 8 digits long
    for i in range(len(bytes)):
        bytes[i] = hex(int(''.join(map(str, bytes[i])), 2)).lstrip("0x").rstrip("L").zfill(2)
    # print longs array to an output file with a comma between each item and a 0x in front of each item
    with open('assets/hex_UINT8.txt', 'w') as f:
        for item in bytes:
            f.write("0x%s, " % item)
            index+=1
            if index == (width / 8):
                f.write('\n')
                index = 0


url = input("Enter image url: ")
#read image from url
img = io.imread(url)
print(img.shape)  # (300, 451, 3)

print('height of the image : ' , img.shape[0])
print('width of the image : ' , img.shape[1])

width = input("Enter width: ")
height = input("Enter height: ")

#create an enum for the three sizes bytes, words, and longs
dataSize = input("Enter size bytes, words, longs or all: ")

width = int(width)
height = int(height)
size = int(size)

#resize image
img = cv2.resize(img, (width, height))
#write resized image to an output file
cv2.imwrite('assets/outputIMG.png', img)

bitmap = []

#if pixel is black, make it white
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j][0] <= 120 and img[i][j][1] <= 120 and img[i][j][2] <= 120:
            bitmap.append(1)
        else:
            bitmap.append(0)
    
index = 0;
# print bitmap array to an output file
with open('assets/output.txt', 'w') as f:
    for item in bitmap:
        f.write("%s " % item)
        index+=1
        if index == width:
            f.write('\n')
            index = 0


if dataSize == 'longs':
    buildLongs()
    longtoHex()
elif dataSize == 'words':
    buildWords()
    wordtoHex()
elif dataSize == 'bytes':
    buildBytes()
    bytetoHex()
elif dataSize == 'all':
    runAll()



