
const loginForm = document.getElementById("login-form");
const closeForm = document.getElementById("close-form");
const openLogin = document.getElementById("open-login");
const dialog = document.querySelectorAll(".dialog-modal");
const openDialog = document.querySelectorAll(".open-dialog");
const closeDialog = document.querySelectorAll(".close-dialog");
const cancelDialog = document.querySelectorAll(".cancel-dialog");
const closeSignupForm = document.getElementById("close-signup-form")


openLogin.addEventListener("click", () => {
    loginForm.classList.replace("hidden", "flex");
});

closeForm.addEventListener("click", () => {
    loginForm.classList.replace("flex", "hidden");
});

for (const key in openDialog) {
    if (Object.hasOwnProperty.call(openDialog, key)) {
        const element = openDialog[key];
        element.addEventListener("click", () => {
            dialog[key].classList.replace("hidden", "flex");
        });
    }
}

for (const key in closeDialog) {
    if (Object.hasOwnProperty.call(closeDialog, key)) {
        const element = closeDialog[key];
        element.addEventListener("click", () => {
            dialog[key].classList.replace("flex", "hidden");
        });
    }
}

for (const key in cancelDialog) {
    if (Object.hasOwnProperty.call(cancelDialog, key)) {
        const element = cancelDialog[key];
        element.addEventListener("click", () => {
            dialog[key].classList.replace("flex", "hidden");

        });
    }
}