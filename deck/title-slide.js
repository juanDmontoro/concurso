function updateTitleSlideClass(event) {
  const currentSlide =
    event?.currentSlide || document.querySelector(".reveal .slides section.present");

  const isTitleSlide = currentSlide && currentSlide.id === "title-slide";

  document.body.classList.toggle("is-title-slide", isTitleSlide);
}

Reveal.on("ready", updateTitleSlideClass);
Reveal.on("slidechanged", updateTitleSlideClass);
