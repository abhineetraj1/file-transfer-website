document.getElementById('toggle').onclick=function () {
	if (document.getElementById('toggle').innerHTML == "=") {
		document.getElementById('tgl').style.display = "block";
		document.getElementById('toggle').innerHTML = "X";
		document.getElementById("content").style.display="none";
	} else {
		document.getElementById("content").style.display="inline";
		document.getElementById('tgl').style.display = "none";
		document.getElementById('toggle').innerHTML = "=";
	}
}