function setCookie(name, value, expireday) {
	var exp = new Date();
	exp.setTime(exp.getTime() + expireday*24*60*60*1000); 
	document.cookie = name+"="+escape(value)+"; expires"+"="+exp.toGMTString();
}
function getCookie(name) {
	var cookieStr = document.cookie;
	if(cookieStr.length > 0) {
		var cookieArr = cookieStr.split(";");
		for (var i=0; i<cookieArr.length; i++) {
			var cookieVal = cookieArr[i].split("=");
			if(cookieVal[0] == name) {
				return unescape(cookieVal[1]);
			}
		}
	}
	return "";
}