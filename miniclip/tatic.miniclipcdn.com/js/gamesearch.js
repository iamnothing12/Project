<html>
 <body>
  <p>
   var Sitesearch=function(a,b){this.results=[];this.input=null;this.hook=null;this.overlay=null;this.timeout=null;this.prev_q="";this.search_timeout=300;this.min_chars=1;this.cache={};this.props={overlay:"search-results-overlay box",row_prefix:"sr-row-"};this.input=$(a);if(this.input.length===0){throw ('Input "'+a+'" not found!')}this.hook=$(b);if(this.hook.length===0){throw ('Input "'+b+'" not found!')}this.input.focus($.proxy(function(d){if(this.input.val()&amp;&amp;!this.overlayExists()){this.search()}},this));var c=this;this.input.blur($.proxy(function(){setTimeout(function(){c.destroyOverlay()},500)},this));this.input.keydown($.proxy(function(d){if(d.keyCode===38||d.keyCode===40){d.preventDefault()}this.handleOnKeyDown(d)},this));this.input.keyup($.proxy(function(d){this.handleOnKeyUp(d)},this));this.overlayExists=function(){return(this.overlay!==null)};this.showOverlay=function(){if(this.overlayExists()){this.clearOverlay()}else{this.overlay=$("
  </p>
  <div>
  </div>
  ").addClass(this.props.overlay);$("body").append(this.overlay);this.overlay.attr("id","search-suggestions");var d=this.hook.offset();this.overlay.css("top",d.top+this.hook.outerHeight());this.overlay.css("left",d.left)}};this.destroyOverlay=function(){if(this.overlayExists()){this.input.removeClass("search-active");this.overlay.remove();this.overlay=null;$("#game-container").stop().animate({"margin-top":0},250)}};this.clearOverlay=function(){if(this.overlayExists()){this.overlay.html("")}};this.populateOverlay=function(){this.showOverlay();this.clearOverlay();this.input.addClass("search-active");var d=$("
  <ul>
  </ul>
  ");if(this.input.val().toLowerCase().indexOf("free")&gt;=0){d.append('
  <li class="free-games">
   '+translate.search_free_games+"
  </li>
  ")}$(this.results).each($.proxy(function(h,f){if(f.is_more_button!==true){var e=$("
  <li>
  </li>
  ");e.addClass(f.type);if(f.highlighted===true){e.addClass("selected")}e.attr("id",this.props.row_prefix+f.site_id);e.data("url",f.link+"#t-sd");var g=$("
  <img/>
  ");if(f.type==="game"){g=f.icon}else{g.attr("src",f.icon);g.addClass("avatar")}e.append(g);e.append('
  <span class="name">
   '+f.name+"
  </span>
  ");var j="";if(f.type==="game"){j=f.short_description?f.short_description:f.description?f.description:""}else{if(f.type==="player"){var k='
  <img class="country-flag" src="/content/images/dynamic/flag_'+f.country_code.toLowerCase()+'_15.png" title="'+f.country_name+'"/>
  ';j=k+f.country_name}else{j=f.type.charAt(0).toUpperCase()+f.type.slice(1)}}e.append('
  <span class="description">
   '+j+"
  </span>
  ");e.on("mouseover",$.proxy(function(i){this.overlay.find("li").removeClass("selected");$("#"+i.currentTarget.id).addClass("selected")},this));e.on("mousedown",$.proxy(function(i){if(f.is_more_button){this.hook.submit();return false}},this));e.on("click",function(l){var i=$(this).data("url");window.location.href=i});d.append(e)}},this));this.overlay.append(d);if(this.input.val().length&gt;0){this.overlay.append('
  <a class="button neutral greedy" href="/games/search/en/?query='+encodeURIComponent(this.input.val().toLowerCase())+'">
   '+translate.show_more_results+"
  </a>
  ")}else{this.overlay.append('
  <a class="button neutral greed" href="/games/search/en/">
   '+translate.show_more_results+"
  </a>
  ")}};this.showNoResultsOverlay=function(){this.clearOverlay();var d=$("
  <div>
  </div>
  ").addClass("no_results").html("Nothing found");this.overlay.append(d)};this.handleOnKeyDown=function(d){if(d.keyCode==13){return this.handleReturn(d)}};this.handleOnKeyUp=function(d){if(this.input.val().toLowerCase()!==this.prev_q){this.prev_q=this.input.val().toLowerCase();clearTimeout(this.timeout);var e=this;this.timeout=setTimeout(function(){e.search()},this.search_timeout);return}if(d.keyCode==38){return this.handleArrowUp(d)}else{if(d.keyCode==27){return this.destroyOverlay()}else{if(d.keyCode==40){return this.handleArrowDown(d)}else{if(d.keyCode==13){return this.handleReturn(d)}}}}};this.handleArrowDown=function(f){f.preventDefault();if(this.results.length&gt;1){var e=this.overlay.find("li.selected");e.removeClass("selected");var d=e.next("li");if(d.length){d.addClass("selected")}else{this.overlay.find("li:first").addClass("selected")}}return false};this.handleArrowUp=function(f){f.preventDefault();if(this.results.length&gt;1){var e=this.overlay.find("li.selected");e.removeClass("selected");var d=e.prev("li");if(d.length){d.addClass("selected")}else{this.overlay.find("li:last").addClass("selected")}}return false};this.handleReturn=function(f){$(f.target.form).submit(function(g){return true});var e=this.overlay.find("li.selected");if(e.length){var d=e.data("url");window.location.href=d}};this.addResults=function(d,e){this.results=[];$(d.result).each($.proxy(function(f,g){this.results.push(g)},this));this.results.push({_id:"more",is_more_button:true,highlighted:false});this.cache[e]=this.results;this.populateOverlay()};this.search=function(){var f=this.input.val().toLowerCase();if(f.length
  <this.min_chars>
   ololololololololololololo
   <br/>
   lolololololololol",highlighted:true,icon:'
   <span class="icon-wrap">
    <img alt="trololol" data-track="trololol" height="57" src="/images/trololol.png" title="trololol" width="68"/>
   </span>
   ',link:"",site_id:0,type:"game"}]},f)}else{var d="/games/ajax/gamesearch/";var e={query:f};$.ajax({url:d,data:e,dataType:"json",type:"GET",success:$.proxy(function(g){if(g.success&amp;&amp;g.result.length){this.addResults(g,f)}else{this.cache[f]=false;this.showNoResultsOverlay()}},this),error:function(g){console.log("error",g)}})}}};$(function(){if($(".search-query").length&gt;=1&amp;&amp;!$("body").hasClass("game-header")){new Sitesearch(".search-query",".search-form")}});
  </this.min_chars>
 </body>
</html>