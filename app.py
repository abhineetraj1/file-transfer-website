import shutil
from flask import*
from flask import request
import datetime
import zipfile
import os

app = Flask(__name__,static_folder="file")

def scp(a):
	return "<script>alert('"+a+"');</script>"
def rf(a):
	return open(a,"r").read()

def create_file(n):
	w = os.listdir(n)
	g = zipfile.ZipFile((n+".zip"),"w")
	for o in w:
		g.write((n+"/"+o))
	g.close()

def rndm():
	return str(datetime.datetime.now()).replace(":","").replace(".","").replace("-","").replace(" ","")

@app.route("/",methods=["GET"])
def aa():
	return open("index.html","r").read()

@app.route("/main",methods=["GET","POST"])
def aa1():
	if (request.method == "GET"):
		return open("send.html","r").read()
	else:
		w = request.form["link"]
		if (w in os.listdir()):
			create_file(w)
			tt =w+".zip"
			shutil.rmtree(w)
			return send_file(tt)
		else:
			return "<script>alert('no such code found');</script>"+rf("b.html")
@app.route("/send",methods=["GET","POST"])
def aa2():
	if (request.method == "GET"):
		return rf("main.html")
	else:
		files = request.files.getlist('files[]')
		if (len(files) > 10):
			return scp("We don't allow more than 10 files to transfer at once")+rf("main.html")
		else:
			n = rndm()
			os.mkdir(n)
			merr=""
			for file in files:
				file.save(n+"/"+file.filename)
			return rf("output.html").replace("pass-sdfhe8rhe98rhf89erhfe8",n)


if __name__ == '__main__':
	app.run()