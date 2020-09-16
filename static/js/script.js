

function changeBg1(c1, c2) {
   
  $('span.bg1').css({
    background: '-moz-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-o-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-webkit-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-ms-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: 'linear-gradient(135deg, ' + c1 + ',' + c2 + ')'
  });
}

$slider1 = $('.slider1');

$slider1.slick({
  arrows: false,
  dots: true,
  infinite: true,
  speed: 600,
  fade: true,
  focusOnSelect: true, 
  customPaging: function(slider, i) {
    var color = $(slider.$slides[i]).data('color').split(',')[1];
    return '<a><svg width="100%" height="100%" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6.215" stroke="' + color + '"></circle></svg><span style="background:' + color + '"></span></a>';
  }
}).on('beforeChange', function(event, slick, currentSlide, nextSlide) {
  colors = $('figure', $slider1).eq(nextSlide).data('color').split(',');
  color1 = colors[0];
  color2 = colors[1];
  color3 = colors[2];
  color4 = colors[3];
  color5 = colors[4];
  
  
  if (color4 = "first" ){
  $('.price, .btn1').css({
    color: color1 
	});
 $('.price').text(color3);
  changeBg1(color1, color2);
  $('.btn1').css({
    borderColor: color2 
  }); 
  }
}); 


 
 
function changeBg2(c1, c2) {
   
  $('span.bg2').css({
    background: '-moz-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-o-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-webkit-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-ms-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: 'linear-gradient(135deg, ' + c1 + ',' + c2 + ')'
  });
}

$slider2 = $('.slider2');

$slider2.slick({
  arrows: false,
  dots: true,
  infinite: true,
  speed: 600,
  fade: true,
  focusOnSelect: true, 
  customPaging: function(slider, i) {
    var color = $(slider.$slides[i]).data('color').split(',')[1];
    return '<a><svg width="100%" height="100%" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6.215" stroke="' + color + '"></circle></svg><span style="background:' + color + '"></span></a>';
  }
}).on('beforeChange', function(event, slick, currentSlide, nextSlide) {
  colors = $('figure', $slider2).eq(nextSlide).data('color').split(',');
  color1 = colors[0];
  color2 = colors[1];
  color3 = colors[2];
  color4 = colors[3];
  
  
  if (color4 = "second" ){
  $('.price22, .btn2').css({
    color: color1 
	});
 $('.price22').text(color3);

  changeBg2(color1, color2);
  $('.btn2').css({
    borderColor: color2 
  }); }
}); 





function changeBg3(c1, c2) {
   
  $('span.bg3').css({
    background: '-moz-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-o-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-webkit-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-ms-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: 'linear-gradient(135deg, ' + c1 + ',' + c2 + ')'
  });
}

$slider3 = $('.slider3');

$slider3.slick({
  arrows: false,
  dots: true,
  infinite: true,
  speed: 600,
  fade: true,
  focusOnSelect: true, 
  customPaging: function(slider, i) {
    var color = $(slider.$slides[i]).data('color').split(',')[1];
    return '<a><svg width="100%" height="100%" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6.215" stroke="' + color + '"></circle></svg><span style="background:' + color + '"></span></a>';
  }
}).on('beforeChange', function(event, slick, currentSlide, nextSlide) {
  colors = $('figure', $slider3).eq(nextSlide).data('color').split(',');
  color1 = colors[0];
  color2 = colors[1];
  color3 = colors[2];
  color4 = colors[3];
  
  
  if (color4 = "third" ){
  $('.price33, .btn3').css({
    color: color1 
	});
 $('.price33').text(color3);

  changeBg3(color1, color2);
  $('.btn3').css({
    borderColor: color2 
  }); }
}); 




function changeBg4(c1, c2) {
   
  $('span.bg4').css({
    background: '-moz-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-o-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-webkit-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-ms-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: 'linear-gradient(135deg, ' + c1 + ',' + c2 + ')'
  });
}

$slider4 = $('.slider4');

$slider4.slick({
  arrows: false,
  dots: true,
  infinite: true,
  speed: 600,
  fade: true,
  focusOnSelect: true, 
  customPaging: function(slider, i) {
    var color = $(slider.$slides[i]).data('color').split(',')[1];
    return '<a><svg width="100%" height="100%" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6.215" stroke="' + color + '"></circle></svg><span style="background:' + color + '"></span></a>';
  }
}).on('beforeChange', function(event, slick, currentSlide, nextSlide) {
  colors = $('figure', $slider4).eq(nextSlide).data('color').split(',');
  color1 = colors[0];
  color2 = colors[1];
  color3 = colors[2];
  color4 = colors[3];
  
  
  if (color4 = "fourth" ){
  $('.price44, .btn4').css({
    color: color1 
	});
 $('.price44').text(color3);

  changeBg4(color1, color2);
  $('.btn4').css({
    borderColor: color2 
  }); }
}); 

