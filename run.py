##This is the code for vardhaman app API
#import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import time as tim
#from functools import wraps
#from telebot import types
from flask import Flask, request, jsonify
#from flask_api import FlaskAPI
import json
import os
#from nltk.tokenize import word_tokenize
from io import StringIO
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import marks as gpa
#import applyper as papply
import attendance as atd

#user_dict={}

#API_TOKEN = '703046139:AAH8uLwxJYHtCVMTdiGHm6ZCxItoQibPZDg'

#bot = telebot.TeleBot(API_TOKEN)
#Bot = telebot.TeleBot(config.bot_token)
#chat_id=config.API_TOKEN
app = Flask(__name__)
#global gid,rid,pid,pper,ppr,rege, rege_attendance, rege_details, rege_cgpa, rege_sgpa, rege_outing
finalurl = "http://studentscorner.vardhaman.org/"
'''gid=[]  # Global storage 
rid=[]  # Roll no storage
pid=[]  # Password storage
pper=[] # Temporary storage of outing
ppr=[]  # Temporary storage of outing
ttt=[]  # Temp storage of rno and pass for logging
rege=["attendance", "details", "name", "cgpa", "c.g.p.a", "CGPA", "C.G.P.A", "sgpa", "SGPA", "s.g.p.a", "S.G.P.A", "outing", "logout"]
rege_attendance = ["attendance"]
rege_details = ["details"]
rege_cgpa = ["cgpa"]
rege_outing = ["outing"]
'''
br = RoboBrowser(history=True, parser="html.parser")

