document.addEventListener("DOMContentLoaded", function () {
    const container = document.querySelector(".paragrafos");
    const imgTexto = document.querySelector(".img-texto");
    const textoDiv = imgTexto.querySelector(".texto");

    const paragrafos = container.querySelectorAll("p");

    if (paragrafos.length < 2) return;

    let alvo;

    if (paragrafos.length > 7) {
      // pega o -4
      alvo = paragrafos[paragrafos.length - 4];
    } else {
      // pega o -2 (penúltimo)
      alvo = paragrafos[paragrafos.length - 2];
    }

    if (!alvo) return;

    // clona o parágrafo
    const clone = alvo.cloneNode(true);

    // joga dentro da div texto
    textoDiv.appendChild(clone);

    // substitui o <p> pelo bloco com imagem
    alvo.replaceWith(imgTexto);
  });