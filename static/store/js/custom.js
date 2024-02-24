$(window).on('load', function() {
  var windowHeight = $(window).height();
  var windowScrollTop = $(window).scrollTop();

  $('.item').each(function() {
    var offsetTop = $(this).offset().top;
    if (offsetTop < windowHeight + windowScrollTop - 100) {
      $(this).addClass('show');
    }
  });
  
  $('.item').each(function() {
    var offsetTop = $(this).offset().top;
    if (offsetTop < windowHeight + windowScrollTop) {
      var spinner = $(this).find('.overlay-spinner');
      var spinner1 = $(this).find('.overlay-spinner1');
      setTimeout(function() {
        spinner.hide();
        spinner1.hide();
      }, 1000); // Change the delay time here (in milliseconds)
    }
  });

  $(window).scroll(function() {
    windowHeight = $(window).height();
    windowScrollTop = $(window).scrollTop();

    $('.item').each(function() {
      var offsetTop = $(this).offset().top;
      if (offsetTop < windowHeight + windowScrollTop - 100) {
        $(this).addClass('show');
      }
    });

    $('.item').each(function() {
      var offsetTop = $(this).offset().top;
      if (offsetTop < windowHeight + windowScrollTop) {
        var spinner = $(this).find('.overlay-spinner');
        var spinner1 = $(this).find('.overlay-spinner1');
        setTimeout(function() {
          spinner.hide();
          spinner1.hide();
        }, 1000); // Change the delay time here (in milliseconds)
      }
    });
  });
});
