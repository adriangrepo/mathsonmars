
$(document).ready(function(){
    $("#myCarousel").carousel({interval: false});
    $("#petCarousel").carousel({interval: false});
    
    // Enable Carousel Controls for chrome
    $(".left").click(function(){
        $("#myCarousel").carousel("prev");
    });
    $(".right").click(function(){
        $("#myCarousel").carousel("next");
    });
});

