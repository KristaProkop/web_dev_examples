
   (function() {
    function $Dojo(element){
        element = document.getElementById(element)
        this.element = element
        console.log(this)
        return this
    }

    $Dojo.prototype.click = function(callback) {
        this.element.addEventListener("click", clickFunction);
        function clickFunction() {
            callback();
        }
    }

    $Dojo.prototype.hover = function(inEvent, outEvent) {

        this.element.addEventListener("mouseover", hoverOn);

        if (outEvent != undefined) {
            this.element.addEventListener("mouseout", hoverOff);
        }
        function hoverOn() {
            inEvent();
        }
        function hoverOff() {
            outEvent();
        }
    }
})(); 
