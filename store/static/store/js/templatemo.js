
'use strict';
$(document).ready(function() {

    // Accordion
    var all_panels = $('.templatemo-accordion > li > ul').hide();

    $('.templatemo-accordion > li > a').click(function() {
        console.log('Hello world!');
        var target =  $(this).next();
        if(!target.hasClass('active')){
            all_panels.removeClass('active').slideUp();
            target.addClass('active').slideDown();
        }
      return false;
    });

    $('#contactForm .close').click(function(){
        $('#contactForm').fadeOut();
        $('#contactIcon').fadeIn();
        $("body").removeClass('open')
    });
    
    // Show form when icon is clicked
    $('#contactIcon').click(function(){
        $(this).fadeOut();
        $('#contactForm').fadeIn();
        $('body').addClass('open')
    });
    // Product detail
    $('.product-links-wap .col-4').mouseenter(function(){
      var this_src = $(this).children('img').attr('src');
      // Remove the borderMe class from all images
      $('.product-links-wap img').removeClass('borderMe');
      
      // Get the source of the clicked image
      var this_src = $(this).children('img').attr('src');
      
      // Set the source of the #product-detail img
      $('#product-detail').attr('src', this_src);
      
      // Add the borderMe class to the clicked image
      $(this).children('img').addClass('borderMe');
      return false;
    });
    
    // End roduct detail

});
