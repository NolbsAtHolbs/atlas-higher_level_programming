#!/usr/bin/node
$(document).ready(() => {
  $('DIV#toggle_header').click(() => {
    if ($('header').hasClass('green')) {
      $('header').addClass('red');
      $('header').removeClass('green');
    } else if ($('header').hasClass('red')) {
      $('header').addClass('green');
      $('header').removeClass('red');
    }
  });
});
