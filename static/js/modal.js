var modal = document.getElementById("modal");
var btn = document.getElementById("openModal");
var span = document.getElementsByClassName("close")[0];

// Abre o modal :D
btn.onclick = function(e) {
  e.preventDefault(); // O link nao redireciona
  modal.style.display = "flex";
}

// Fechar no X
span.onclick = function() {
  modal.style.display = "none";
}

// Fechar clicando fora
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
