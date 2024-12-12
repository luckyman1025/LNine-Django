document.addEventListener("DOMContentLoaded", function () {
  refreshOptions();
});

function refreshOptions() {
  console.log("LLLLLLLLLLL");

  const profileList = document.getElementById('profile_list');
    
  // Clear existing profiles
  profileList.innerHTML = '';

  fetch("/get_profile_list/")
    .then((response) => response.json())
    .then((data) => {
      console.log("options", data.user_profiles);
      profiles = data.user_profiles

      profiles.forEach((profile) => {
        const listItem = document.createElement("li");
        listItem.className = "nav-link";

        const form = document.createElement("form");
        form.method = "POST";
        form.action = "/switch_profile/"; // Ensure this matches your URL
        form.className = "profile-switch-form";

        // CSRF Token (assuming you'll pass it from the server)
        const csrfInput = document.createElement("input");
        csrfInput.type = "hidden";
        csrfInput.name = "csrfmiddlewaretoken";
        csrfInput.value = getCsrfToken() || ''; // You'll need to implement this
        form.appendChild(csrfInput);

        // Profile ID input
        const profileIdInput = document.createElement("input");
        profileIdInput.type = "hidden";
        profileIdInput.name = "profile_id";
        profileIdInput.value = profile.id;
        form.appendChild(profileIdInput);

        // Button
        const button = document.createElement("button");
        button.type = "submit";
        button.className = "nav-item dropdown-item profile-switch-btn";

        // Bank icon
        const icon = document.createElement("i");
        icon.className = "tim-icons icon-bank mr-2";
        button.appendChild(icon);

        // Company name
        const companyText = document.createTextNode(
          ` ${profile.company.name} `
        );
        button.appendChild(companyText);

        // Badge
        const badge = document.createElement("span");
        badge.className = profile.is_active
          ? "badge badge-sm bg-gradient-success float-right"
          : "badge badge-sm bg-gradient-secondary float-right";
        badge.textContent = profile.is_active ? "Active" : "Switch";
        button.appendChild(badge);

        form.appendChild(button);
        listItem.appendChild(form);
        profileList.appendChild(listItem);
      });
    });
}

function getCsrfToken() {
    const csrfElement = document.querySelector('[name=csrfmiddlewaretoken]');
    
    // If the element doesn't exist, try to get it from a cookie
    if (!csrfElement) {
        return getCsrfTokenFromCookie();
    }
    
    return csrfElement.value;
}

function getCsrfTokenFromCookie() {
    // Fallback method to get CSRF token from cookies
    const cookieName = 'csrftoken';
    let cookieValue = null;
    
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, cookieName.length + 1) === (cookieName + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(cookieName.length + 1));
                break;
            }
        }
    }
    
    return cookieValue;
}