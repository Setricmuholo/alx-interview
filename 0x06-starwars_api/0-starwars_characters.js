#!/usr/bin/node

const request = require('request');

function getMovieCharacters(movieId) {
  const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(filmUrl, (error, response, filmBody) => {
    if (error) {
      console.error(`Error fetching movie data: ${error}`);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Error: Unable to retrieve data for movie ID ${movieId}`);
      return;
    }

    const filmData = JSON.parse(filmBody);
    const characters = filmData.characters;

    console.log(`Characters from ${filmData.title} (Episode ${filmData.episode_id}):`);
    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, characterBody) => {
        if (error) {
          console.error(`Error fetching character data: ${error}`);
          return;
        }

        if (response.statusCode === 200) {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        } else {
          console.error(`Error: Unable to retrieve character data from ${characterUrl}`);
        }
      });
    });
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node star_wars_characters_request.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