'''def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(*args, **kwargs):
        bot, update = args
        #bot.send_chat_action(chat_id=update.effective_message.chat_id, action=telegram.ChatAction.TYPING)
        return func(bot, update, **kwargs)

    return command_func
'''
'''
def send_welcome(message):
	#starts.acquire()
	bot.reply_to(message, """\
Hi there, I am Vbot here to give you, your things!
For logging in please type "/login"
For help type '/help'\
""")



@bot.message_handler(commands=['help'])
def help(message):
	#helps.acquire()
	bot.reply_to(message,"""
      '/login',
      '/details',
      '/attendance',
      '/cgpa',
      '/sgpa',
      '/logout' 
     for now.""")
	#helps.release()
# error handling if user isn't known yet
# (obsolete once known users are saved to file, because all users
#   had to use the /start command and are therefore known to the bot)
'''
'''def get_user_step(uid):
	if uid in userStep:
	        return userStep[uid]
	else:
		knownUsers.append(uid)
	        userStep[uid] = 0
	        print("New user detected, who hasn't used \"/start\" yet")
	 	return 0
'''
#rno=''
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
'''@bot.message_handler(commands=['login'])
def login(message):
	tid = str(message.from_user.id)
	m=message.text
	print(tid)
	if tid in gid :
		tindex=gid.index(tid)
		rno=rid[tindex]
		pas=pid[tindex]
		gid.remove(tid)
		rid.remove(rno)
		pid.remove(pas)
		bot.send_message(tid,"Try again, logged out old user.")
	else:
		msg=bot.send_message(tid,"Enter your Roll no")
		bot.register_next_step_handler(msg, roll_no)
		
def roll_no(message):
	chat_id = message.chat.id
	rno = message.text
	rno = rno.upper()
	ttt.append(rno)
	try:
		msg=bot.send_message(chat_id,"Enter your password")
		bot.register_next_step_handler(msg, passd)
	except Exception as e:
		Bot.send_message(chat_id,'oooops\nSomething went wrong.\nsend a mail to vardhamanassistant@gmail.com stating the issue.\n')
def passd(message):
	chat_id = message.chat.id
	pas=''
	pas = message.text
	ttt.append(pas)
	rno = ttt[0]
	finalurl = "http://studentscorner.vardhaman.org/"
	finalurl=check_pas(rno,pas)
	tid = str(chat_id)
	print(finalurl)
	tim.sleep(1)
	if(finalurl == "http://studentscorner.vardhaman.org/Students_Corner_Frame.php"):
		f='1'
		print(f)
		sin_id(tid,rno,pas)
		bot.reply_to(message,'Correct credentials, what do you want?')
	else:
		bot.reply_to(message,'Incorrect credentials!, try again')
	del ttt[:]

#////////////////***********************//////////////////////////

@send_typing_action
@bot.message_handler(func=lambda message:True if(len(message.text)==16 or len(message.text)>25) else False)
#@bot.message_handler(commands=['login'])
def login1(message):
	#while(func=lambda message:True if(len(message.text)==16 or len(message.text)>25) else False):
	rno=''
	#one()
	m=message.text
	tid = str(message.from_user.id)
	print(tid)
	if tid in gid :
		tindex=gid.index(tid)
		rno=rid[tindex]
		pas=pid[tindex]
		gid.remove(tid)
		rid.remove(rno)
		pid.remove(pas)
		#bot.reply_to(message,'First logout the other user and then try again')
	if(m[0]=='1'):
		for i in range(0,10):
			rno=rno+m[i]
			#print(rno)
	rno=rno.upper()
	print(rno)
	pas=''
	bot.reply_to(message,"wait")
	if(m[11]=='#' or m[11] == 'h'):
		for i in range(11,len(m)):
			pas=pas+m[i]
		br = RoboBrowser(history=True, parser="html.parser")
		br = RoboBrowser(user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6')
		br.open('http://studentscorner.vardhaman.org')
		form = br.get_form(action="")
		form["rollno"] = rno
		form["wak"] = pas
		br.submit_form(form)
		#global finalurl
		finalurl = "http://studentscorner.vardhaman.org/"
		finalurl=check_pas(rno,pas)
		#finalurl=suburl.geturl()
		print(finalurl)
		tim.sleep(1)
		if(finalurl == "http://studentscorner.vardhaman.org/Students_Corner_Frame.php"):
			f='1'
			print(f)
			#tid = str(message.from_user.id)
			
			sin_id(tid,rno,pas)
			bot.reply_to(message,'Correct Password, what do you want?')
			
		else:
			bot.reply_to(message,'Incorrect password!, try again')
		#logins.release()
#Saving rollno and passwords
def sin_id(tid,rno,pas):
	
	print("In sin")
	if tid not in gid :
		rid.append(rno)
		pid.append(pas)
		print(rno,pas)
		print("sin success")
		dic_gid(tid)
	#semaphore.release()	
#Saving tokenId of user
def dic_gid(tid):
	print("In dic_gid")
	#id={"1":"11"}
	gid.append(tid)
	if(tid in gid):
		print("dic_gid success")
	#semaphore.release()
@send_typing_action
@bot.message_handler(commands=['attendance','atd'])
def attendance(message):	
	tid = str(message.from_user.id)
	#bot.send_chat_action(chat_id=tid, action=telegram.ChatAction.TYPING)
	if(tid in gid):
		tindex=gid.index(tid)
		rno=rid[tindex]
		pas=pid[tindex]
		t = atd.attendance(tid,rno,pas)
		
	else:
		bot.reply_to(message,"First login to get details")
	#atds.release()

@send_typing_action
@bot.message_handler(commands=['details','det'])
def details(message):
	print("In details",finalurl)
	tid = str(message.from_user.id)
	if(tid in gid):
		det=get_det(tid)
		
		bot.reply_to(message,det)
		if(det != "First login to get details!"):
			if tid in gid :
				tindex=gid.index(tid)
				rno=rid[tindex]
			purl="http://resources.vardhaman.org/images/cse/"
			purl=purl+rno
			purl=purl+".jpg"
			print(purl)
			try:
				bot.send_photo(chat_id=tid, photo=purl)
			except:
				bot.reply_to(message,"We cannot send the photo to your phone.\nIf you got the photo previously in the same phone, please send a mail to \n vardhamanassistant@gmail.com stating the issue.")
	else:
		bot.reply_to(message,"First login to get details")
	#detailss.release()
@bot.message_handler(commands=['logout'])
def logout(message):
	#logouts.acquire()
	#global finalurl
	tid = str(message.from_user.id)
	if tid in gid :
		tindex=gid.index(tid)
		rno=rid[tindex]
		pas=pid[tindex]
		print(rno,pas)
	#try:
	if(tid in gid):
		tid = str(message.from_user.id)
		tindex=gid.index(tid)
		rno=str(rid[tindex])
		pas=str(pid[tindex])
		br.open("http://studentscorner.vardhaman.org/logout.php")
		finalurl = "http://studentscorner.vardhaman.org/"
		gid.remove(tid)
		rid.remove(rno)
		pid.remove(pas)
		bot.reply_to(message,	"loggedout successfully!")
	else:
		bot.reply_to(message,"I think you have not loggedIn.")
	#finally:
		#logouts.release()
def check_pas(rno,pas):
	br = RoboBrowser(history=True, parser="html.parser")
	br = RoboBrowser(user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6')
	br.open('http://studentscorner.vardhaman.org')
	form = br.get_form(action="")
	form["rollno"] = rno
	form["wak"] = pas
	br.submit_form(form)
	checkrno=str(br.select)
	#time.sleep(5)
	#print(finalurl)
	if(rno in checkrno):
		finalurl="http://studentscorner.vardhaman.org/Students_Corner_Frame.php"
		print("In check_pas",finalurl)
		return(finalurl)
	else:
		return False

def get_det(tid):
	#global finalurl
	#if tid in gid :
	tindex=gid.index(tid)
	rno=rid[tindex]
	pas=pid[tindex]
	print(rno,pas)
	#else:
	#	return("First Login")
	br = RoboBrowser(history=True, parser="html.parser")
	br = RoboBrowser(user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6')
	br.open('http://studentscorner.vardhaman.org')
	form = br.get_form(action="")
	form["rollno"] = rno
	form["wak"] = pas
	br.submit_form(form)
	#br.open("http://studentscorner.vardhaman.org")
	print(rno)
	#bot.reply_to(m,"wait")
	br.open("http://studentscorner.vardhaman.org/student_information.php")
	bt=br.parsed()
	th=br.select("th")#3
	td=br.select("td")#8
	print("In details "+rno)
	#print(z.geturl())
	#if finalurl != "http://studentscorner.vardhaman.org/":
	try:
		return(str(th[3].text.strip())+":"+str(td[8].text.strip())+"\n"+str(th[10].text.strip())+":"+str(td[17].text.strip())+"\n"+str(th[29].text.strip())+":"+(str(td[33].text.strip()))+"\n"+str(th[31].text.strip())+":"+str(td[35].text.strip()))#details
	except IndexError:
		return("Something is wrong")
	#else:
	#	return("First login to get details!")
	#return 0
@bot.message_handler(commands=['outing'])
def outing(message):
	tid = str(message.from_user.id)
	if tid in gid:
		tindex=gid.index(tid)
		rno=rid[tindex]
		pas=pid[tindex]
		#out_date=out.out_datetime(tid)
		#in_date=out.in_datetime(tid)
		#reason=out.reason(tid)
		#status=
		c=papply.check_hostel(rno,pas)
		if(c=="True"):
			out_datetime(rno,pas,tid)
		else:
			bot.reply_to(message,"You are not a hosteler! :).\nIf it is wrong please send a mail to vardhamanassistant@gmail.com stating the issue.")
		#bot.reply_to(message,status)
		#driver = webdriver.Firefox()
		#driver.get('http://studentscorner.vardhaman.org/students_permission_form.php')
		#driver.save_screenshot('permission.png')
		#driver.quit()
		#n=str(tid)+'.png'
		#bot.send_photo(message, open(n, 'rb'))
		
	else:
		bot.reply_to(message,"First login to apply permission")
def out_datetime(rno,pas,tid):
	chat_id = tid
	ppr.append(rno)
	ppr.append(pas)
	#name="user"
	#user = User(name)
	#user_dict[chat_id] = user
	#user.rno=rno
	#user.pas=pas
	#user.tid=tid
	try:
		msg=bot.send_message(chat_id,"Enter outdate and time")
		bot.register_next_step_handler(msg, in_datetime)
	except Exception as e:
		Bot.send_message(chat_id,'oooops\nSomething went wrong.\nsend a mail to vardhamanassistant@gmail.com stating the issue.\n')


def in_datetime(message):
	chat_id = message.chat.id
	#user = user_dict[chat_id]
	out_time=message.text
	pper.append(out_time)
	
	#user.out_time = out_time
	print(out_time)
	try:
		msg=bot.reply_to(message,"Enter indate and time")
        #if not age.isdigit():
        #    msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #    bot.register_next_step_handler(msg, process_age_step)
        #    return
        
        #markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        #markup.add('Yes', 'No')
        #msg = bot.reply_to(message, 'Do you want to apply', reply_markup=markup)
		bot.register_next_step_handler(msg, reason)
	except Exception as e:
		bot.send_message(message,'oops\nSomething went wrong.\nsend a mail to vardhamanassistant@gmail.com stating the issue.\n')



def reason(message):
	chat_id = message.chat.id
	#user = user_dict[chat_id]
	in_time = message.text
	pper.append(in_time)
	#user = user_dict[chat_id]
	#user.in_time = in_time
	try:
		msg=bot.reply_to(message,"Enter reason :)")
        	
		bot.register_next_step_handler(msg, yes_no)
        	#bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.sex)
	except Exception as e:
		bot.send_message(message,'oooops\nSomething went wrong.\nsend a mail to vardhamanassistant@gmail.com stating the issue.\n')

def yes_no(message):
	chat_id = message.chat.id
	reas = message.text
	#user = user_dict[chat_id]
	#user.reas = reas
	pper.append(reas)
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Yes', 'NO')
	msg = bot.reply_to(message, 'Do you want to apply', reply_markup=markup)
	bot.register_next_step_handler(msg, applying)
    
def applying(message):
	chat_id = message.chat.id
	ask = message.text
        #user = user_dict[chat_id]
	if(ask == u'Yes'):
		#tindex=gid.index(tid)
		#rno=rid[tindex]
		#pas=pid[tindex]
		tt=papply.applyf(ppr[0],ppr[1],pper[0],pper[1],pper[2])
		bot.reply_to(message,tt)
		
		tt = papply.form(ppr[0], ppr[1])
		f = StringIO()
		# write some content to 'f'
		f.write("tt 'test.html'")
		f.seek(0)
		file_data = open('test.html', 'rb')
		tb = telebot.TeleBot(API_TOKEN)
		ret_msg = tb.send_document(chat_id, file_data)
		assert ret_msg.message_id
		ret_msg = tb.send_document(chat_id, ret_msg.document.file_id)
		assert ret_msg.message_id
		del ppr[:]
		del pper[:]
	elif(ask == u'No'):
		bot.reply_to(message,"You have cancelled to submit the form.")
		del ppr[:]
		del pper[:]
@bot.message_handler(commands=['cgpa','CGPA','C.G.P.A','c.g.p.a'])
def Cgpa(message):
	#cgpas.acquire()
	#global finalurl
	tid = str(message.from_user.id)
	#if(tid in gid):
	if tid in gid :
		tindex=gid.index(tid)
		rno=rid[tindex]
		pas=pid[tindex]
		data=gpa.cgpa(rno,pas)
		bot.reply_to(message,data)
		print(rno,pas)
	else:
		bot.reply_to(message,"First Login")

@bot.message_handler(commands=['sgpa','SGPA','S.G.P.A','s.g.p.a'])
def Sgpa(message):
	chat_id = message.chat.id
	tid = str(chat_id)
	if tid in gid :
		try:
			msg=bot.send_message(chat_id,"Enter semester number")
			bot.register_next_step_handler(msg, Sgpan)
		except Exception as e:
			Bot.send_message(chat_id,'oooops\nSomething went wrong.\nsend a mail to vardhamanassistant@gmail.com stating the issue.\n')
	else:
		bot.reply_to(message,"First Login")
def Sgpan(message):
	tid = str(message.chat.id)
	mtext=str(message.text)
#	semid=str(semid)
	print(gid,rid, pid)
	tindex=gid.index(tid)
	rno=rid[tindex]
	pas=pid[tindex]
	data=gpa.sgpa(rno,pas,mtext)
	bot.reply_to(message,data)
	print(rno,pas)
	#sgpas.release()
#schedule.every().day.at("00:29").do(push)
#@bot.message_handler(func=lambda message: False) #cause there is no message
def push():
	now = datetime.now()
	print(now.time())
	l=len(gid)
	for i in range(0,l+1):
		tid=gid[i]
		a=get_atd(tid)
		bot.send_message(message,a)
def papers(bot, update):
    keyboard = [[InlineKeyboardButton("2018-2019", callback_data='1'),
                 InlineKeyboardButton("2017-2018", callback_data='2')],
                [InlineKeyboardButton("2016-2017", callback_data='3'),
                 InlineKeyboardButton("2015-2016", callback_data='4')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)
@bot.message_handler(func=lambda message:True)
def regular_expression(message):
	print("Entered into rege_expression")
	m = message.text
	tid = str(message.from_user.id)
	if tid in gid :
		tindex=gid.index(tid)
		rno=rid[tindex]
		pas=pid[tindex]
		tokens = word_tokenize(m)
		same_token = list(set(tokens) & set(rege))
		print(type(same_token))
		print(same_token, same_token[0])
		if(same_token[0] in rege_attendance):
			l=atd.attendance(tid,rno,pas)
		if(same_token[0] in rege_details):
			details(message)
		if(same_token[0] in rege_cgpa):
			Cgpa(message)
		if(same_token[0] in rege_outing):
			outing(message)
#if(same_token in rege_attendance):
	else:
		bot.reply_to(message,'First login to access me!')		        

@bot.message_handler(func=lambda m: True)
def push(message): 
	schedule.every().day.at('00:07').do(push, tid="")
	l=len(gid)
	for i in range(0,l+1):
		tid=gid[i]
		a=get_atd(tid)
		
		bot.reply_to(message,"Attendance is:"+a) 
'''
#@app.route('/', methods=['POST'])
def check_url(timeout=13 ):
	try:
		urlopen("http://studentscorner.vardhaman.org",timeout=timeout).getcode() == 200
		return("up")
	except URLError as e:
		print("Wrong URL",e)
		return("down")
	except socket.timeout as e:
		print("Not working")
		return("down")
		
