var judgeRangeMap={};
function judgeCalcRet(judge, calcret)
{
	var jr;
	if(judgeRangeMap[judge]!=undefined)
	{
		jr=judgeRangeMap[judge];
	}
	else
	{
		var cur=JudgeRange();
		jr=cur;
		var cons=judge.split("|");
		for(var i=0;i<cons.length;i++)
		{
			var it=JudgeRangeItem();
			it.parse(cons[i]);
			jr.items.push(it);
		}
		judgeRangeMap[judge]=jr;
	}
	return jr.judge(calcret);
}
function parseCalc(calc,dataitem)
{
	var isparam=false;
	var key="";
	var datalist=[];
	var calcstr="";
	for(var i=0;i<calc.length;i++)
	{
		if(calc[i]>='a'&&calc[i]<='z'||calc[i]>='A'&&calc[i]<='Z'||calc[i]>='0'&&calc[i]<='9'||calc[i]=='.')
		{
			isparam=true;
			key+=calc[i];
		}
		else
		{
			if(isparam==true)
			{
				var tmp_f=dataitem.getByKey(key);
				if(tmp_f!=undefined)
					datalist.push(tmp_f);
				else
				{
					if(isNaN(key))return {};
					tmp_f=key*1.0;
					datalist.push(tmp_f);
				}
				key="";
				calcstr+="d";
			}
			calcstr+=calc[i];
			isparam=false;
		}
	}
	if(isparam==true)
	{
		var tmp_f=dataitem.getByKey(key);
		if(tmp_f!=undefined)
			datalist.push(tmp_f);
		else
		{
			if(isNaN(key))return {};
			tmp_f=key*1.0;
			datalist.push(tmp_f);
		}
		key="";
		calcstr+="d";
	}
	return {"calcstr":calcstr,"datalist":datalist};
}
function judgeLogic(logics,data)
{
	var logictkeys={};
	var ret=[];
	for(var i=0;i<data.itemlist.length;i++)
	{
		var it=data.itemlist[i];
		for(var j=0;j<logics.length;j++)
		{
			var lo=logics[j];
			var calcret=0;
			if(lo.condition.length>0)
			{
				//condition
				var outcalc=parseCalc(lo.condition,it);
				if(outcalc.calcstr!=undefined)
				{
					var c_ret=calc(outcalc.calcstr,outcalc.datalist);
					if(c_ret==0)continue;
				}
			}
			if(lo.calc.length>0)
			{
				var outcalc=parseCalc(lo.calc,it);
				if(outcalc.calcstr!=undefined)
				{
					calcret=calc(outcalc.calcstr,outcalc.datalist);
				}
				else continue;
			}
			if(lo.judge.length>0)
			{
				if(judgeCalcRet(lo.judge,calcret))
				{
					var err=Error();
					err.ret=lo.ret;
					err.datatype=it.datatype;
					err.key=lo.key;
					err.msg=lo.msg;
					err.value=calcret;
					var key=lo.key+"_"+lo.ret+"_"+it.datatype;
					if(logictkeys[key]==undefined)
					{
						ret.push(err);
						logictkeys[key]=1;
					}
				}
			}
		}
	}
	return ret;
}
function parseLogic(str)
{
	var ret=[];
	var lines=str.split("\n");
	for(var i=0;i<lines.length;i++)
	{
		var attrs=lines[i].split(",");
		var cur=Logic();
		for(var j=0;j<attrs.length;j++)
		{
			var kv=attrs[j].split(":");
			if(kv.length==2)
			{
				if(kv[0]=="return")
				{
					cur.ret=kv[1]*1;
				}
				else if(kv[0]=="msg")
				{
					cur.msg=kv[1];
				}
				else if(kv[0]=="condition")
				{
					cur.condition=kv[1];
				}
				else if(kv[0]=="calc")
				{
					cur.calc=kv[1];
				}
				else if(kv[0]=="judge")
				{
					cur.judge=kv[1];
				}
				else if(kv[0]=="key")
				{
					cur.key=kv[1];
				}
			}
		}
		ret.push(cur);
	}
	return ret;
}
function calc(str,datalist)
{
	var postfix=intoPostfix(str);
	var res=0;
	var sk=Stack();
	var datalistpos=0;
	for(var i=0;i<postfix.length;i++)
	{
		var token=postfix[i];
		var a,b;
		if(token=='d')sk.push(datalist[datalistpos++]);
		else
		{
			if(token=='N')
			{
				a=sk.top();
				sk.pop();
				sk.push(a==0?1:0);
			}
			else
			{
				b=sk.top();
				sk.pop();
				a=sk.top();
				sk.pop();
				switch(token)
				{
				case '+':
					sk.push(a+b);
					break;
				case '-':
					sk.push(a-b);
					break;
				case '*':
					sk.push(a*b);
					break;
				case '/':
					sk.push(a/b);
					break;
				case '^':
					sk.push(Math.pow(a,b));
					break;
				case 'L':
					sk.push(a<=b?1:0);
					break;
				case 'l':
					sk.push(a<b?1:0);
					break;
				case 'G':
					sk.push(a>=b?1:0);
					break;
				case 'g':
					sk.push(a>b?1:0);
					break;
				case 'n':
					sk.push(a!=b?1:0);
					break;
				case 'e':
					sk.push(a==b?1:0);
					break;
				case 'A':
					sk.push(a&&b?1:0);
					break;
				case 'O':
					sk.push(a||b?1:0);
					break;
				}
			}
		}
	}
	return sk.top();
}
function intoPostfix(expr)
{
	var ret="";
	var s=Stack();
	for(var i=0;i<expr.length;i++)
	{
		var token=expr[i];
		if(token>='a'&&token<='z')  
			ret+=token;  
        else  
            switch(token)  
			{  
			case ')':  
				while(!s.empty()&&s.top()!='(')  
				{  
					ret+=s.top(); 
					s.pop();  
				}  
				s.pop();  
				break;  
			case '(':  
				s.push(token);  
				break;
			case '^':  
				while(!s.empty()&&s.top()=='^')  
				{  
					ret+=s.top();  
					s.pop();  
				}  
				s.push(token);  
				break;  
			case '*' :  
			case '/' :  
				while(!s.empty() && (s.top() == '*'|| s.top() == '/' || s.top() == '^'))  
				{  
					ret+=s.top();   
					s.pop();  
				}  
				s.push(token);   
				break;  
			case '+' :  
			case '-' :  
				while(!s.empty() && (s.top() == '*'|| s.top() == '/' || s.top() == '^'|| s.top() == '+'|| s.top() == '-'))  
				{  
					ret+=s.top(); 
					s.pop();  
				}  
				s.push(token);  
				break; 
			case '&' ://&& A
				while(!s.empty() && (s.top() == 'N'|| s.top() == 'L' || s.top() == 'l'|| s.top() == 'G'|| s.top() == 'g' || s.top() == 'n' || s.top() == 'e' || s.top() == 'A'))  
				{  
					ret+=s.top();   
					s.pop();  
				}  
				s.push('A'); 
				i++;
				break;
			case '|' ://|| O
				while(!s.empty() && (s.top() == 'N'|| s.top() == 'L' || s.top() == 'l'|| s.top() == 'G'|| s.top() == 'g' || s.top() == 'n' || s.top() == 'e' || s.top() == 'A' || s.top() == 'O'))  
				{  
					ret+=s.top();    
					s.pop();  
				}  
				s.push('O'); 
				i++;
				break;
			case '!' :
				if(expr[i+1]=='=')//!= n
				{
					while(!s.empty() && s.top() == 'N')  
					{  
						ret+=s.top(); 
						s.pop();  
					}  
					s.push('n');
					i++;
				}
				else//! N
				{ 
					s.push('N'); 
				}
				break;
			case '=' ://== e
				while(!s.empty() && s.top() == 'N')  
				{  
					ret+=s.top();  
					s.pop();  
				} 
				s.push('e');
				i++;
				break;
			case '>' :
				if(expr[i+1]=='=')//>= G
				{
					s.push('G'); 
					i++;
				}
				else//> g
				{
					s.push('g'); 
				}
				break;
			case '<' :
				if(expr[i+1]=='=')//<= L
				{
					s.push('L'); 
					i++;
				}
				else//< l
				{
					s.push('l'); 
				}
				break;
			}  
    }  
    while (!s.empty())  
    {  
        ret+=s.top(); 
        s.pop();  
    }
	return ret;
}
function Logic()
{
	var ret={};
	ret.ret=0;
	ret.key="";
	ret.msg="";
	ret.condition="";
	ret.calc="";
	ret.judge="";
	return ret;
}
function DataItemForAnalyze()
{
	var ret={};
	ret.datatype=0;
	ret.kv={};
	ret.getByKey=function(key){
		return this.kv[key];
	};
	ret.setByKey=function(key,value){
		this.kv[key]=value;
	};
	return ret;
}

