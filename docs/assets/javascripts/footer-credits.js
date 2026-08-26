// Injects a branded credit bar at the top of the site footer.
(function () {
  function init() {
    var footer = document.querySelector(".md-footer");
    if (!footer || document.querySelector(".qa-footer-extra")) return;

    var bar = document.createElement("div");
    bar.className = "qa-footer-extra";
    bar.innerHTML =
      '<div class="qa-footer-extra__inner">' +
      '<span>Autor: <strong>Bruno Bertin Marquez</strong></span>' +
      '<span class="qa-sep">|</span>' +
      '<span>Certificações: <strong>ASTFC-AICS</strong> · <strong>SCRUM</strong></span>' +
      '<span class="qa-sep">|</span>' +
      '<a href="https://github.com/Marquezbertin" target="_blank" rel="noopener">GitHub: @Marquezbertin</a>' +
      "</div>";

    footer.insertBefore(bar, footer.firstChild);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
