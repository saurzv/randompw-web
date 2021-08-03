function copy(){
	var copyText = document.getElementById("pw");
	copyText.select();
	document.execCommand("copy");
	$("#copy").html("Copied!");
}