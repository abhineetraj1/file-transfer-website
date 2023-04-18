import shutil
import qrcode
import zipfile
import datetime
import os
from flask import*
from flask import render_template
import qrcode

app = Flask(__name__, static_folder="static",template_folder=os.getcwd())

url="http://localhost:5000/"

#This function is created to delete first 4 files in directory in order to sustain server space
def dtl():
	try:
		k=os.listdir()
		for i in k:
			if k.index(i) != 4:
				if (".zip" in i):
					os.remove(i)
			else:
				break
	except Exception as sr:
		print(sr)

def rdm():
	return str(datetime.datetime.now()).replace(" ","").replace(":","").replace(".","").replace("-","")

@app.route("/", methods=["GET"])
def a1():
	dtl()
	return render_template("index.html")

@app.route("/send", methods=["GET","POST"])
def a3():
	if request.method == "POST":
		g= request.files.getlist("files[]")
		h=rdm() #random number is generated
		os.mkdir(f"files/{h}") #folder is created by name of that random number and files uploaded are stored in it
		qrcode.make(f"{url}/data/{h}/").save(f"files/{h}/qrcode.png")
		for i in g:
			i.save(f"files/{h}/{i.filename}")
		return render_template("post.html", file_id=h)
	else:
		return render_template("send.html")

@app.route("/recieve", methods=["GET","POST"])
def a4():
	if request.method == "GET":
		return render_template("recieve.html", err="none")
	else:
		#In this function if the directory name with that download ID exists then the folder is converted into zip and sent to client
		nm=request.form["id"]
		if nm in os.listdir("files"):
			zp = zipfile.ZipFile(f"{nm}.zip", 'w') 
			for i in os.listdir(f"files/{nm}"):
				zp.write(f"files/{nm}/{i}")
			zp.close()
			shutil.rmtree(f"files/{nm}")
			return send_file(f"{nm}.zip")
		else:
			return render_template("recieve.html", err="No file(s) available")

@app.route("/files/<id>/qrcode.png",methods=["GET"])
def a6(id):
	try:
		return send_file(f"files/{id}/qrcode.png") #function for generating QRcode for download link
	except:
		return "404"

@app.route("/data/<nm>")
def a7(nm):
	if nm in os.listdir("files"):
		zp = zipfile.ZipFile(f"{nm}.zip", 'w') 
		for i in os.listdir(f"files/{nm}"):
			zp.write(f"files/{nm}/{i}")
		zp.close()
		shutil.rmtree(f"files/{nm}")
		return send_file(f"{nm}.zip")
	else:
		return render_template("recieve.html", err="No file(s) available")

#Adding custom 404 error template
@app.errorhandler(404)
def a12(e):
	return render_template("err.html",err="404")

#Error handling of internal server error
@app.errorhandler(501)
def a12(e):
	return render_template("err.html",err="501")

if __name__ == '__main__':
	app.run()
