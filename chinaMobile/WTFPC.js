co_f="2";
var dCur=new Date();
var adj=(dCur.getTimezoneOffset()*60000)+(8*3600000);
dCur.setTime(dCur.getTime()+adj);
var curt=dCur.getTime().toString();
for (var i=2;i<=(32-curt.length);i++){
	co_f+=Math.floor(Math.random()*16.0).toString(16);
}
co_f+=curt;