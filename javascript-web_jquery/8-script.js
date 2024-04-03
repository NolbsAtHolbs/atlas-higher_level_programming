#!/usr/bin/node
$(document).ready(() => {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
    const movieList = $('<ul id="list_movies"></ul>');
    data.results.forEach(movie => {
      movieList.append(`<li>${movie.title}</li>`);
    });
    $('body').append(movieList);
  });
});
