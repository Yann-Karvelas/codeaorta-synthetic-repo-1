// Finding 5: Insecure HTTP
fetch('http://api.example.com/data')
  .then(res => res.json())
  .then(data => console.log(data));

// Finding 6: console.log in production
function debug(msg) {
  console.log('DEBUG:', msg);
}
