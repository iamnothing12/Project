<html>
 <body>
  <p>
   MC.Currency=new function(){var a=this;this._params={};this._interface=null;this._interface_handler=null;this._game_width=null;this._game_height=null;this.attempts=0;this.max_attempts=10;this._game_obj=null;this._game_type="none";this._init=function(){var c=document.getElementsByTagName("body").item(0);var b=c.getAttribute("data-platform");if(b===""||b===null){b="external"}a._interface=b.charAt(0).toUpperCase()+b.slice(1).toLowerCase();MC.Modules.include("Currency."+a._interface);if(b!=="external"){if(typeof Currency==="undefined"){window.Currency=a}}};this._initGameObject=function(){if(typeof(getGameInstance)!="undefined"){this._game_obj=getGameInstance();this._game_type="unity"}else{this._game_obj=jQuery("#game-embed");this._game_type="flash";if(this._game_obj==null){this._game_obj=jQuery("#shockwaveGameContainer embed");this._game_type="shockwave";if(this._game_obj.length===0){this._game_obj=null;this._game_type="none"}}}};this._postInit=function(){if(a._game_obj===null){a._initGameObject()}if(a._interface_handler===null){if(typeof a[a._interface]!=="undefined"){a._interface_handler=a[a._interface]}else{if(typeof MC.Currency[a._interface]!=="undefined"){a._interface_handler=MC.Currency[a._interface]}else{MC.console("warn","Currency interface not found")}}}};this.showTopup=function(b){this._postInit();this._interface_handler.showTopup(b)};this._hideWindow=function(c,b){this._postInit();this._interface_handler._hideWindow(c,b)};this.purchaseBundle=function(b){a._postInit();a._interface_handler.purchaseBundle(b)};this.purchaseItem=function(b){this._postInit();this._interface_handler.purchaseItem(b)};this._parseToFloat=function(b){var c=b[0].toString();c=c.replace(/\,/g,"");return parseFloat(c)};this.sizeCurrency=function(){var c=0;jQuery(".credits_amount_price a").each(function(e,d){price=_parseToFloat($(this).text().match(/[0-9]+(?:\,?)[0-9]*\.[0-9]{2}/g));if(price&gt;c){c=price}});var b=1;if(c&gt;9999999){b=0.6}else{if(c&gt;999999){b=0.68}else{if(c&gt;99999){b=0.78}else{if(c&gt;9999){b=0.92}else{if(c&gt;999){b=1}else{if(c&gt;99){b=1.1}else{b=1.2}}}}}}jQuery(".credits_amount_price a").attr("style","font-size: "+b+"em")};this.pollForTransactionCompletion=function(b,d,e,c){start_ts=new Date().getTime();this.interval=setInterval(function(){Currency._checkTransactionStatus(b,d,e,start_ts,c)},5000)};this._checkTransactionStatus=function(b,d,g,e,c){if(!g){g=40}if(this.attempts&gt;g){clearInterval(this.interval);new_location=c+"error=1&amp;reason=MAX_RETRIES";window.location=new_location;return false}var f=this;jQuery.getJSON("/currency/status/?transaction_session_id="+d,function(h){if(!h){}else{switch(h.status){case"COMPLETE":window.location=c+"&amp;tw="+Math.round(((new Date().getTime()-e)/1000));break;default:f.attempts++;break}}})};this.debugParams=function(){return JSON.stringify(this._params)};this.trackBundleStats=function(b,f,d){if(typeof(b)=="undefined"){if(d){setTimeout(redirectPage(d),500)}}var c=0;if(typeof(Currency)!="undefined"&amp;&amp;typeof(Currency._params)!="undefined"&amp;&amp;typeof(Currency._params.source_id)!="undefined"){c=Currency._params.source_id}else{if(typeof(game_data)!="undefined"&amp;&amp;typeof(game_data.game_id)!="undefined"){c=game_data.game_id}else{c=0}}var e="binary/credits/topup/"+b+"/"+f+"/"+c;if(d){setTimeout(redirectPage(d),500)}return false};this._init()};var credits=new function(){this._params={old:true};this.__init=function(a){this._params.game_id=a};this.ShowTopupWindow=function(){Currency.showTopup(this._params)};this.ShowPurchaseOptions=function(){Currency.showTopup(this._params)};this.HideTopupWindow=function(b,a){Currency._hideWindow(b,a)};this.SetWindowType=function(){};this.GetGameId=function(){return this._params.game_id};this.GetGameWidth=function(){return Currency._game_height};this.GetGameHeight=function(){return Currency._game_height};this.GetWindowType=function(){return 1}};
  </p>
 </body>
</html>