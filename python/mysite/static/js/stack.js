function Stack()
{
	var ret={};
	ret.STACKMAX=100;
	ret._stack=new Array(this.STACKMACK);
	ret._top=-1;
	ret.empty=function(){
		if(this._top==-1){
			return true;
		}
		else{
			return false;
		}
	};
	ret.push=function(elem){
		if(this._top==this.STACKMAX-1){
			return "stack full";
		}
		else{
			this._top++;
			this._stack[this._top] = elem;
		}
	};
	ret.pop=function(){
		if(this._top==-1){
			return "empty stack";
		}
		else{
			var x = this._stack[this._top];
			this._top--;
			return x;
		}
	};
	ret.top=function(){
		if(this._top!=-1){
			return this._stack[this._top];
		}
		else{
			return "empty stack";
		}
	};
	return ret;
};