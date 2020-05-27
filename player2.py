import vlc
import tkinter
import pafy
from youtube_transcript_api import YouTubeTranscriptApi
global media


url=""


m=tkinter.Tk()
m.title("transcript traverse")
tkinter.Label(m,text="enter the link").grid(row=0)

letty= tkinter.Label(m, text = "enter search key")
textBox1= tkinter.Text(m, height = 2, width =10)
#frame = tkinter.Frame(m,bg="#80c1ff")
#frame.place(relheight=.5,relwidth=.5,relx=.5)

textBox= tkinter.Text(m, height=2, width=10)
textBox.grid()
enterbutton = tkinter.Button(m,text = "enter" , command= lambda:onclick("enter"))

myvar = tkinter.StringVar()
label_time=tkinter.Label(m,textvariable=myvar)


sexy = tkinter.Text(m,height = 2,width = 10)





def onclick(args):
    if args == "enter":
        global url
        global media
        inputValue=textBox.get("1.0","end-1c")
        print(inputValue)
        url=inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
    print(type(media))
    if args == 1:
        media.play()
    if args == 2:
        media.pause()
    if args == 3:
        media.stop()
    if args == 4:
        videoid = url.split('=')
        print(videoid[1])
        transcript_list = YouTubeTranscriptApi.list_transcripts(videoid[1])
        transcript = transcript_list.find_transcript(['en'])
        trans = transcript.fetch()
        #print(trans)

            

        word = textBox1.get("1.0","end-1c")
        print(word)
        mylist=[]
        for i in trans:
            #print(i['text'])
            if word in i['text']:
                print(word)
                startpoint=i['start']
                #timelapse=i['duration']
                print(startpoint)
                #print(timelapse)
                mylist.append(startpoint)
                mylist.append(',')
         
        myvar.set(mylist)     
        
        print(mylist)





    if args == 5:
        #vart = media.get_rate()
        #outer = media.has_vout()
        idq = media.get_length()

        print(idq)

        t = media.video_take_snapshot(0,"C:/Users/Public",0,0)
        print(t)
        #media.set_time(10000)

    if args == 6:
        
        
        #if sexy.get("1.0","end-1c") == "" :
            var = sexy.get("1.0","end-1c")
            var = int(var)

            media.set_time(var)

        
            

        #print(timeValue)



#https://www.youtube.com/watch?v=Ck2gRjj6_2w
              


#nitap@campus123


#button0 = tkinter.Button(m,text="find",width=25, command= showvideo)

button1 = tkinter.Button(m,text='play',width=25, command = lambda:onclick(1))

button2 = tkinter.Button(m,text='pause',width=25, command = lambda:onclick(2))

button3 = tkinter.Button(m,text='stop',width=25, command = lambda:onclick(3))

button4 = tkinter.Button(m,text= 'find word' ,width=25, command = lambda:onclick(4))

button5 = tkinter.Button(m,text='get snapshot', width =25 , command = lambda : onclick(5))

button6 = tkinter.Button(m,text='go to time',width=25, command = lambda:onclick(6))
#button0.grid()
enterbutton.grid()
button1.grid()
button2.grid()
button3.grid()

letty.grid()
textBox1.grid()
button4.grid()
label_time.grid()
button5.grid()
button6.grid()
sexy.grid()

m.mainloop()