@app.route("/login/<string:pas>", methods=['GET'])
def check_cred(rno,pas):
	status = check_url()
	if(status == "down"):
		return jsonify({'site':'down'})
	else:
		br = RoboBrowser(history=True, parser="html.parser")
		br = RoboBrowser(user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6')
		br.open('http://studentscorner.vardhaman.org')
		form = br.get_form(action="")
		form["rollno"] = rno
		form["wak"] = pas
		br.submit_form(form)
		checkrno=str(br.select)
		if(rno in checkrno):
			br.open("http://studentscorner.vardhaman.org/student_information.php")
			bt=br.parsed()
			th=br.select("th")#3
			td=br.select("td")#8
			name = str(td[8].text.strip())
			print("In check_pas",finalurl)
			return jsonify({'valid':'True','rollno': rno, 'pas': pas, 'name': name })
		else:
			return jsonify({'valid':'False'})
@app.route('/')
def demo():
	return jsonify({ 'text' : "Hello" })
@app.route("/check/<string:pas>", methods=['GET'])
def check(pas):
	print(pas)
	t = list(pas)
	rno = pas[0:10]
	rno = rno.upper()
	print(rno)
	pas = "#"+pas[11:]
	t = check_cred(rno, pas)
	return (t)

@app.route("/attendance/<string:pas>", methods=['GET'])
def attendance(pas):
	print(pas)
	t = list(pas)
	rno = pas[0:10]
	rno = rno.upper()
	print(rno)
	pas = "#"+pas[11:]
	status = check_url()
	if(status == "down"):
		return jsonify({'site':'down'})
	else:
		t = atd.attendance(rno, pas)
		if(t == "down"):
			return jsonify({'atd_site':'down'})
		try:
			try:
				t = int(t)
				return jsonify({'type':'int','attendance': t })
			except:
				pass
			try:
				t = float(t)
				return jsonify({'type':'float','attendance': t })
			except ValueError:
				return jsonify({'type':'string','attendance': t })
		except ValueError:
			return jsonify({'type':'string','attendance': t })

@app.route("/cgpa/<string:pas>", methods=['GET'])
def cgpa(pas):
	print(pas)
	t = list(pas)
	rno = pas[0:10]
	rno = rno.upper()
	print(rno)
	pas = "#"+pas[11:]
	status = check_url()
	if(status == "down"):
		return jsonify({'site':'down'})
	else:
		t = gpa.cgpa(rno, pas)
		#if(t == "down"):
		#	return jsonify({'atd_site':'down'})
		try:
			try:
				#t = int(t)
				return jsonify({'type':'float','cgpa': t })
			except:
				pass
			try:
				t = float(t)
				return jsonify({'type':'float','cgpa': t })
			except ValueError:
				return jsonify({'type':'string','cgpa': t })
		except ValueError:
			return jsonify({'type':'string','cgpa': t })

@app.route("/period_attendance/<string:pas>", methods=['GET'])
def period_attendance(pas):
	print(pas)
	t = list(pas)
	rno = pas[0:10]
	rno = rno.upper()
	print(rno)
	pas = "#"+pas[11:]
	status = check_url()
	if(status == "down"):
		return jsonify({'site':'down'})
	else:
		t = atd.period_attendance(rno, pas)
		if(t == "down"):
			return jsonify({'atd_site':'down'})
		pa = json.loads(t)
	#print(type(pa))
	#temp = jsonify(pa)
		return jsonify(pa)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
