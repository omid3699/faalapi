const server_url = "http://localhost:8000/faal/";
let faal_text = document.getElementById("faal-text");

async function get_faal() {
  const options = { method: "GET" };
  let faal = "";

  await fetch(server_url, options)
    .then((response) => response.json())
    .then((response) => (faal = response["faal"]))
    .catch((err) => console.error(err));

  if (faal != "") {
    faal_text.innerText = faal;
  }    
}
