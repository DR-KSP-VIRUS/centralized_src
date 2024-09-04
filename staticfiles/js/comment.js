const comments = document.querySelectorAll(".comment-sections");
const commentForms = document.querySelectorAll(".comment-forms");
const loginComment = document.querySelectorAll(".login-comment");
const commentInfo = document.getElementById("comment-info");
const closeInfo = document.getElementById("close-comment-info");


for (const key in comments) {
    if (Object.prototype.hasOwnProperty.call(comments, key)) {
        const element = comments[key];
        element.addEventListener('click', () => {
            commentForms[key].classList.toggle('hidden');
        });
    }
}

for (const key in loginComment) {
    if (Object.prototype.hasOwnProperty.call(loginComment, key)) {
        const element = loginComment[key];
        element.addEventListener('click', () => {
            commentInfo.classList.replace("hidden", "flex");
        })

    }
}

closeInfo.addEventListener("click", () => {
    commentInfo.classList.replace("flex", "hidden");
});
