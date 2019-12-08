<html>
 <body>
  <p>
   var Modal=new function(){var a=this;var b={};this.eventMethodAdd=window.addEventListener?"addEventListener":"attachEvent";this.eventMethodRemove=window.removeEventListener?"removeEventListener":"detachEvent";this.eventMessage=!window.addEventListener||!window.removeEventListener?"onmessage":"message";this.modal=$("
  </p>
  <div>
  </div>
  ").addClass("mc-modal");this.modalDialog=$("
  <div>
  </div>
  ").addClass("mc-modal-dialog");this.modalContent=$("
  <div>
  </div>
  ").addClass("mc-modal-content");this.modalHeader=$("
  <div>
  </div>
  ").addClass("mc-modal-header");this.modalBody=$("
  <div>
  </div>
  ").addClass("mc-modal-body");this.modalClose=$("
  <span>
  </span>
  ").addClass("mc-close");this.modalCallback=null;this.frameHeight=0;this.domain;this.validOriginThrottleMsg=502;this.close_button=true;this.init=function(){a.actions()};this.actions=function(){$(window).on("resize",function(){a.resize(a.frameHeight)});$(document.body).on("click",".mc-modal .mc-close",function(){a.close(true);return false})};this.getDomain=function(){if(typeof a.domain!=="undefined"){return a.domain}var c=document.getElementsByTagName("script");var d="//static.miniclipcdn.com";if(c&amp;&amp;c.length&gt;0){for(var f in c){if(c[f].src&amp;&amp;c[f].src.match(/\/js\/mc\.js/)){var e=c[f].src.replace(/https?:\/\/(.+)\/js\/mc\.js.*$/,"$1");var g=e.split(".");if(g.length&gt;3){g.shift()}return"//"+g.join(".")}}}return d};this.isValidUrl=function(c){if((c.toLowerCase().startsWith("//"))){c="https:"+c}let isValidUrl=a.isValidJSURL(c);let isUrl=a.isValidPattern(c);let sameDomain=c.toLowerCase().startsWith("/")&amp;&amp;!c.substr(1).toLowerCase().startsWith("/");return((isValidUrl&amp;&amp;isUrl)||sameDomain)};this.isValidPattern=function(c){let expression=/^((?:http(?:s)?\:\/\/)?[a-zA-Z0-9_-]+(?:.[a-zA-Z0-9_-]+)*.[a-zA-Z]{2,4}(?:\/[a-zA-Z0-9_]+)*(?:\/[a-zA-Z0-9_]+.[a-zA-Z]{2,4}(?:\?[a-zA-Z0-9_]+\=[a-zA-Z0-9_]+)?)?(?:\&amp;[a-zA-Z0-9_]+\=[a-zA-Z0-9_]+)*)$/gi;let regex=new RegExp(expression);let urlNoQueryString=c.split("?")[0];return(c!=null&amp;&amp;!(urlNoQueryString.match(regex)===null||(c.split(" ").length-1)&gt;0))};this.isValidJSURL=function(c){if(!(c.toLowerCase().startsWith("http://")||c.toLowerCase().startsWith("https://"))){c="https://"+c}let toOpenUrl;try{toOpenUrl=new URL(c);return toOpenUrl.origin!=="null"}catch(d){}return false};this.open=function(c){if(typeof c==="undefined"||c===null||c.constructor!==Object){throw"Incorrect data format for modal"}this.modalDialog.removeClass("mc-modal-borderless");this.modalContent.removeClass("mc-modal-borderless");if(typeof c.close_button!=="undefined"&amp;&amp;c.close_button==false){this.close_button=false}if(typeof c.borderless!=="undefined"&amp;&amp;c.borderless==true){this.modalDialog.addClass("mc-modal-borderless");this.modalContent.addClass("mc-modal-borderless")}switch(c.type){case"url":let openData=null;if(c.src!==undefined){openData=decodeURIComponent(c.src.split("@")[0])}if(openData===null||!this.isValidUrl(openData)){a.close(true);console.log("Incorrect data format for modal");throw"Incorrect data format for modal"}a.url(openData);break;case"content":a.content(c.html);break;default:throw"Modal type not set"}a.header(c.header||null);if("action" in c){b[c.action]=c.callback||null}a.callback(c.callback||null);a.build()};this.close=function(c){a.listenerRemove();if(typeof a.modalCallback==="function"){a.modalCallback(c===true)}a.modalCallback=null;$(".mc-modal").remove();return false};this.header=function(c){a.modalHeader.html("");if(typeof c==="string"){a.modalHeader.html('
  <h1 class="title">
   '+c+"
  </h1>
  ")}};this.callback=function(c){a.modalCallback=typeof c==="function"?c:null};this.url=function(d){var c=$("
  <iframe>
  </iframe>
  ").addClass("mc-modal-iframe").attr({hidden:true,frameBorder:0,src:d});c.on("load",function(){$(".mc-modal-loading").remove();c.show()});a.loading();a.listenerAdd();a.modalBody.append(c)};this.content=function(c){a.modalBody.empty().append(c)};this.loading=function(){var c=$("
  <div>
  </div>
  ").addClass("mc-modal-loading").html('
  <img alt="Loading" src="'+a.getDomain()+'/images/loading/waiting64.gif"/>
  ');a.modalBody.html(c)};this.build=function(){if(a.close_button==true){a.modalHeader.append(a.modalClose.html('
  <a href="#">
   ×
  </a>
  '))}a.modalContent.append(a.modalHeader).append(a.modalBody);a.modalDialog.append(a.modalContent);a.modal.append(a.modalDialog);$("body").append(a.modal)};this.listenerAdd=function(){if(a.eventMethodAdd==="attachEvent"){window[a.eventMethodAdd](a.eventMessage,a.listener,false)}else{window[a.eventMethodAdd](a.eventMessage,a.listener)}};this.listenerRemove=function(){if(a.eventMethodRemove==="detachEvent"){window[a.eventMethodRemove](a.eventMessage,a.listener,false)}else{window[a.eventMethodRemove](a.eventMessage,a.listener)}};this.listener=function(f){var l={},c=false,i=false,k=false;try{l=JSON.parse(f.data);c=typeof l.miniclip!=="undefined"&amp;&amp;l.miniclip===true;i=typeof l.modal!=="undefined"&amp;&amp;l.modal===true;k=typeof l.close!=="undefined"&amp;&amp;l.close===true}catch(h){}if(c!==true||i!==true){return}var g=typeof l.data!=="undefined"?l.data:{};var d=typeof g.action!=="undefined"?a.stripTagsResponse(g.action):null;var j=typeof g.parameters!=="undefined"?g.parameters:{};let actions={action:d,parameters:j,close:k};if(f.origin.endsWith(".miniclip.com")){a.listenerActions(actions)}else{a.validateContentOrigin(f.origin,actions)}};this.listenerActions=function(c){if(typeof a[c.action]==="function"){a[c.action](c.parameters)}if(typeof b[c.action]==="function"){b[c.action](c.parameters)}if(c.close===true){b[c.action]=null;a.close()}};this.stripTagsResponse=function(c){let regex=/(]+)&gt;)/ig;let responseStripped=c.replace(regex,"");if(responseStripped.indexOf("&gt;")!==-1){return""}return responseStripped};this.validateContentOrigin=function(c,d){if(typeof Throttleable==="undefined"||Throttleable.isThrottled(a.validOriginThrottleMsg)){return false}$.ajax({url:"/ajax/valid-origin",dataType:"json",type:"POST",data:{origin:c,appId:MC.appId},success:function(e){if(e.error_code!==undefined){Throttleable.setThrottling(a.validOriginThrottleMsg,e.msg)}if(!e.msg){a.modalBody.html(e.data);d.parameters=e.data;return}a.listenerActions(d)},error:function(e){console.log("Error"+event.data,e)}})};this.resize=function(c){var e=$(".mc-modal-iframe");var g=e.position()||{};var h=window.innerHeight||document.documentElement.clientHeight;var d=h-((g.top||0)+$(".mc-modal-header").outerHeight(true));var f=100;a.frameHeight=c;if(!isNaN(c)&amp;&amp;c&lt;=d){f=c}else{if(!isNaN(c)&amp;&amp;c&gt;d){f=d}}e.height(f)}};$(document).ready(function(){Modal.init()});
 </body>
</html>