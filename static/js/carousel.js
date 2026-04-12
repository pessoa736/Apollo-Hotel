const track = document.getElementById("sliderTrack");
const slides = document.querySelectorAll(".slide");
const nextBtn = document.getElementById("next");
const prevBtn = document.getElementById("prev");
const dotsContainer = document.getElementById("dots");

let index = 0;
let autoPlayInterval;
let startX = 0;
let endX = 0;

/* ---------- criar dots ---------- */
slides.forEach((_, i) => {
  const dot = document.createElement("div");
  dot.classList.add("dot");
  if (i === 0) dot.classList.add("active");
  dot.addEventListener("click", () => {
    index = i;
    updateSlider();
    resetAutoplay();
  });
  dotsContainer.appendChild(dot);
});

function updateDots() {
  document
    .querySelectorAll(".dot")
    .forEach((dot) => dot.classList.remove("active"));
  document.querySelectorAll(".dot")[index].classList.add("active");
}

function updateSlider() {
  const width = slides[0].clientWidth;
  track.style.transform = `translateX(-${index * width}px)`;
  updateDots();
}

/* ---------- botões ---------- */
nextBtn.onclick = () => {
  nextSlide();
  resetAutoplay();
};
prevBtn.onclick = () => {
  prevSlide();
  resetAutoplay();
};

function nextSlide() {
  index = (index + 1) % slides.length;
  updateSlider();
}

function prevSlide() {
  index = (index - 1 + slides.length) % slides.length;
  updateSlider();
}

/* ---------- AUTOPLAY ---------- */
function startAutoplay() {
  autoPlayInterval = setInterval(nextSlide, 4000);
}
function resetAutoplay() {
  clearInterval(autoPlayInterval);
  startAutoplay();
}
startAutoplay();

/* pausa ao passar mouse */
track.addEventListener("mouseenter", () => clearInterval(autoPlayInterval));
track.addEventListener("mouseleave", startAutoplay);

/* ---------- SWIPE MOBILE ---------- */
track.addEventListener("touchstart", (e) => {
  startX = e.touches[0].clientX;
});

track.addEventListener("touchend", (e) => {
  endX = e.changedTouches[0].clientX;
  handleSwipe();
});

function handleSwipe() {
  if (startX - endX > 50) nextSlide();
  if (endX - startX > 50) prevSlide();
  resetAutoplay();
}

/* resize */
window.addEventListener("resize", updateSlider);