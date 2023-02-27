function onLoad() {
  const sidebarIcon = document.getElementById("nav-icon");
  const sidebar = document.getElementById("slim-nav");

  sidebarIcon.addEventListener("click", () => {
    console.log("clicked", sidebar);
    sidebar.classList.toggle("hidden");
  });
}

document.addEventListener("DOMContentLoaded", onLoad, false);
