(function() {
  const BRAND_NAME = "Waytransit Travels & Tourism";

  function initLeadCapture() {
    // 1. Remove any WhatsApp widget or Chaty floating widget if found
    const waWidget = document.getElementById("go-whatsapp-widget");
    if (waWidget) waWidget.remove();
    
    document.querySelectorAll(".chaty-widget, .whatsapp-chat-button, .chaty-in-desktop, .chaty-in-mobile").forEach(function(el) {
      el.remove();
    });

    // 2. Wire Action Buttons to Contact Page
    const buttons = document.querySelectorAll("a, button");
    buttons.forEach(function(btn) {
      const href = btn.getAttribute("href") || "";
      if (href.includes("whatsapp.com") || href.includes("wa.me") || href.startsWith("tel:")) {
        btn.setAttribute("href", "/contact-us/index.html");
        btn.removeAttribute("target");
      }
    });

    // 3. Ensure Hero video plays properly
    const heroVideo = document.querySelector(".elementor-element-f27e79f video, .elementor-background-video-hosted");
    if (heroVideo) {
      heroVideo.muted = true;
      heroVideo.playsInline = true;
      heroVideo.autoplay = true;
      heroVideo.loop = true;
      const playPromise = heroVideo.play();
      if (playPromise !== undefined) {
        playPromise.catch(function(error) {
          // Autoplay was prevented
        });
      }
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initLeadCapture);
  } else {
    initLeadCapture();
  }
})();
