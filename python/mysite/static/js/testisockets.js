function colors(a)
{
	switch(a.ret)
	{
	case 1:return red;
	case 2:return purple;
	case 3:return yellow;
	case 4:return green;
	case 5:return blue;
	default:return "";
	}
}
function results(a)
{
	if(a=="success")return a;
	else return "<font color='red'>"+a+"</font>";
}
function percent(errvalue)
{
	if(errvalue.ret==3||errvalue.ret==4)
	{
		if(errvalue.value==undefined)return "";
		else if(errvalue.value<0.9||errvalue.value>1.1)return "("+(parseInt(10000*errvalue.value)/100)+"%)";
	}
	return "";
}
function q(key)
{
	if(param_map[key]==undefined)return {v:undefined,u:undefined};
	else return param_map[key];
}
function wv(val)
{
	if(val==undefined)return "";
	else return val;
}
function errmap(key,datatype)
{
	if(err_map[key]==undefined)return {"ret":0};
	if(err_map[key][datatype]==undefined)return {"ret":0};
	return err_map[key][datatype];
}
function show(devid){
	var myTable= document.getElementById(devid+"-table"); myTable.style.display="block";
}

function hide(devid){
	var myTable= document.getElementById(devid+"-table"); myTable.style.display ="none";
}