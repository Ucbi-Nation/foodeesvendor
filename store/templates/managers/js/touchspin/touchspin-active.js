(function ($) {
 "use strict";



	$(".touchspin2").TouchSpin({
		min: 0,
		max: 10000,
		step: 10,
		decimals: 1,
		boostat: 20,
		maxboostedstep: 1000,
		postfix: '%',
		buttondown_class: 'btn btn-white',
		buttonup_class: 'btn btn-white'
	});







})(jQuery);