function changeBg5(c1, c2) {
   
  $('span.bg5').css({
    background: '-moz-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-o-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-webkit-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-ms-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: 'linear-gradient(135deg, ' + c1 + ',' + c2 + ')'
  });
}

$slider5 = $('.slider5');

$slider5.slick({
  arrows: false,
  dots: true,
  infinite: true,
  speed: 600,
  fade: true,
  focusOnSelect: true, 
  customPaging: function(slider, i) {
    var color = $(slider.$slides[i]).data('color').split(',')[1];
    return '<a><svg width="100%" height="100%" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6.215" stroke="' + color + '"></circle></svg><span style="background:' + color + '"></span></a>';
  }
}).on('beforeChange', function(event, slick, currentSlide, nextSlide) {
  colors = $('figure', $slider5).eq(nextSlide).data('color').split(',');
  color1 = colors[0];
  color2 = colors[1];
  color3 = colors[2];
  color4 = colors[3];
  
  
  if (color4 = "fifth" ){
  $('.price55, .btn5').css({
    color: color1 
	});
 $('.price55').text(color3);

  changeBg5(color1, color2);
  $('.btn5').css({
    borderColor: color2 
  }); }
}); 

function changeBg6(c1, c2) {
   
  $('span.bg6').css({
    background: '-moz-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-o-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-webkit-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-ms-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: 'linear-gradient(135deg, ' + c1 + ',' + c2 + ')'
  });
}

$slider6 = $('.slider6');

$slider6.slick({
  arrows: false,
  dots: true,
  infinite: true,
  speed: 600,
  fade: true,
  focusOnSelect: true, 
  customPaging: function(slider, i) {
    var color = $(slider.$slides[i]).data('color').split(',')[1];
    return '<a><svg width="100%" height="100%" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6.215" stroke="' + color + '"></circle></svg><span style="background:' + color + '"></span></a>';
  }
}).on('beforeChange', function(event, slick, currentSlide, nextSlide) {
  colors = $('figure', $slider6).eq(nextSlide).data('color').split(',');
  color1 = colors[0];
  color2 = colors[1];
  color3 = colors[2];
  color4 = colors[3];
  
  
  if (color4 = "sixth" ){
  $('.price66, .btn6').css({
    color: color1 
	});
 $('.price66').text(color3);

  changeBg6(color1, color2);
  $('.btn6').css({
    borderColor: color2 
  }); }
});


function changeBg7(c1, c2) {

  $('span.bg7').css({
    background: '-moz-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-o-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-webkit-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-ms-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: 'linear-gradient(135deg, ' + c1 + ',' + c2 + ')'
  });
}

$slider7 = $('.slider7');

$slider7.slick({
  arrows: false,
  dots: true,
  infinite: true,
  speed: 600,
  fade: true,
  focusOnSelect: true,
  customPaging: function(slider, i) {
    var color = $(slider.$slides[i]).data('color').split(',')[1];
    return '<a><svg width="100%" height="100%" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6.215" stroke="' + color + '"></circle></svg><span style="background:' + color + '"></span></a>';
  }
}).on('beforeChange', function(event, slick, currentSlide, nextSlide) {
  colors = $('figure', $slider7).eq(nextSlide).data('color').split(',');
  color1 = colors[0];
  color2 = colors[1];
  color3 = colors[2];
  color4 = colors[3];


  if (color4 = "seventh" ){
  $('.price77, .btn7').css({
    color: color1
	});
 $('.price77').text(color3);

  changeBg7(color1, color2);
  $('.btn7').css({
    borderColor: color2
  }); }
});


function changeBg8(c1, c2) {

  $('span.bg8').css({
    background: '-moz-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-o-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-webkit-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: '-ms-linear-gradient(135deg, ' + c1 + ', ' + c2 + ')',
    background: 'linear-gradient(135deg, ' + c1 + ',' + c2 + ')'
  });
}

$slider8 = $('.slider8');

$slider8.slick({
  arrows: false,
  dots: true,
  infinite: true,
  speed: 600,
  fade: true,
  focusOnSelect: true,
  customPaging: function(slider, i) {
    var color = $(slider.$slides[i]).data('color').split(',')[1];
    return '<a><svg width="100%" height="100%" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6.215" stroke="' + color + '"></circle></svg><span style="background:' + color + '"></span></a>';
  }
}).on('beforeChange', function(event, slick, currentSlide, nextSlide) {
  colors = $('figure', $slider8).eq(nextSlide).data('color').split(',');
  color1 = colors[0];
  color2 = colors[1];
  color3 = colors[2];
  color4 = colors[3];


  if (color4 = "eight" ){
  $('.price88, .btn8').css({
    color: color1
	});
 $('.price88').text(color3);

  changeBg8(color1, color2);
  $('.btn8').css({
    borderColor: color2
  }); }
});


