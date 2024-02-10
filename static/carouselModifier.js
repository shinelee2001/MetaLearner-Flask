let slideIndex = 0;
showSlide(slideIndex);

function nextSlide() {
    showSlide((slideIndex += 1));
}

function prevSlide() {
    showSlide((slideIndex -= 1));
}

function showSlide(n) {
    const slides = document.querySelectorAll('.slide');
    if (n >= slides.length) {
        slideIndex = 0;
    }
    if (n < 0) {
        slideIndex = slides.length - 1;
    }
    slides.forEach((slide) => {
        slide.style.display = 'none';
    });
    slides[slideIndex].style.display = 'block';
}
