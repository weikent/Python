function testit()
{
	var did='DFEDB715A9F1ADBADC8F3FEAD801F6C9';
	/*var pa=-1;
	var pfa=-1;
	var ia=0.03;
	var pb=87;
	var pfb=0.8;
	var ib=1;
	var vb=220;
	var qb=65;
	var pc=270;
	var pfc=0.8
	var ic=1;
	var vc=220;
	var qc=200;*/
	/*var pa=88;
	var pfa=0.4;
	var ia=1;
	var va=220;
	var qa=200;
	var pb=176;
	var pfb=0.8;
	var ib=1;
	var vb=220;
	var qb=300;
	var pc=88;
	var pfc=0.4
	var ic=1;
	var vc=220;
	var qc=0;*/
	/*var pa=130;
	var pfa=0.8;
	var ia=1;
	var va=220;
	var qa=65;
	var pb=200;
	var pfb=0.8;
	var ib=1;
	var vb=220;
	var qb=200;
	var pc=110;
	var pfc=0.5
	var ic=1;
	var vc=220;
	var qc=200;
	var pa=176;
	var pfa=0.8;
	var ia=1;
	var va=220;
	var qa=200;
	var pb=110;
	var pfb=0.5;
	var ib=1;
	var vb=220;
	var qb=5;
	var pc=176;
	var pfc=0.8
	var ic=1;
	var vc=220;
	var qc=100;
	var jsonx='{"result":"success","errorCode":"9999","list":[{"sensorType":"6", "paramType":"75", "paramValue":"16.000", "paramUnit":"V", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"76", "paramValue":"27.800", "paramUnit":"V", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"77", "paramValue":"405.10", "paramUnit":"V", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"78", "paramValue":"406.30", "paramUnit":"V", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"79", "paramValue":"402.70", "paramUnit":"V", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"80", "paramValue":"0.1400", "paramUnit":"A", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"81", "paramValue":"0.6113", "paramUnit":"", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"82", "paramValue":"'+pfa+'", "paramUnit":"", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"83", "paramValue":"'+pfb+'", "paramUnit":"", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"84", "paramValue":"'+pfc+'", "paramUnit":"", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"85", "paramValue":"40.000", "paramUnit":"W", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"90", "paramValue":"243.70", "paramUnit":"KW.h", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"91", "paramValue":"50.000", "paramUnit":"Hz", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"95", "paramValue":"'+va+'", "paramUnit":"V", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"100", "paramValue":"'+ia+'", "paramUnit":"A", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"105", "paramValue":"'+pa+'", "paramUnit":"W", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"106", "paramValue":"'+qa+'", "paramUnit":"Var", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"110", "paramValue":"81.900", "paramUnit":"KW.h", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"115", "paramValue":"'+vb+'", "paramUnit":"V", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"120", "paramValue":"'+ib+'", "paramUnit":"A", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"125", "paramValue":"'+pb+'", "paramUnit":"W", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"126", "paramValue":"'+qb+'", "paramUnit":"Var", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"130", "paramValue":"90.800", "paramUnit":"KW.h", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"135", "paramValue":"'+vc+'", "paramUnit":"V", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"140", "paramValue":"'+ic+'", "paramUnit":"A", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"145", "paramValue":"'+pc+'", "paramUnit":"W", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"146", "paramValue":"'+qc+'", "paramUnit":"Var", "paramTime":"1480667052802"},{"sensorType":"6", "paramType":"150", "paramValue":"71.100", "paramUnit":"KW.h", "paramTime":"1480667052802"}]}';
	*/
	var jsonx='{"result":"success","errorCode":"9999","list":[{"sensorType":"7", "paramType":"1", "paramValue":"16.000", "paramUnit":"m3/h", "paramTime":"1480667052802"},{"sensorType":"7", "paramType":"2", "paramValue":"27.800", "paramUnit":"C", "paramTime":"1480667052802"},{"sensorType":"7", "paramType":"3", "paramValue":"5.1", "paramUnit":"Mpa", "paramTime":"1480667052802"}]}';
	$("#result").append("<div id='DFEDB715A9F1ADBADC8F3FEAD801F6C9\\1'></div>");
	testdevidport({responseText:jsonx},'DFEDB715A9F1ADBADC8F3FEAD801F6C9\\1');
}