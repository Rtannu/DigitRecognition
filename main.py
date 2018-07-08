from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter

#function for creating file numArEx.txt	
def createExamples():
         numberArrayExamples=open('numArEx.txt','a')
         numbersWeHave=range(0,10)
         versionsWeHave=range(1,10)
         

         for eachNum in numbersWeHave:
             for eachVer in versionsWeHave:
                    #print str(eachNum)+'.'+str(eachVer)
                    imageFilePath='Images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
                    ei=Image.open(imageFilePath)
                    eiar=np.array(ei)
                    eiar1=str(eiar.tolist())
                    #print eiar1
                    lineToWrite=str(eachNum)+'::'+eiar1+'\n'
                    #print lineToWrite
                    numberArrayExamples.write(lineToWrite) 


#function for converting image into black and white
def threshold(imageArray):
      balanceAr=[]
      newAr=imageArray
    
      for eachRow in imageArray:
          for eachPix in eachRow:
               #print eachPix
               avgNum=reduce(lambda x,y: int(x)+int(y), eachPix[:3])/len(eachPix[:3])
               balanceAr.append(avgNum)
               #print avgNum      
               #time.sleep(5)
      balance=reduce(lambda x,y : int(x)+int(y),balanceAr)/len(balanceAr)
     
      newAr.setflags(write=True)
      for eachRow in newAr:
          for eachPix in eachRow:
             if reduce(lambda x,y: int(x)+int(y), eachPix[:3])/len(eachPix[:3])>balance :
                  
                  eachPix[0]=255
                  eachPix[1]=255
                  eachPix[2]=255
                  eachPix[3]=255
             else:
                  eachPix[0]=0
                  eachPix[1]=0
                  eachPix[2]=0
                  eachPix[3]=255
      return newAr 



#function for checking image detection
def whatNumIsThis(filePath):
           matchedAr=[]
           loadExample=open('numArEx.txt','r').read()
           loadExamples=loadExample.split('\n')
           #print loadExamples

           i=Image.open(filePath)
           iar=np.array(i)
           #print iar
           iar1=iar.tolist()
           #print iar1
           inQuestion=str(iar1)
           #print inQuestion  
           for eachExample in loadExamples:
                 if len(eachExample) >3:
                    splitEx=eachExample.split('::')
                    #print splitEx
                    #print "roushan raj"
                    currentNum=splitEx[0]
                    currentAr=splitEx[1]

                    eachPixEx=currentAr.split('],')
                    eachPixInQ=inQuestion.split('],')
                    
                    x=0
              
                    while(x< len(eachPixEx)):
                      if eachPixEx[x] ==  eachPixInQ[x]:
                          matchedAr.append(int(currentNum))
                      x+=1
           #print matchedAr
           x=Counter(matchedAr)
           print (x) 
           
           graphX=[]
           graphY=[]
           
          
           for eachThing in x:
                print (eachThing)
                graphX.append(eachThing)
                print (x[eachThing])
                graphY.append(x[eachThing])

           fig=plt.figure()
           ax1=plt.subplot2grid((4,4),(0,0),rowspan=1,colspan=4)
           ax2=plt.subplot2grid((4,4),(1,0),rowspan=3,colspan=4)

           ax1.imshow(iar)
           ax2.bar(graphX,graphY,align='center')
           plt.ylim(400)
           
           xloc=plt.MaxNLocator(12)

           ax2.xaxis.set_major_locator(xloc)

           plt.show()
                    

createExamples()

#loading input Images(which is in Images folder) for detection 
whatNumIsThis('Images/1.6.png')
"""
i=Image.open('Images/numbers/0.1.png')
iar=np.asarray(i)
#threshold(iar)
#print iar
#plt.imshow(iar)
#plt.show() 

i2=Image.open('Images/numbers/y0.4.png')
iar2=np.asarray(i2)


i3=Image.open('Images/numbers/y0.5.png')
iar3=np.asarray(i3)


i4=Image.open('Images/sentdex.png')
iar4=np.asarray(i4)
createExamples()
threshold(iar3)

fig=plt.figure()
ax1=plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
ax2=plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
ax3=plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)
ax4=plt.subplot2grid((8,6),(4,3),rowspan=4,colspan=3)


ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()
"""
