document.getElementById('drg').ondragover = function (e) {
	e.preventDefault();
	e.stopPropagation();
}
document.getElementById('drg').ondragend = function (e) {
	e.preventDefault();
	e.stopPropagation();
	document.getElementById("drg").style.borderColor="#ccc";
}
document.getElementById('drg').ondragenter = function (e) {
	e.preventDefault();
	e.stopPropagation();
	document.getElementById("drg").style.borderColor="#84a9ff";
}
document.getElementById('drg').ondragexit = function (e) {
	e.preventDefault();
	e.stopPropagation();
	document.getElementById("drg").style.borderColor="#84a9ff";
}
document.getElementById('drg').ondragstart = function (e) {
	e.preventDefault();
	e.stopPropagation();
	document.getElementById("drg").style.borderColor="#84a9ff";
}
document.getElementById('drg').ondrag = function (e) {
	e.preventDefault();
	e.stopPropagation();
}
document.getElementById('drg').ondragleave = function (e) {
	e.preventDefault();
	e.stopPropagation();
	document.getElementById("drg").style.borderColor="#ccc";
}

document.getElementById('drg').ondrop = function (e) {
	e.preventDefault();
	e.stopPropagation();
	document.getElementsByTagName('input')[1].files = e.dataTransfer.files;
	document.getElementById("drg").style.borderColor="#ccc";
	setTimeout(function () {
		rt = get_len_b();
		if (rt < 75) {
			document.getElementById("drg").innerHTML = (e.dataTransfer.files).length + " file(s) selected <br>Size: "+rt+" MB";
			document.getElementById("frm").style.display="block";
		} else {
			alert("Upload files with total size less than 75 MB");
		}
	}, 1000);
}
document.getElementsByTagName('input')[0].oninput = function () {
	setTimeout(function () {
		rt=get_len();
		if (rt < 75) {
			document.getElementsByTagName('input')[1].files = document.getElementsByTagName('input')[0].files;
			document.getElementById("drg").innerHTML = (document.getElementsByTagName('input')[0].files).length + " file(s) selected <br>Size: "+rt+" MB";
			document.getElementById("frm").style.display="block";
		} else {
			alert("Upload files with total size less than 75 MB");
		}
	}, 1000);
}
function get_len() {
	var n=0;
	var i =0 ;
	while (i < document.getElementsByTagName("input")[0].files.length) {
		n = n + document.getElementsByTagName("input")[0].files[i].size;
		i++;
	}
	return Math.floor((n/1024)/1024);
}
function get_len_b() {
	var n=0;
	var i =0 ;
	while (i < document.getElementsByTagName("input")[1].files.length) {
		n = n + document.getElementsByTagName("input")[1].files[i].size;
		i++;
	}
	return Math.floor((n/1024)/1024);
}
document.getElementsByTagName("button")[0].onclick = function (e) {
	e.preventDefault();
	e.stopPropagation();
	document.getElementById("msg").style.display="block";
	document.getElementsByTagName("form")[0].submit();
}