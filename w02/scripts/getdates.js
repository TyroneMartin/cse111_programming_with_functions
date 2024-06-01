// getdates.js
document.addEventListener("DOMContentLoaded", function() {
    // Copyright Year
    const copyrightYear = new Date().getFullYear();
    document.querySelector('footer p:first-of-type').textContent += copyrightYear;
  
    // Last Modified Date
    const lastModifiedDate = new Date(document.lastModified);
    document.querySelector('footer p:last-of-type').textContent += lastModifiedDate;
  });