function DataForAnalyze()
{
	var ret={};
	ret.itemlist=[];
	ret.typeindex={};
	ret.getadditem=function(datatype){
		if(this.typeindex[datatype]==undefined)
		{
			var it=DataItemForAnalyze();
			it.datatype=datatype;
			this.itemlist.push(it);
			this.typeindex[datatype]=this.itemlist.length-1;
		}
		return this.itemlist[this.typeindex[datatype]];
	}
	return ret;
}

var JudgeType={"NONE":0,"LT":1,"LTE":2,"GT":3,"GTE":4};
function Error()
{
	var ret={};
	ret.ret=0;
	ret.datatype=0;
	ret.key="";
	ret.msg="";
	ret.value=0;
	return ret;
}
function JudgeRange()
{
	var ret={};
	ret.items=[];
	ret.judge=function(val){
		for(var i=0;i<this.items.length;i++)
		{
			if(this.items[i].judge(val))return true;
		}
		return false;
	};
	return ret;
}
function JudgeRangeItem()
{
	var ret={};
	ret.typea=0;
	ret.a=0;
	ret.typeb=0;
	ret.b=0;
	ret.parse=function (str)
	{
		var parts=str.split("_");
		if(parts.length==2)
		{
			if(parts[0].length==0)
			{
				this.typea=JudgeType.NONE;
			}
			else
			{
				var cur=parts[0][0];
				this.a=parts[0].substring(1)*1.0;
				if(cur=='[')
				{
					this.typea=JudgeType.GTE;
				}
				else if(cur=='(')
				{
					this.typea=JudgeType.GT;
				}
			}
			if(parts[1].length==0)
			{
				this.typeb=JudgeType.NONE;
			}
			else
			{
				var cur=parts[1][parts[1].length-1];
				this.b=parts[1].substring(0,parts[1].length-1)*1.0;
				if(cur==']')
				{
					this.typeb=JudgeType.LTE;
				}
				else if(cur==')')
				{
					this.typeb=JudgeType.LT;
				}
			}	
		}
	};
	ret.judge=function(val)
	{
		if(this.typea!=JudgeType.NONE)
		{
			switch (this.typea)
			{
			case JudgeType.NONE:
				break;
			case JudgeType.LT:
				if(val<this.a);
				else
				{ 
					//printf("return false!\n");
					return false;
				}
				break;
			case JudgeType.LTE:
				if(val<=this.a);
				else
				{
					//printf("return false!\n");
					return false;
				}
				break;
			case JudgeType.GT:
				if(val>this.a);
				else
				{
					//printf("return false!\n");
					return false;
				}
				break;
			case JudgeType.GTE:
				if(val>=this.a);
				else
				{
					//printf("return false!\n");
					return false;
				}
				break;
			default:
				break;
			}
		}
		if(this.typeb!=JudgeType.NONE)
		{
			switch (this.typeb)
			{
			case JudgeType.NONE:
				break;
			case JudgeType.LT:
				if(val<this.b);
				else
				{
					//printf("return false!\n");
					return false;
				}
				break;
			case JudgeType.LTE:
				if(val<=this.b);
				else
				{
					//printf("return false!\n");
					return false;
				}
				break;
			case JudgeType.GT:
				if(val>this.b);
				else
				{
					//printf("return false!\n");
					return false;
				}
				break;
			case JudgeType.GTE:
				if(val>=this.b);
				else
				{
					//printf("return false!\n");
					return false;
				}
				break;
			default:
				break;
			}
		}
		//printf("return true!\n");
		return true;
	};
	return ret;
}