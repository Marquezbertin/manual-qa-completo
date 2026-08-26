// Language switcher: toggles between the PT and EN versions of the current module.
(function () {
  function init() {
    var path = window.location.pathname;
    var m = path.match(/\/(\d{2})\/(PT|EN)\//);
    if (!m) return; // only on module pages (not home)

    var num = m[1];
    var lang = m[2];
    var other = lang === "PT" ? "EN" : "PT";
    var alt = path.replace(
      "/" + num + "/" + lang + "/",
      "/" + num + "/" + other + "/"
    );

    var options = document.querySelector(".md-header__options");
    if (!options) return;

    var wrap = document.createElement("div");
    wrap.className = "lang-switch";
    wrap.setAttribute("role", "group");
    wrap.setAttribute("aria-label", "Idioma");

    ["PT", "EN"].forEach(function (l) {
      var a = document.createElement("a");
      a.textContent = l;
      a.className = "lang-switch__item" + (l === lang ? " is-active" : "");
      a.href = l === lang ? path : alt;
      a.setAttribute("title", l === lang ? "Versão atual" : "Ver em " + l);
      wrap.appendChild(a);
    });

    options.insertBefore(wrap, options.firstChild);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
