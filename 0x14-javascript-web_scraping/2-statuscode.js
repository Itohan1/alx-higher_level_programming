#!/usr/bin/node
//

const apiRequest = () => {
  const url = process.argv[2];
  fetch(url)
    .then((response) => Promise.all([response.status, response.json()]))
    .then(([status, data]) => console.log({ status, data }));
};
