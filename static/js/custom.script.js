const sort = document.getElementById('sort');
const param = new URLSearchParams(window.location.search).get("q");
if(param == null) {
  sort.textContent = "All";
}
else if(param != null)
{
  sort.textContent = String(param).charAt(0).toUpperCase() + String(param).slice(1);
}
else
{
  sort.textContent = "Default"
}

function openLink(e)
{
  window.open(e['href']);
}