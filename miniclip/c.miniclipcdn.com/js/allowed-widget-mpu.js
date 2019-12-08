<html>
 <body>
  <p>
   var AllowedWidgetMpu = new function() {
    this.init = () =&gt; {
        if (document.querySelector('#customAdvert') == null) {
            let mpu_length = document.querySelectorAll(".widget-mpu").length;
            let widget = document.querySelectorAll(".widget-mpu");
            for (let i = 0; i &lt; mpu_length; i++) {
                widget[i].nextElementSibling.style.display = "block";

            }
        }
    }
};

$(document).ready(function() {
    AllowedWidgetMpu.init();
})
  </p>
 </body>
</html>