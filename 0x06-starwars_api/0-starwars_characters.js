const request = require('request');


if (process.argv.length === 2) {
    movieId = process.argv[2];
  }
  else {
    throw new Error("MovieId must be passed to CMD")
  }

  const BASE_ENDPOINT = `https://swapi-api.alx-tools.com/api/films/${movieId}`
  const CHARACTER_ENDPOINT = "https://swapi-api.alx-tools.com/api/people/"

  try {
    request(BASE_ENDPOINT, (error, response, body) => {
        if (error) {
            throw new Error("Invalid request")
        }
        else if (response.statusCode != 200) {
            throw new Error("Resource is prohibited")
        }
        const result = JSON.parse(body)
        console.log(result)

        for (let i = 1; i <= result['characters']; i++) {
            request(CHARACTER_ENDPOINT + i, (error, response, body) => {
                if (error) {
                    console.log(error)
                }
                if (response.statusCode == 200) {
                    const secondResult = JSON.parse(body)
                    console.log(secondResult['name'])

                }
            })
        }

    });
}
catch (error) {
    console.log(error)
}

