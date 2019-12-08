<html>
 <body>
  <p>
   let Throttleable=new function(){let _self=this;this.throttlingTime={};this.isThrottled=function(a){return(_self.throttlingTime[a]!==undefined&amp;&amp;!isNaN(_self.throttlingTime[a])&amp;&amp;_self.throttlingTime[a]&gt;(new Date()).getTime())};this.setThrottling=function(a,b){_self.throttlingTime[a]=(new Date()).getTime()+Math.abs(b)}};
  </p>
 </body>
</html>